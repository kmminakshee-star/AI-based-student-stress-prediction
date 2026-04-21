# 🎓 AI-Based Student Stress Prediction System

An intelligent web-based application that predicts student stress levels using Machine Learning.  
The system analyzes user input and classifies stress as Low, Medium, or High.

---

## 🚀 Overview

Student stress is a major issue in academic life. This project provides a simple and effective system to analyze stress levels based on input factors like study patterns and lifestyle.

The goal is to help students understand their stress condition and take necessary actions.

---

## 🧠 Features

- 🔍 Predict student stress level using Machine Learning  
- 🤖 Random Forest ML model  
- ⚡ Real-time prediction using Flask  
- 📊 Dashboard visualization (Low / Medium / High counts)  
- 🔐 User authentication (Login & Register)  
- 💾 Data storage using SQLite database  
- 🌐 Simple and responsive UI  

---

## 🏗️ System Architecture

| Layer        | Technology Used |
|-------------|----------------|
| Frontend     | HTML, CSS |
| Backend      | Flask (Python) |
| ML Model     | Scikit-learn (Random Forest) |
| Database     | SQLite |

---

## 📂 Project Structure

AI-based-student-stress-prediction/

├── app.py  
├── model.py  
├── .gitignore  

├── templates/  
│   ├── login.html  
│   ├── index.html  
│   ├── result.html  
│   ├── dashboard.html  

├── static/  
│   └── style.css  

├── dataset/  
│   └── student_mental_health_burnout.csv  

└── README.md  

---

## ⚙️ Prerequisites

- Python 3.x  
- pip installed  

---

## ⚙️ Setup Guide

### 🔽 1. Clone Repository

git clone https://github.com/kmminakshee-star/AI-based-student-stress-prediction.git  
cd AI-based-student-stress-prediction  

---

### 🐍 2. Install Libraries

pip install flask pandas scikit-learn  

---

### 🤖 3. Train Model

python model.py  

---

### 🚀 4. Run Application

python app.py  

---

### 🌐 5. Open in Browser

http://127.0.0.1:5000  

---

## 🔐 Authentication Flow

- Register new user  
- Login with credentials  
- Redirect to home page  
- Access prediction system  
- Data stored in database  

---

## 📊 Dashboard Features

- Displays number of predictions  
- Shows count of:
  - Low Stress  
  - Medium Stress  
  - High Stress  

---

## 🧠 Machine Learning Model

- Model: Random Forest Classifier  
- Dataset: Student Mental Health Dataset  
- Output:
  - 0 → Low Stress  
  - 1 → Medium Stress  
  - 2 → High Stress  

---

## ⚠️ Important Notes

- Large files (model.pkl, database.db) are excluded using .gitignore  
- Model is trained locally before running the app  
- Database is created automatically  

---

## 🔮 Future Improvements

- 🔐 Secure authentication  
- 📊 Advanced dashboard  
- 🌐 Better UI  
- 🧠 Deep learning model  

---

## 🎯 Project Highlights

- ✔ Machine Learning + Web App  
- ✔ Real-time prediction  
- ✔ Login + Database system  
- ✔ Simple and clean design  

---

## 👩‍💻 Author

Minakshi Singh  
MCA Student  

---

## 🔗 GitHub Repository

https://github.com/kmminakshee-star/AI-based-student-stress-prediction  

