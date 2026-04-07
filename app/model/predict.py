import joblib
import pandas as pd
from collections import Counter
from app.model.preprocess import transform_input

df = pd.read_csv("data/dataset.csv")

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_role(skills):
    X = transform_input(skills, vectorizer)
    return model.predict(X)[0]

def growth_category(exp):
    if exp < 2:
        return "High"
    elif exp < 5:
        return "Medium"
    else:
        return "Stable"

def recommend_skills(predicted_role, user_skills, top_n=5):
    role_data = df[df['next_job_role'] == predicted_role]

    all_skills = []
    for skills in role_data['skills']:
        skill_list = [s.strip().lower() for s in skills.split(",")]
        all_skills.extend(skill_list)

    skill_counts = Counter(all_skills)

    user_skill_set = set([s.strip().lower() \
                          for s in user_skills.split(",")])

    # Remove existing skills
    filtered_skills = [
        skill for skill, _ in skill_counts.most_common()
        if skill not in user_skill_set
    ]

    return filtered_skills[:top_n]