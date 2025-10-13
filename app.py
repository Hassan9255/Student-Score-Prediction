import streamlit as st     # Streamlit for building the web app interface
import numpy as np         # NumPy for creating input arrays for the model
import joblib              # Joblib for loading the saved machine learning model
import warnings            # Warnings module to suppress warning messages


# Suppress warnings
warnings.filterwarnings("ignore")

# Load the pre-trained model
model = joblib.load("best_model.pkl")

# Streamlit UI
st.title("🎓 Student Exam Score Predictor")

# Input fields
study_hours = st.slider("Study Hours per Day", 0.0, 12.0, 2.0)
attendance = st.slider("Attendance Percentage", 0.0, 100.0, 80.0)
mental_health = st.slider("Mental Health Rating [1-10]", 1, 10, 5)
sleep_hours = st.slider("Sleep Hours per Night", 0.0, 12.0, 7.0)
part_time_job = st.selectbox("Do you have a Part-Time Job?", ["No", "Yes"])

# Encode categorical input
ptj_encoded = 1 if part_time_job == "Yes" else 0

# Predict button
if st.button("Predict Exam Score"):
    input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj_encoded]])
    prediction = model.predict(input_data)[0]

    # Clamp prediction between 0 and 100
    prediction = max(0, min(100, prediction))

    st.success(f"🎯 Predicted Exam Score: **{prediction:.2f}**")
