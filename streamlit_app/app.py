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

        # Show Top Career Paths
        st.subheader("Top Career Paths")

        for role in result["predicted_roles"]:
            st.write(f"{role['role']} ({role['confidence']*100:.2f}%)")

        # Growth
        st.info(f"Growth: {result['growth']}")

        # Recommended Skills
        st.subheader("Recommended Skills")
        st.write(result['recommended_skills'])

    else:
        st.error("Error connecting to API")