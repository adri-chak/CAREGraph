from backend.services.llm_service import get_llm


class ClinicalReasoningAgent:

    def __init__(self):
        self.llm = get_llm()

    def analyze(self, patient):

        prompt = f"""
You are an experienced physician.

Patient Details:

Age: {patient.age}
Gender: {patient.gender}
Symptoms: {", ".join(patient.symptoms)}
Duration: {patient.duration}
Medications: {", ".join(patient.medications)}
Allergies: {", ".join(patient.allergies)}

Return ONLY:

1. Possible Conditions
2. Confidence (0-100)
3. Reasoning
4. Suggested Next Step
"""

        response = self.llm.invoke(prompt)

        return response.content