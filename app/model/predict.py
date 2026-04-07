import joblib
import numpy as np
import pandas as pd
from collections import Counter
from app.model.preprocess import transform_input

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_roles(skills, job_title, experience, top_n=3):
    X = transform_input(skills, job_title, experience, vectorizer)

    # Get probabilities
    probs = model.predict_proba(X)[0]

    # Get class labels
    classes = model.classes_

    # Get top N indices
    top_indices = np.argsort(probs)[-top_n:][::-1]

    # Return top roles with probabilities
    results = [
        {"role": classes[i], "confidence": float(probs[i])}
        for i in top_indices
    ]

    return results

def growth_category(exp):
    if exp < 2:
        return "High"
    elif exp < 5:
        return "Medium"
    else:
        return "Stable"

df = pd.read_csv("data/dataset.csv")

def recommend_skills(role, top_n=5):
    # Filter dataset for given role
    role_data = df[df['next_job_role'] == role]

    if role_data.empty:
        return ["Cloud", "AI", "Data Structures"]  # fallback

    all_skills = []

    for skills in role_data['skills']:
        # Split comma-separated skills
        skill_list = [s.strip().lower() for s in skills.split(",")]
        all_skills.extend(skill_list)

    # Count frequency
    skill_counts = Counter(all_skills)

    # Get top N skills
    top_skills = [skill for skill, _ in skill_counts.most_common(top_n)]

    return top_skills