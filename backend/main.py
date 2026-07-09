from fastapi import FastAPI
from backend.api.patient import router as patient_router

app = FastAPI(
    title="CAREGraph API",
    description="Backend for the CAREGraph Multi-Agent Healthcare System",
    version="0.1.0"
)

app.include_router(patient_router)


@app.get("/")
def home():
    return {
        "message": "CAREGraph Backend is Running!"
    }