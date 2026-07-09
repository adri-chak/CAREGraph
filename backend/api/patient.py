from fastapi import APIRouter
from backend.models.patient import PatientProfile
from backend.agents.clinical_reasoning import ClinicalReasoningAgent

router = APIRouter()

agent = ClinicalReasoningAgent()


@router.post("/patient")
def analyze_patient(patient: PatientProfile):

    result = agent.analyze(patient)

    return {
        "patient": patient,
        "clinical_reasoning": result
    }