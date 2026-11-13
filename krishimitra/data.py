# data.py - static data used by the whole project.
# NOTE: values are typical/approximate. Before your viva, replace prices with Agmarknet
# data and soil values with Soil Health Card data for better accuracy.
# Every text field is (English, Kannada) or has a "kn" key.

DISTRICTS = {
    "Mysuru":        dict(kn="ಮೈಸೂರು", alt=["mysore"], lat=12.30, lon=76.65, rain=780, water=200, temp=26, hum=65, N=70, P=40, K=40, ph=6.5, soil=("Red loamy soil", "ಕೆಂಪು ಗೋಡು ಮಣ್ಣು")),
    "Mandya":        dict(kn="ಮಂಡ್ಯ", alt=[], lat=12.52, lon=76.90, rain=700, water=800, temp=27, hum=68, N=85, P=45, K=45, ph=6.8, soil=("Red sandy loam (canal irrigated)", "ಕೆಂಪು ಮರಳು ಗೋಡು ಮಣ್ಣು (ನಾಲೆ ನೀರಾವರಿ)")),
    "Belagavi":      dict(kn="ಬೆಳಗಾವಿ", alt=["belgaum"], lat=15.85, lon=74.50, rain=1000, water=150, temp=25, hum=70, N=75, P=42, K=50, ph=6.9, soil=("Black and red soil", "ಕಪ್ಪು ಮತ್ತು ಕೆಂಪು ಮಣ್ಣು")),
    "Dharwad":       dict(kn="ಧಾರವಾಡ", alt=[], lat=15.46, lon=75.01, rain=750, water=0, temp=25, hum=62, N=60, P=45, K=55, ph=7.4, soil=("Deep black cotton soil", "ಆಳವಾದ ಕಪ್ಪು ಮಣ್ಣು")),
    "Raichur":       dict(kn="ರಾಯಚೂರು", alt=[], lat=16.20, lon=77.36, rain=620, water=100, temp=29, hum=55, N=55, P=35, K=50, ph=7.8, soil=("Black soil", "ಕಪ್ಪು ಮಣ್ಣು")),
    "Kalaburagi":    dict(kn="ಕಲಬುರಗಿ", alt=["gulbarga"], lat=17.33, lon=76.83, rain=750, water=0, temp=28, hum=55, N=45, P=35, K=45, ph=7.9, soil=("Medium black soil", "ಮಧ್ಯಮ ಕಪ್ಪು ಮಣ್ಣು")),
    "Ballari":       dict(kn="ಬಳ್ಳಾರಿ", alt=["bellary"], lat=15.14, lon=76.92, rain=580, water=150, temp=29, hum=52, N=50, P=38, K=48, ph=7.6, soil=("Black and red mixed soil", "ಕಪ್ಪು ಮತ್ತು ಕೆಂಪು ಮಿಶ್ರ ಮಣ್ಣು")),
    "Shivamogga":    dict(kn="ಶಿವಮೊಗ್ಗ", alt=["shimoga"], lat=13.93, lon=75.57, rain=1800, water=0, temp=24, hum=82, N=80, P=40, K=38, ph=5.8, soil=("Laterite soil", "ಜಂಬಿಟ್ಟಿಗೆ ಮಣ್ಣು")),
    "Chikkamagaluru":dict(kn="ಚಿಕ್ಕಮಗಳೂರು", alt=["chikmagalur"], lat=13.32, lon=75.77, rain=1700, water=0, temp=22, hum=80, N=95, P=30, K=40, ph=5.6, soil=("Forest loam / laterite", "ಅರಣ್ಯ ಗೋಡು / ಜಂಬಿಟ್ಟಿಗೆ ಮಣ್ಣು")),
    "Tumakuru":      dict(kn="ತುಮಕೂರು", alt=["tumkur"], lat=13.34, lon=77.10, rain=650, water=0, temp=27, hum=60, N=50, P=40, K=35, ph=6.1, soil=("Red sandy soil", "ಕೆಂಪು ಮರಳು ಮಣ್ಣು")),
}

