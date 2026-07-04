from fastapi import FastAPI
from pydantic import BaseModel
from src.decay_model import calculate_survival_prob

app = FastAPI(title="Temporal Knowledge Decay API")

class DecayRequest(BaseModel):
    half_life_days: float
    current_age_days: float

@app.post("/survival")
def survival(req: DecayRequest):
    prob = calculate_survival_prob(req.half_life_days, req.current_age_days)
    return {"survival_probability": float(prob)}
