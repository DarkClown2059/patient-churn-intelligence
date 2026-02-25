# 🏥 Patient Churn Intelligence System

A machine learning web application that predicts patient churn risk and provides business-driven retention insights.

---

## 🚀 Project Overview

This project analyzes patient engagement data to predict churn probability using a Random Forest classifier.  

The system enables hospitals to:

- Identify high-risk patients
- Estimate churn probability
- Assess potential revenue at risk
- Support proactive retention strategies

---

## 🌍 Live Demo

The application is deployed using Streamlit Cloud.

🔗 **Access the Live App:**  
👉 https://sahil-patient-churn-app.streamlit.app


## 🧠 Features

- Interactive Streamlit dashboard
- Gender & Insurance dropdown encoding
- Risk probability visualization
- Revenue risk estimation
- Real-time model inference
- Feature-based churn prediction

---

## 📊 Machine Learning Model

- Model: Random Forest Classifier
- Task: Binary Classification (Churn / No Churn)
- Evaluation Metrics:
  - Precision
  - Recall
  - F1 Score
  - ROC-AUC

---

## 🖥️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Project Structure

```
patient_churn_app/
│
├── churn_model.pkl
├── model_columns.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Run Locally

1. Clone the repository:

```
git clone <your-repo-url>
cd patient_churn_app
```

2. Create virtual environment:

```
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
streamlit run app.py
```

---

## 🌍 Deployment

Deployed using Streamlit Cloud.

---

## 📈 Business Value

This system demonstrates how predictive analytics can be applied to healthcare operations to reduce churn and improve revenue stability.

---

## 👤 Author

Sahil Narula  
B.Tech CSE – 3rd Year  
