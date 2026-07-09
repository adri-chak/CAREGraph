from fastapi import APIRouter
from backend.models.patient import PatientProfile

router = APIRouter()


@router.post("/patient")
def create_patient(patient: PatientProfile):
    return {
        "message": "Patient profile received successfully!",
        "patient": patient
    }