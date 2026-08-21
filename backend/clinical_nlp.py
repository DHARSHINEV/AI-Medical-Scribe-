import re


def extract_entities(transcript):

    text = transcript.lower()

    entities = {
        "symptoms": [],
        "medications": [],
        "dosages": [],
        "duration": [],
        "pain_score": [],
        "allergies": [],
        "surgical_history": [],
        "vitals": []
    }

    # Symptoms
    symptom_patterns = [
        "abdominal pain",
        "chest pain",
        "headache",
        "fever",
        "cough",
        "nausea",
        "vomiting"
    ]

    for symptom in symptom_patterns:

        if symptom in text:
            entities["symptoms"].append(symptom)

    # Medication
    medication_match = re.search(
        r"(amoxicillin|paracetamol|ibuprofen)\s*(\d+\s*mg)?",
        text,
        re.IGNORECASE
    )

    if medication_match:

        entities["medications"].append(
            medication_match.group(1)
        )

        if medication_match.group(2):
            entities["dosages"].append(
                medication_match.group(2)
            )

    # Duration
    duration_match = re.search(
        r"(\d+)\s*(day|days|week|weeks|month|months)",
        text,
        re.IGNORECASE
    )

    if duration_match:

        entities["duration"].append(
            duration_match.group(0)
        )

    # Pain score
    pain_match = re.search(
        r"(\d+)\s*(?:out of|/)\s*10",
        text,
        re.IGNORECASE
    )

    if pain_match:

        entities["pain_score"].append(
            pain_match.group(1) + "/10"
        )

    # Allergy
    if "allerg" in text:

        if "not sure" in text or "unknown" in text:
            entities["allergies"].append(
                "Allergy history unclear"
            )

        elif "no" in text:
            entities["allergies"].append(
                "No known allergy reported"
            )

    # Surgical history
    if "no previous surgeries" in text:
        entities["surgical_history"].append(
            "No previous surgeries"
        )

    return entities
