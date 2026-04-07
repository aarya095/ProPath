from fastapi import FastAPI
from app.schemas import UserInput
from app.model.predict import predict_roles, growth_category, recommend_skills

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ProPath API running"}

@app.post("/predict")
def predict(data: UserInput):

    role_predictions = predict_roles(
        data.skills,
        data.job_title,
        data.experience,
        top_n=3
    )

    growth = growth_category(data.experience)

    # Recommend skills based on top role
    top_role = role_predictions[0]["role"]
    skills = recommend_skills(top_role)

    return {
        "predicted_roles": role_predictions,
        "growth": growth,
        "recommended_skills": skills
    }