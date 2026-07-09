from fastapi import APIRouter
from backend.models.patient import PatientProfile
from backend.agents.clinical_reasoning import ClinicalReasoningAgent
from backend.agents.evidence_agent import EvidenceAgent

router = APIRouter()

clinical_agent = ClinicalReasoningAgent()
evidence_agent = EvidenceAgent()


@router.post("/patient")
def analyze_patient(patient: PatientProfile):

    clinical_result = clinical_agent.analyze(patient)

    evidence_result = evidence_agent.verify(clinical_result)

    return {
        "patient": patient,
        "clinical_reasoning": clinical_result,
        "evidence_verification": evidence_result
    }