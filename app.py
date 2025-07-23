import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("salary_model.pkl", "rb"))

st.title("Employee Salary Prediction")

age = st.slider("Age", 18, 65, 25)
gender = st.selectbox("Gender", ["Male", "Female"])
degree = st.selectbox("Highest Degree", [ "Bachelor's", "Master's", "PhD"])
job_title = st.selectbox("Job Title", ["Software Engineer", "Data Analyst", "Manager", "HR", "Others"])
experience_years = st.slider("Years of Experience", 0, 40, 1)


def encode_inputs(age, gender, degree, job, experience):
    age_scaled = age / 100
    experience_scaled = experience / 40

    gender_map = {"Male": 1, "Female": 0}
    degree_map = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
    job_map = {"Software Engineer": 0, "Data Analyst": 1, "Manager": 2, "HR": 3, "Others": 4}

    return np.array([[age_scaled,
                    gender_map[gender],
                    degree_map[degree],
                    job_map[job],
                    experience_scaled]])


if st.button("Predict Salary"):
    input_features = encode_inputs(age, gender, degree, job_title, experience_years)
    salary = model.predict(input_features)[0]
    st.success(f"Predicted Salary: INR {salary:,.2f}")