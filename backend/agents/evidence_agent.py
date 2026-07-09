from backend.services.llm_service import get_llm


class EvidenceAgent:

    def __init__(self):
        self.llm = get_llm()

    def verify(self, clinical_reasoning):

        prompt = f"""
You are an Evidence Verification Agent.

Your task is NOT to diagnose.

Your task is to verify whether the following reasoning is medically reasonable.

Clinical Reasoning:

{clinical_reasoning}

Return ONLY:

1. Evidence Strength (Weak / Moderate / Strong)

2. Missing Information

3. Recommended Diagnostic Tests

4. Possible Red Flags
"""

        response = self.llm.invoke(prompt)

        return response.content