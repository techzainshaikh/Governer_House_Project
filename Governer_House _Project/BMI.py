import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height_feet):
    # Convert height from feet to meters
    height_meters = height_feet * 0.3048
    bmi = weight / (height_meters ** 2)
    return bmi

# Function to categorize BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Streamlit User Interface
st.title("BMI Calculator")
st.write("### Enter your details below to calculate your BMI:")

# User inputs for weight and height
weight = st.number_input("Weight (kg):", min_value=1.0, step=0.1)
height_feet = st.number_input("Height (feet):", min_value=1.0, step=0.1)

# Check if the button is pressed
if st.button("Calculate BMI"):
    if weight > 0 and height_feet > 0:
        # Calculate BMI
        bmi = calculate_bmi(weight, height_feet)
        category = bmi_category(bmi)
        
        st.write(f"Your BMI is: {bmi:.2f}")
        st.write(f"Category: {category}")
    else:
        st.write("Please enter valid values for weight and height.")
