import streamlit as st
import pickle

# Load the machine learning model
model_path = 'diabetes_model.pkl'
with open(diabetes_model.pkl, 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Diabetes Prediction")

# User input fields
Pregnancies = st.number_input("Enter number of pregnancies:", min_value=0)
Glucose = st.number_input("Enter your glucose level:", min_value=0)
Insulin = st.number_input("Enter your insulin level:", min_value=0)
BMI = st.number_input("Enter your BMI:", min_value=0.0)
DiabetesPedigreeFunction = st.number_input("Enter your diabetes pedigree function:", min_value=0.0)
Age = st.number_input("Enter your age:", min_value=0)

# When the user clicks the predict button
if st.button("Predict"):
    try:
        # Check for missing values
        if None not in [Pregnancies, Glucose, Insulin, BMI, DiabetesPedigreeFunction, Age]:
            output = model.predict([[Pregnancies, Glucose, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if output[0] == 1:
                st.write("The model predicts that the patient has diabetes.")
            else:
                st.write("The model predicts that the patient does not have diabetes.")
        else:
            st.error("Please fill in all fields.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
