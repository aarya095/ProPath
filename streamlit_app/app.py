import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="ProPath",
    layout="centered"
)

# Custom styling
st.markdown("""
    <style>
        .title {
            font-size: 32px;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 16px;
            color: #6c757d;
            margin-bottom: 30px;
        }
        .card {
            padding: 20px;
            border-radius: 10px;
            background-color: #f8f9fa;
            margin-top: 20px;
        }
        .result-title {
            font-weight: 600;
            font-size: 18px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">ProPath</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ML-Based Career Trajectory Predictor</div>', unsafe_allow_html=True)

# Input section
with st.container():
    st.subheader("Input Details")

    col1, col2 = st.columns(2)

    with col1:
        job_title = st.text_input("Current Job Title")

    with col2:
        experience = st.slider("Years of Experience", 0, 10, 1)

    skills = st.text_area("Skills (comma separated)", height=100)

# Button
predict_btn = st.button("Generate Prediction", use_container_width=True)

# Prediction
if predict_btn:
    if not skills or not job_title:
        st.warning("Please fill all fields before submitting.")
    else:
        data = {
            "skills": skills,
            "job_title": job_title,
            "experience": experience
        }

        with st.spinner("Processing..."):
            response = requests.post("http://127.0.0.1:8000/predict", json=data)

        if response.status_code == 200:
            result = response.json()

            st.divider()
            st.subheader("Prediction Results")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Predicted Role**")
                st.success(result["next_role"])

            with col2:
                st.markdown("**Growth Category**")
                st.info(result["growth"])

            st.markdown("**Recommended Skills**")

            skills_html = ""
            for skill in result["recommended_skills"]:
                skills_html += f"""
                    <span style="
                        display:inline-block;
                        background-color:#e9ecef;
                        color: black;
                        padding:6px 10px;
                        margin:5px;
                        border-radius:8px;
                        font-size:14px;">
                        {skill}
                    </span>
                """

            st.markdown(skills_html, unsafe_allow_html=True)

            # 📄 Generate Report
            report = f"""
                        ProPath Career Report
                        ---------------------

                        Input Details:
                        Skills: {skills}
                        Current Job Title: {job_title}
                        Experience: {experience} years

                        Prediction:
                        Next Role: {result['next_role']}
                        Growth Category: {result['growth']}

                        Recommended Skills:
                        {', '.join(result['recommended_skills'])}
                        """

            # 📥 Download Button
            st.download_button(
                label="Download Report",
                data=report,
                file_name="propath_report.txt",
                mime="text/plain"
            )

        else:
            st.error("Unable to connect to backend service.")