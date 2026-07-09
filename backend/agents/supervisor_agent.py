class SupervisorAgent:

    def run(self, state):

        confidence = state["clinical_reasoning"].get("confidence", 0)

        red_flags = state["evidence"].get("red_flags", [])

        decision = {}

        if confidence < 0.75:

            decision["action"] = "Need More Investigation"

        else:

            decision["action"] = "Sufficient Confidence"

        if len(red_flags) > 0:

            decision["priority"] = "HIGH"

        else:

            decision["priority"] = "NORMAL"

        decision["next_step"] = state["clinical_reasoning"]["next_step"]

        state["consensus"] = decision

        return state