from pydantic import BaseModel

class UserInput(BaseModel):
    skills: str
    job_title: str
    experience: int