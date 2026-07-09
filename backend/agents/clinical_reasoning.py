from backend.services.llm_service import get_llm
from backend.utils.json_parser import parse_json

class ClinicalReasoningAgent:

    def __init__(self):
        self.llm = get_llm()

    def run(self, state):

        patient = state["patient"]

        prompt = f"""
You are an experienced physician.

Patient Details

Age: {patient['age']}
Gender: {patient['gender']}
Symptoms: {', '.join(patient['symptoms'])}
Duration: {patient['duration']}
Medications: {', '.join(patient['medications'])}
Allergies: {', '.join(patient['allergies'])}

Return ONLY valid JSON.

{{
"possible_conditions": [],
"confidence": 0,
"reasoning":"",
"next_step":""
}}
"""

        response = self.llm.invoke(prompt)

        state["clinical_reasoning"] = parse_json(response.content)

        return state