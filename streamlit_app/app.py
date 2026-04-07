import streamlit as st
import requests

st.title("ProPath - Career Predictor")

skills = st.text_input("Enter Skills (comma separated)")
job_title = st.text_input("Current Job Title")
experience = st.slider("Years of Experience", 0, 10, 1)

if st.button("Predict"):
    data = {
        "skills": skills,
        "job_title": job_title,
        "experience": experience
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    if response.status_code == 200:
        result = response.json()

        st.success(f"Next Role: {result['next_role']}")
        
        st.subheader("Top Career Options")
        for i, role in enumerate(result["top_roles"], 1):
            st.write(f"{i}. {role['role']} ({role['confidence']}%)")

        st.info(f"Growth: {result['growth']}")