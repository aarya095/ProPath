import joblib
from app.model.preprocess import transform_input

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_role(skills, job_title, experience):
    X = transform_input(skills, job_title, experience, vectorizer)
    return model.predict(X)[0]

def growth_category(exp):
    if exp < 2:
        return "High"
    elif exp < 5:
        return "Medium"
    else:
        return "Stable"

def recommend_skills(role):
    mapping = {
        "Data Analyst": ["Python", "Machine Learning", "Power BI"],
        "Software Engineer": ["System Design", "Docker", "Kubernetes"]
    }
    return mapping.get(role, ["Cloud", "AI", "Data Structures"])