# nlp.py - small bilingual (Kannada + English) NLP for the question box.
# Steps: 1) detect language  2) normalise Kannada word endings (stemming)
#        3) find district / crop names  4) detect intent keywords  5) reply in same language
from data import DISTRICTS, CROPS, SCHEMES

KEYWORDS = {
    "price":   ["price", "rate", "cost", "market", "ಬೆಲೆ", "ದರ", "ಮಾರುಕಟ್ಟೆ"],
    "scheme":  ["scheme", "subsidy", "loan", "insurance", "ಯೋಜನೆ", "ಸಬ್ಸಿಡಿ", "ಸಾಲ", "ವಿಮೆ"],
    "soil":    ["soil", "ಮಣ್ಣು", "ಮಣ್ಣಿನ"],
    "weather": ["weather", "rain", "temperature", "climate", "ಹವಾಮಾನ", "ಮಳೆ", "ತಾಪಮಾನ"],
}

def is_kannada(text):
    return any("\u0c80" <= ch <= "\u0cff" for ch in text)

def stem(word):
    # Kannada adds endings to words (ಮೈಸೂರು -> ಮೈಸೂರಿನಲ್ಲಿ), so we cut the last vowel sign
    return word.rstrip("ುಿೆೊಂ")

def answer_query(text, rank_fn):
    kn = is_kannada(text)
    i = 1 if kn else 0
    low = text.lower()
    dist = next((n for n, d in DISTRICTS.items()
                 if n.lower() in low or any(a in low for a in d["alt"]) or stem(d["kn"]) in text), None)
    crop = next((c for c, d in CROPS.items()
                 if c.lower() in low or any(a in low for a in d["alt"]) or stem(d["kn"]) in text), None)
    intents = [k for k, words in KEYWORDS.items() if any(stem(w) in low for w in words)]
    cname = lambda c: CROPS[c]["kn"] if kn else c
    dname = lambda d: DISTRICTS[d]["kn"] if kn else d

    if "scheme" in intents:
        names = ", ".join(s["name"][i] for s in SCHEMES)
        return ("ಲಭ್ಯವಿರುವ ಯೋಜನೆಗಳು: " if kn else "Schemes for you: ") + names
    if "price" in intents:
        if crop:
            lo, hi = CROPS[crop]["price"]
            return (f"{cname(crop)} ಬೆಲೆ ₹{lo}-{hi} ಪ್ರತಿ ಕ್ವಿಂಟಾಲ್." if kn
                    else f"{crop} sells around Rs {lo}-{hi} per quintal.")
        return ", ".join(f"{cname(c)}: ₹{d['price'][0]}-{d['price'][1]}" for c, d in CROPS.items())
    if dist and "soil" in intents:
        d = DISTRICTS[dist]
        return (f"{dname(dist)} ಮಣ್ಣು: {d['soil'][1]}, pH {d['ph']}." if kn
                else f"Soil in {dist}: {d['soil'][0]}, pH {d['ph']}.")
    if dist and "weather" in intents:
        d = DISTRICTS[dist]
        return (f"{dname(dist)}: ವಾರ್ಷಿಕ ಮಳೆ {d['rain']} ಮಿಮೀ, ತಾಪಮಾನ {d['temp']}°C, ತೇವಾಂಶ {d['hum']}%." if kn
                else f"{dist}: about {d['rain']} mm rain a year, {d['temp']}°C, humidity {d['hum']}%.")
    if dist:
        top = [cname(c) for c, _ in rank_fn(DISTRICTS[dist])[:3]]
        return (f"{dname(dist)} ಜಿಲ್ಲೆಗೆ ಉತ್ತಮ ಬೆಳೆಗಳು: " if kn else f"Best crops for {dist}: ") + ", ".join(top)
    if crop:
        c = CROPS[crop]
        return (f"{cname(crop)}: ಋತು {c['season'][1]}. {c['tip'][1]}" if kn
                else f"{crop}: season {c['season'][0]}. {c['tip'][0]}")
    return ("ಕ್ಷಮಿಸಿ, ಅರ್ಥವಾಗಲಿಲ್ಲ. ಉದಾಹರಣೆ: 'ಮೈಸೂರಿನಲ್ಲಿ ಯಾವ ಬೆಳೆ ಬೆಳೆಯಬೇಕು?'" if kn
            else "Sorry, I did not get that. Try: 'Which crop is best in Mysuru?'")
