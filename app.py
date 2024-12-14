from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

#loading pickle file
try:
    with open('NB_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")

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

@app.route('/result', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # form se data
            gender = request.form['gender']
            if gender not in ['Male', 'Female']:  # gender sirf do hote hain
                return render_template('result.html', prediction_text='Invalid gender input.')

            age = float(request.form['age'])
            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            smoking_history = request.form['smoking_history']
            bmi = float(request.form['bmi'])
            hba1c = float(request.form['hba1c'])
            blood_glucose = float(request.form['blood_glucose'])

        
            if not (0 <= bmi <= 100):
                return render_template('result.html', prediction_text='Invalid BMI value. Kindly enter the correct BMI value')
            if not (0 <= hba1c <= 20):
                return render_template('result.html', prediction_text='Invalid HbA1c value. Kindly enter the correct  HbA1c value.')

            
            gender_encoded = 1 if gender == 'male' else 0  
            smoking_encoded = 1 if smoking_history == 'yes' else 0  
            
            
            data = np.array([[gender_encoded, age, hypertension, heart_disease, smoking_encoded, bmi, hba1c, blood_glucose]])
            print(data)
            
            # prediction wla code
            if model is not None:
                prediction = model.predict(data)
            else:
                return render_template('result.html', prediction_text='Try Again!')

            result = "Your predicted diabetes risk is: High" if prediction[0] == 1 else "You don't have diabetes."

            return render_template('result.html', prediction_text=result)

        except ValueError as e:
            print(e)
            return render_template('result.html', prediction_text=f'Invalid input: {str(e)}')
        except Exception as e:
            print(e)
            return render_template('result.html', prediction_text=f'Error occurred: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)

