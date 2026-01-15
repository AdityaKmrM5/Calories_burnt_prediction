import streamlit as st
import pickle
import numpy as np

# Load model (use relative path for deployment)
model = pickle.load(open("model.pkl", "rb"))

# Display image
st.image(
    "oip.png",
    caption="Stay Healthy!",
    use_column_width=True
)

st.title("Calorie Burnt Prediction App")
st.subheader("Created by Aditya")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 10, 80)
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
duration = st.number_input("Workout Duration (minutes)")
heart_rate = st.number_input("Heart Rate")

# Predict
if st.button("Predict"):
    gender_val = 0 if gender == "Male" else 1
    bmi = weight / ((height / 100) ** 2)

    body_temp = 37.0  # default value for model compatibility

    input_data = np.array([[
        gender_val,
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp
    ]])

    prediction = model.predict(input_data)

    # BMI Category
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    st.success(f" Calories Burned: {prediction[0]:.2f}")
    st.info(f" BMI: {bmi:.2f} ({bmi_category})")
