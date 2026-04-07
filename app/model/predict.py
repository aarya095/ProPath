import joblib
import numpy as np
import pandas as pd
from collections import Counter
from app.model.preprocess import transform_input

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

def get_top_roles(skills, model, vectorizer, label_encoder):
    # Convert input text → vector
    input_vector = vectorizer.transform([skills])

    probs = model.predict_proba(input_vector)[0]

    top_indices = probs.argsort()[-3:][::-1]

    results = []
    for idx in top_indices:
        role = label_encoder.inverse_transform([idx])[0]
        confidence = round(probs[idx] * 100, 2)
        results.append({"role": role, "confidence": confidence})

    return results

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