import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("churn_model.pkl")
columns = joblib.load("model_columns.pkl")

st.set_page_config(page_title="Patient Churn Intelligence", layout="wide")

st.title("🏥 Patient Churn Intelligence System")
st.markdown("### Predict patient churn risk and analyze engagement patterns")

# ---------------- SIDEBAR INPUT ---------------- #

st.sidebar.header("Enter Patient Details")

patient_id = st.sidebar.number_input("Patient ID", min_value=1, value=1001)

age = st.sidebar.slider("Age", 18, 90, 40)

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
gender_encoded = 1 if gender == "Male" else 0

tenure = st.sidebar.slider("Tenure (Months)", 0, 60, 12)

visits = st.sidebar.slider("Visits Last Year", 0, 30, 5)

chronic = st.sidebar.selectbox("Chronic Disease", ["No", "Yes"])
chronic_encoded = 1 if chronic == "Yes" else 0

insurance = st.sidebar.selectbox("Insurance Type", ["Private", "Public"])
insurance_encoded = 1 if insurance == "Private" else 0

satisfaction = st.sidebar.slider("Satisfaction Score", 1, 10, 5)

bill_amount = st.sidebar.number_input("Total Bill Amount", min_value=0.0, value=10000.0)

missed = st.sidebar.slider("Missed Appointments", 0, 10, 1)

# ---------------- CREATE INPUT DATAFRAME ---------------- #

input_dict = {
    "Patient_ID": patient_id,
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

# Ensure correct column order
input_df = input_df[columns]

# ---------------- PREDICTION ---------------- #

if st.sidebar.button("Predict Churn"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    st.write(f"### Churn Probability: {probability:.2%}")

    st.progress(float(probability))

    if prediction == 1:
        st.error("⚠️ High Risk of Churn")
    else:
        st.success("✅ Low Risk of Churn")

    # ---------------- BUSINESS INSIGHT ---------------- #

    st.markdown("### 📊 Risk Interpretation")

    if probability > 0.7:
        st.warning("Critical risk. Immediate retention intervention recommended.")
    elif probability > 0.4:
        st.info("Moderate risk. Monitor patient engagement.")
    else:
        st.success("Patient appears stable.")

    # Revenue Risk Insight
    if probability > 0.5:
        potential_loss = bill_amount
        st.markdown(f"### 💰 Potential Revenue at Risk: ₹{potential_loss:,.2f}")