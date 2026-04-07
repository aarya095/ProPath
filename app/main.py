from fastapi import FastAPI
from app.schemas import UserInput
from app.model.predict import get_top_roles, growth_category, recommend_skills, model, vectorizer, label_encoder

app = FastAPI()

@app.post("/predict")
def predict(data: UserInput):
    top_roles = get_top_roles(data.skills, model, vectorizer, label_encoder)

    # First role = best prediction
    next_role = top_roles[0]["role"]

    growth = growth_category(data.experience)
    skills = recommend_skills(next_role)

    return {
        "next_role": next_role,
        "top_roles": top_roles,
        "growth": growth,
        "recommended_skills": skills
    }