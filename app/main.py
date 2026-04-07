from fastapi import FastAPI
from app.schemas import UserInput
from app.model.predict import predict_role, growth_category, recommend_skills

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ProPath API running"}

@app.post("/predict")
def predict(data: UserInput):
    next_role = predict_role(data.skills)
    growth = growth_category(data.experience)
    skills = recommend_skills(next_role)

    return {
        "next_role": next_role,
        "growth": growth,
        "recommended_skills": skills
    }