import json
import re


def parse_json(text: str):
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)
    text = text.strip()

    try:
        return json.loads(text)
    except Exception:
        return {
            "error": "Invalid JSON",
            "raw_output": text
        }