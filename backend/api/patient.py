from fastapi import APIRouter

from backend.models.patient import PatientProfile
from backend.agents.clinical_reasoning import ClinicalReasoningAgent
from backend.agents.evidence_agent import EvidenceAgent

router = APIRouter()

clinical = ClinicalReasoningAgent()
evidence = EvidenceAgent()


from backend.core.workflow import graph


@router.post("/patient")
def analyze(patient: PatientProfile):

    state = {
        "patient": patient.model_dump(),
        "clinical_reasoning": {},
        "evidence": {},
        "medication": {},
        "consensus": {}
    }

    result = graph.invoke(state)

    return result