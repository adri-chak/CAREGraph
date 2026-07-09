from pydantic import BaseModel
from typing import List, Optional


class PatientProfile(BaseModel):
    age: int
    gender: str
    symptoms: List[str]
    duration: str
    medications: List[str] = []
    allergies: List[str] = []
    lifestyle: Optional[str] = None