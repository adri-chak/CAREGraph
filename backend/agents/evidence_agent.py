from backend.services.llm_service import get_llm
from backend.utils.json_parser import parse_json

class EvidenceAgent:

    def __init__(self):
        self.llm = get_llm()

    def run(self, state):

        prompt = f"""
Verify this clinical reasoning.

{state["clinical_reasoning"]}

Return ONLY valid JSON.

{{
"evidence_strength":"",
"missing_information":[],
"recommended_tests":[],
"red_flags":[]
}}
"""

        response = self.llm.invoke(prompt)

        state["evidence"] = parse_json(response.content)

        return state