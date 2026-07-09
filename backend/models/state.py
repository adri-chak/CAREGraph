from typing import TypedDict


class CAREGraphState(TypedDict):

    patient: dict

    clinical_reasoning: dict

    evidence: dict

    medication: dict

    consensus: dict