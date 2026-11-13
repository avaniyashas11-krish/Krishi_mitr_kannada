# train_model.py - builds a dataset and trains the crop recommendation model.
# Run once:  python train_model.py
# To use the real Kaggle "Crop_recommendation.csv", replace make_data() with pd.read_csv(...)
# and keep the same 7 feature columns (N, P, K, temp, humidity, water, ph).
import numpy as np, pandas as pd, joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from data import CROPS

def make_data(per_crop=300, seed=42):
    rng = np.random.default_rng(seed)
    rows = []
    for crop, info in CROPS.items():
        mean = np.array(info["prof"], dtype=float)
        sample = rng.normal(mean, mean * 0.12, size=(per_crop, 7))   # 12% natural variation
        for r in sample:
            rows.append(list(r) + [crop])
    return pd.DataFrame(rows, columns=["N","P","K","temp","humidity","water","ph","crop"])

df = make_data()
X, y = df.drop(columns="crop"), df["crop"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=1)
model = RandomForestClassifier(n_estimators=150, random_state=1).fit(X_tr.values, y_tr)
print("Test accuracy:", round(accuracy_score(y_te, model.predict(X_te.values)), 3))
joblib.dump(model, "model.pkl")
print("Saved model.pkl")
