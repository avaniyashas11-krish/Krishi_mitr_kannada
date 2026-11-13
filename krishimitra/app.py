# app.py - main Flask application. Run with:  python app.py
import sqlite3, joblib, requests
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from data import DISTRICTS, CROPS, SCHEMES
from text import TEXT
from nlp import answer_query

app = Flask(__name__)
app.secret_key = "change-this-secret-before-submission"
model = joblib.load("model.pkl")          # created by train_model.py

def db():
    con = sqlite3.connect("users.db")
    con.row_factory = sqlite3.Row
    return con

with db() as con:
    con.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")

@app.context_processor
def helpers():
    lang = session.get("lang", "en")
    return dict(t=lambda k: TEXT[k][lang], L=lambda pair: pair[1] if lang == "kn" else pair[0], lang=lang)

def login_required(f):
    @wraps(f)
    def wrapper(*a, **kw):
        if "user" not in session:
            flash(TEXT["need_login"][session.get("lang", "en")])
            return redirect(url_for("login"))
        return f(*a, **kw)
    return wrapper

def rank_crops(d):
    """Return [(crop, probability)] sorted best first for a district's conditions."""
    x = [[d["N"], d["P"], d["K"], d["temp"], d["hum"], d["rain"] + d["water"], d["ph"]]]
    probs = model.predict_proba(x)[0]
    return sorted(zip(model.classes_, probs), key=lambda p: -p[1])

def live_weather(d):
    """Current weather from the free Open-Meteo API. Returns None when offline."""
    try:
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={d['lat']}&longitude={d['lon']}"
               "&current=temperature_2m,relative_humidity_2m,precipitation")
        c = requests.get(url, timeout=3).json()["current"]
        return dict(temp=c["temperature_2m"], hum=c["relative_humidity_2m"], rain=c["precipitation"])
    except Exception:
        return None

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lang/<code>")
def set_lang(code):
    session["lang"] = "kn" if code == "kn" else "en"
    return redirect(request.referrer or url_for("home"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        u, p = request.form["username"].strip(), request.form["password"]
        lang = session.get("lang", "en")
        if not u or not p:
            flash(TEXT["empty"][lang])
        else:
            try:
                with db() as con:
                    con.execute("INSERT INTO users (username, password) VALUES (?, ?)", (u, generate_password_hash(p)))
                session["user"] = u
                return redirect(url_for("recommend"))
            except sqlite3.IntegrityError:
                flash(TEXT["exists"][lang])
    return render_template("auth.html", mode="register")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        row = db().execute("SELECT * FROM users WHERE username = ?", (request.form["username"].strip(),)).fetchone()
        if row and check_password_hash(row["password"], request.form["password"]):
            session["user"] = row["username"]
            return redirect(url_for("recommend"))
        flash(TEXT["bad_login"][session.get("lang", "en")])
    return render_template("auth.html", mode="login")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

@app.route("/recommend", methods=["GET", "POST"])
@login_required
def recommend():
    result = None
    if request.method == "POST":
        name, crop = request.form["district"], request.form["crop"]
        if name in DISTRICTS and crop in CROPS:
            d = DISTRICTS[name]
            ranked = rank_crops(d)
            result = dict(name=name, d=d, crop=crop, weather=live_weather(d),
                          top3=[(c, round(p * 100)) for c, p in ranked[:3]],
                          mine=next(round(p * 100) for c, p in ranked if c == crop))
    return render_template("recommend.html", districts=DISTRICTS, crops=CROPS, result=result)

@app.route("/prices")
def prices():
    return render_template("prices.html", crops=CROPS)

@app.route("/schemes")
def schemes():
    return render_template("schemes.html", schemes=SCHEMES)

@app.route("/assistant", methods=["GET", "POST"])
@login_required
def assistant():
    q = reply = None
    if request.method == "POST":
        q = request.form["q"].strip()
        if q:
            reply = answer_query(q, rank_crops)
    return render_template("assistant.html", q=q, reply=reply)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
