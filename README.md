# ❤️ Heart Disease Risk Predictor

A web application that predicts heart disease risk using a **Random Forest Classifier** trained on clinical data.

---

## 📁 Project Structure

```
heart_disease_app/
├── app.py                      # Flask backend
├── Heart_Disease___1_.pkl      # Trained ML model
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # Frontend UI
└── README.md
```

---

## 🚀 How to Run Locally

### Step 1 — Prerequisites

Make sure you have **Python 3.8+** installed.

```bash
python --version
```

### Step 2 — Create a Virtual Environment (recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ **Important:** The model was trained with `scikit-learn==1.6.1`.  
> Using a different version may produce a warning but should still work.

### Step 4 — Run the App

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 5 — Open in Browser

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🧠 Model Details

| Property        | Value                        |
|----------------|------------------------------|
| Model Type      | Random Forest Classifier     |
| Output Classes  | 0 = No Disease, 1 = Disease  |
| Input Features  | 16 clinical/lifestyle fields |

### Top Features by Importance

| Feature              | Importance |
|----------------------|------------|
| Sleep Hours          | 14.8%      |
| BMI                  | 14.8%      |
| Cholesterol Level    | 13.4%      |
| Fasting Blood Sugar  | 12.5%      |
| Blood Pressure       | 12.1%      |
| Age                  | 10.7%      |

---

## 📌 Notes

- This app is for **educational/informational purposes only**.
- It is **not** a substitute for professional medical advice.
- The model file must be in the **same directory** as `app.py`.

---

## 🛑 Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: flask` | Run `pip install -r requirements.txt` |
| `Port 5000 already in use` | Change port in `app.py`: `app.run(port=5001)` |
| sklearn version warning | Safe to ignore, or install `scikit-learn==1.6.1` |
| Model not found | Ensure `.pkl` file is in the same folder as `app.py` |
