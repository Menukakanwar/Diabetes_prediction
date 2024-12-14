from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Loading pickle file
try:
    with open('NB_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    raise Exception(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html') 

@app.route('/prediction')
def prediction():
    return render_template('prediction.html') 

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Form data
            gender = request.form['gender']
            if not gender or gender not in ['male', 'female']:
                return render_template('result.html', prediction_text='Invalid gender input.')

            try:
                age = float(request.form['age'])
                bmi = float(request.form['bmi'])
                hba1c = float(request.form['hba1c'])
            except ValueError:
                return render_template('result.html', prediction_text='Invalid input: Please enter a valid number.')

            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            smoking_history = request.form['smoking_history']
            blood_glucose = float(request.form['blood_glucose'])

            # Input validation
            if not (0 <= bmi <= 100):
                return render_template('result.html', prediction_text='Invalid BMI value. Kindly enter the correct BMI value')
            if not (0 <= hba1c <= 20):
                return render_template('result.html', prediction_text='Invalid HbA1c value. Kindly enter the correct  HbA1c value.')

            # Encoding categorical variables
            gender_encoded = 1 if gender == 'male' else 0  
            smoking_encoded = 1 if smoking_history == 'yes' else 0  

            # Creating input data
            data = np.array([[gender_encoded, age, hypertension, heart_disease, smoking_encoded, bmi, hba1c, blood_glucose]])

            # Prediction
            if model is not None and hasattr(model, 'predict'):
                prediction