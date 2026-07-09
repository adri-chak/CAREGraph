from langgraph.graph import StateGraph, END
from backend.agents.medication_agent import MedicationAgent

from backend.models.state import CAREGraphState
from backend.agents.clinical_reasoning import ClinicalReasoningAgent
from backend.agents.evidence_agent import EvidenceAgent
from backend.agents.supervisor_agent import SupervisorAgent

clinical = ClinicalReasoningAgent()
evidence = EvidenceAgent()
medication = MedicationAgent()
supervisor = SupervisorAgent()


def supervisor_node(state):
    return supervisor.run(state)


def medication_node(state):
    return medication.run(state)

def clinical_node(state):
    return clinical.run(state)


def evidence_node(state):
    return evidence.run(state)


builder = StateGraph(CAREGraphState)

builder.add_node("clinical", clinical_node)
builder.add_node("evidence", evidence_node)
builder.add_node("medication", medication_node)
builder.add_node("supervisor", supervisor_node)

builder.set_entry_point("clinical")

builder.add_edge("clinical", "evidence")
builder.add_edge("evidence", "medication")
builder.add_edge("medication", "supervisor")
builder.add_edge("supervisor", END)

graph = builder.compile()