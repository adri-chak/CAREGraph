from langgraph.graph import StateGraph, END

from backend.models.state import CAREGraphState
from backend.agents.clinical_reasoning import ClinicalReasoningAgent
from backend.agents.evidence_agent import EvidenceAgent

clinical = ClinicalReasoningAgent()
evidence = EvidenceAgent()


def clinical_node(state):
    return clinical.run(state)


def evidence_node(state):
    return evidence.run(state)


builder = StateGraph(CAREGraphState)

builder.add_node("clinical", clinical_node)
builder.add_node("evidence", evidence_node)

builder.set_entry_point("clinical")

builder.add_edge("clinical", "evidence")
builder.add_edge("evidence", END)

graph = builder.compile()