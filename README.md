# 🩺 Diabetes Prediction System

## 📌 Project Overview

The Diabetes Prediction System is a Machine Learning web application that predicts whether a person is likely to have diabetes based on their **Glucose Level** and **BMI (Body Mass Index)**.

The application uses a trained Machine Learning model and provides predictions through a modern, user-friendly web interface built with Flask, HTML, CSS, and JavaScript.

---

## 🚀 Features

* Modern and responsive user interface
* Real-time diabetes prediction
* Machine Learning integration using Scikit-Learn
* Flask backend API
* Interactive result display
* Input validation
* Smooth animations and professional design

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* Pandas
* Joblib

---

## 📂 Project Structure

```text
Diabetes-Prediction-System/
│
├── templates/
│   └── home.html
│
├── diabetes_model.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Diabetes-Prediction-System
```

### Step 2: Install Required Packages

```bash
pip install flask pandas scikit-learn joblib
```

### Step 3: Run the Application

```bash
python app.py
```

---

## ▶️ Usage

1. Open your browser.
2. Navigate to:

```text
http://127.0.0.1:5000
```

3. Enter:

   * Glucose Level
   * BMI Value

4. Click **Predict Result**.

5. The system will display:

   * ✅ No Diabetes Detected
   * ⚠️ High Risk of Diabetes

---

## 🧠 Machine Learning Workflow

1. Collect diabetes dataset.
2. Select important features:

   * Glucose
   * BMI
3. Train Machine Learning model.
4. Save model using Joblib.
5. Load model in Flask application.
6. Predict results based on user inputs.

---

## 📊 Input Parameters

| Parameter | Description                 |
| --------- | --------------------------- |
| Glucose   | Blood glucose concentration |
| BMI       | Body Mass Index             |

---

## 🎯 Future Enhancements

* Add more health parameters
* Display prediction probability
* User authentication
* Prediction history storage
* Database integration
* Deployment on cloud platforms

---

## 👨‍💻 Author

Developed as a Machine Learning and Flask Mini Project for diabetes risk prediction.

---

## 📜 License

This project is intended for educational and learning purposes.
