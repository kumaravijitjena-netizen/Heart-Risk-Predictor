from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the model
model = joblib.load('Heart_Disease___1_.pkl')

FEATURES = ['Age', 'Gender', 'Blood Pressure', 'Cholesterol Level', 'Exercise Habits',
            'Smoking', 'Family Heart Disease', 'Diabetes', 'BMI', 'High Blood Pressure',
            'Alcohol Consumption', 'Stress Level', 'Sleep Hours', 'Sugar Consumption',
            'Fasting Blood Sugar', 'Age_Group']

def get_age_group(age):
    if age < 30:
        return 0
    elif age < 45:
        return 1
    elif age < 60:
        return 2
    else:
        return 3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        age = int(data['age'])
        age_group = get_age_group(age)

        features = [
            age,
            int(data['gender']),
            float(data['blood_pressure']),
            float(data['cholesterol']),
            int(data['exercise_habits']),
            int(data['smoking']),
            int(data['family_heart_disease']),
            int(data['diabetes']),
            float(data['bmi']),
            int(data['high_blood_pressure']),
            int(data['alcohol_consumption']),
            int(data['stress_level']),
            float(data['sleep_hours']),
            int(data['sugar_consumption']),
            float(data['fasting_blood_sugar']),
            age_group
        ]

        X = np.array(features).reshape(1, -1)
        prediction = model.predict(X)[0]
        proba = model.predict_proba(X)[0]

        risk_percent = round(float(proba[1]) * 100, 1)

        if risk_percent < 30:
            risk_level = "Low"
        elif risk_percent < 60:
            risk_level = "Moderate"
        else:
            risk_level = "High"

        return jsonify({
            'prediction': int(prediction),
            'risk_percent': risk_percent,
            'risk_level': risk_level
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