# N,P,K,temp,hum,water(mm),ph = ideal growing conditions; price in Rs per quintal (min,max)
CROPS = {
    "Rice":      dict(kn="ಭತ್ತ", alt=["paddy"], prof=(80,45,40,25,80,1300,6.2), price=(2200,2600), season=("Kharif (Jun-Oct)", "ಮುಂಗಾರು (ಜೂನ್-ಅಕ್ಟೋಬರ್)"), tip=("Needs standing water; use SRI method to save water.", "ನೀರು ನಿಲ್ಲುವ ಜಮೀನು ಬೇಕು; ನೀರು ಉಳಿಸಲು ಶ್ರೀ ಪದ್ಧತಿ ಬಳಸಿ.")),
    "Ragi":      dict(kn="ರಾಗಿ", alt=["finger millet"], prof=(50,40,35,26,65,650,6.0), price=(3800,4300), season=("Kharif (Jun-Nov)", "ಮುಂಗಾರು (ಜೂನ್-ನವೆಂಬರ್)"), tip=("Drought tolerant, good for red soils.", "ಬರ ತಡೆದುಕೊಳ್ಳುತ್ತದೆ, ಕೆಂಪು ಮಣ್ಣಿಗೆ ಸೂಕ್ತ.")),
    "Maize":     dict(kn="ಮೆಕ್ಕೆಜೋಳ", alt=["corn"], prof=(80,45,40,26,65,800,6.5), price=(2000,2400), season=("Kharif / Rabi", "ಮುಂಗಾರು / ಹಿಂಗಾರು"), tip=("Avoid waterlogging; sow with first good rain.", "ನೀರು ನಿಲ್ಲದಂತೆ ನೋಡಿ; ಮೊದಲ ಮಳೆಗೆ ಬಿತ್ತನೆ ಮಾಡಿ.")),
    "Jowar":     dict(kn="ಜೋಳ", alt=["sorghum"], prof=(45,35,45,28,55,600,7.3), price=(3000,3600), season=("Rabi (Oct-Feb)", "ಹಿಂಗಾರು (ಅಕ್ಟೋಬರ್-ಫೆಬ್ರವರಿ)"), tip=("Best on deep black soil with stored moisture.", "ತೇವಾಂಶವಿರುವ ಆಳವಾದ ಕಪ್ಪು ಮಣ್ಣಿನಲ್ಲಿ ಉತ್ತಮ.")),
    "Cotton":    dict(kn="ಹತ್ತಿ", alt=[], prof=(90,40,50,28,55,800,7.4), price=(6500,7500), season=("Kharif (Jun-Dec)", "ಮುಂಗಾರು (ಜೂನ್-ಡಿಸೆಂಬರ್)"), tip=("Watch for pink bollworm; use pheromone traps.", "ಗುಲಾಬಿ ಕಾಯಿಕೊರಕ ಹುಳುವಿಗೆ ಫೆರೋಮೋನ್ ಬಲೆ ಬಳಸಿ.")),
    "Sugarcane": dict(kn="ಕಬ್ಬು", alt=[], prof=(90,50,60,28,70,1800,7.0), price=(340,380), season=("Year-round planting", "ವರ್ಷವಿಡೀ ನಾಟಿ"), tip=("Heavy water need; drip irrigation saves 40% water.", "ಹೆಚ್ಚು ನೀರು ಬೇಕು; ಹನಿ ನೀರಾವರಿಯಿಂದ ಶೇ.40 ನೀರು ಉಳಿತಾಯ.")),
    "Groundnut": dict(kn="ಕಡಲೆಕಾಯಿ", alt=["peanut"], prof=(30,45,40,27,60,650,6.3), price=(5800,6600), season=("Kharif / Summer", "ಮುಂಗಾರು / ಬೇಸಿಗೆ"), tip=("Add gypsum at flowering for better pods.", "ಹೂ ಬಿಡುವ ಸಮಯದಲ್ಲಿ ಜಿಪ್ಸಂ ಹಾಕಿ.")),
    "Tur":       dict(kn="ತೊಗರಿ", alt=["redgram", "pigeon pea", "toor"], prof=(25,50,40,27,58,700,6.8), price=(7000,8000), season=("Kharif (Jun-Jan)", "ಮುಂಗಾರು (ಜೂನ್-ಜನವರಿ)"), tip=("Good as intercrop with jowar or cotton.", "ಜೋಳ ಅಥವಾ ಹತ್ತಿಯೊಂದಿಗೆ ಅಂತರ ಬೆಳೆಯಾಗಿ ಒಳ್ಳೆಯದು.")),
    "Coffee":    dict(kn="ಕಾಫಿ", alt=[], prof=(100,30,40,22,80,1800,5.6), price=(18000,26000), season=("Perennial (harvest Nov-Feb)", "ಬಹುವಾರ್ಷಿಕ (ಕೊಯ್ಲು ನವೆಂಬರ್-ಫೆಬ್ರವರಿ)"), tip=("Needs shade trees and well drained slopes.", "ನೆರಳಿನ ಮರಗಳು ಮತ್ತು ನೀರು ಬಸಿಯುವ ಇಳಿಜಾರು ಬೇಕು.")),
    "Sunflower": dict(kn="ಸೂರ್ಯಕಾಂತಿ", alt=[], prof=(60,40,50,27,55,600,7.0), price=(6000,7000), season=("Rabi / Summer", "ಹಿಂಗಾರು / ಬೇಸಿಗೆ"), tip=("Short duration, fits well after kharif crops.", "ಕಡಿಮೆ ಅವಧಿಯ ಬೆಳೆ, ಮುಂಗಾರಿನ ನಂತರ ಸೂಕ್ತ.")),
}

