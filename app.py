import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("churn_model.pkl")
columns = joblib.load("model_columns.pkl")

st.set_page_config(
    page_title="Patient Churn Intelligence",
    layout="centered"
)

st.title("🏥 Patient Churn Intelligence System")

st.markdown("Predict patient churn risk with an interactive dashboard.")

st.divider()

# -------- Patient Basic Info -------- #

st.subheader("👤 Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 90, 40)
    tenure = st.slider("Tenure (Months)", 0, 60, 12)
    visits = st.slider("Visits Last Year", 0, 30, 5)

with col2:
    satisfaction = st.slider("Satisfaction Score", 1, 10, 5)
    missed = st.slider("Missed Appointments", 0, 10, 1)
    bill_amount = st.number_input("Total Bill Amount", min_value=0.0, value=10000.0)

st.divider()

# -------- Categorical Inputs -------- #

st.subheader("📋 Additional Details")

col3, col4 = st.columns(2)

with col3:
    gender = st.selectbox("Gender", ["Male", "Female"])
    chronic = st.selectbox("Chronic Disease", ["No", "Yes"])

with col4:
    insurance = st.selectbox("Insurance Type", ["Private", "Public"])

# Encode values
gender_encoded = 1 if gender == "Male" else 0
chronic_encoded = 1 if chronic == "Yes" else 0
insurance_encoded = 1 if insurance == "Private" else 0

# -------- Prepare Input -------- #

input_dict = {
    "Age": age,
    "Gender": gender_encoded,
    "Tenure_Months": tenure,
    "Visits_Last_Year": visits,
    "Chronic_Disease": chronic_encoded,
    "Insurance_Type": insurance_encoded,
    "Satisfaction_Score": satisfaction,
    "Total_Bill_Amount": bill_amount,
    "Missed_Appointments": missed
}

input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=columns, fill_value=0)

st.divider()

# -------- Predict Button -------- #

if st.button("🔍 Predict Churn Risk", use_container_width=True):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("📊 Prediction Result")

    st.metric("Churn Probability", f"{probability:.2%}")

    st.progress(float(probability))

    if prediction == 1:
        st.error("⚠️ High Risk of Churn")
    else:
        st.success("✅ Low Risk of Churn")

    if probability > 0.5:
        st.markdown(f"### 💰 Revenue at Risk: ₹{bill_amount:,.2f}")