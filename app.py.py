from flask import render_template
from flask import Flask,request,jsonify
import pandas as pd
import joblib
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
model=joblib.load('diabetes_model.pkl')
@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    glu = float(data['Glucose'])
    bmi = float(data['BMI'])

    testing = pd.DataFrame(
        [[glu,bmi]],
        columns=['Glucose','BMI']
    )

    prediction = model.predict(testing)

    output = "having disease" if prediction[0]==1 else "No disease"

    return jsonify({'prediction':output}) 
if __name__=="__main__":
    app.run(debug=True)