SCHEMES = [
    dict(name=("PM-KISAN", "ಪಿಎಂ-ಕಿಸಾನ್"), desc=("Rs 6,000 per year income support in three instalments to farmer families.", "ರೈತ ಕುಟುಂಬಗಳಿಗೆ ವರ್ಷಕ್ಕೆ ₹6,000 ಆದಾಯ ಬೆಂಬಲ, ಮೂರು ಕಂತುಗಳಲ್ಲಿ."), link="https://pmkisan.gov.in"),
    dict(name=("PM Fasal Bima Yojana", "ಪ್ರಧಾನಮಂತ್ರಿ ಫಸಲ್ ಬಿಮಾ ಯೋಜನೆ"), desc=("Crop insurance against drought, flood and pests at a low farmer premium.", "ಬರ, ಪ್ರವಾಹ, ಕೀಟಗಳಿಂದ ಆಗುವ ನಷ್ಟಕ್ಕೆ ಕಡಿಮೆ ಪ್ರೀಮಿಯಂನಲ್ಲಿ ಬೆಳೆ ವಿಮೆ."), link="https://pmfby.gov.in"),
    dict(name=("Kisan Credit Card", "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್"), desc=("Short-term farm loans at subsidised interest through banks.", "ಬ್ಯಾಂಕ್‌ಗಳ ಮೂಲಕ ರಿಯಾಯಿತಿ ಬಡ್ಡಿದರದಲ್ಲಿ ಅಲ್ಪಾವಧಿ ಕೃಷಿ ಸಾಲ."), link="https://www.myscheme.gov.in"),
    dict(name=("Soil Health Card", "ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್"), desc=("Free soil testing and fertiliser advice for your field.", "ನಿಮ್ಮ ಜಮೀನಿಗೆ ಉಚಿತ ಮಣ್ಣು ಪರೀಕ್ಷೆ ಮತ್ತು ಗೊಬ್ಬರ ಸಲಹೆ."), link="https://soilhealth.dac.gov.in"),
    dict(name=("PM Krishi Sinchayee Yojana", "ಪ್ರಧಾನಮಂತ್ರಿ ಕೃಷಿ ಸಿಂಚಾಯಿ ಯೋಜನೆ"), desc=("Subsidy for drip and sprinkler irrigation (more crop per drop).", "ಹನಿ ಮತ್ತು ತುಂತುರು ನೀರಾವರಿಗೆ ಸಹಾಯಧನ."), link="https://pmksy.gov.in"),
    dict(name=("Raitha Siri (Karnataka)", "ರೈತ ಸಿರಿ (ಕರ್ನಾಟಕ)"), desc=("State incentive for farmers growing millets like ragi and jowar.", "ರಾಗಿ, ಜೋಳದಂತಹ ಸಿರಿಧಾನ್ಯ ಬೆಳೆಯುವ ರೈತರಿಗೆ ರಾಜ್ಯ ಪ್ರೋತ್ಸಾಹ ಧನ."), link="https://raitamitra.karnataka.gov.in"),
]
