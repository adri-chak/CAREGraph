from backend.services.openfda_service import search_drug


class MedicationAgent:

    def run(self, state):

        medications = state["patient"]["medications"]

        report = []

        for medicine in medications:

            report.append(

                {

                    "medicine": medicine,

                    "details": search_drug(medicine)

                }

            )

        state["medication"] = report

        return state