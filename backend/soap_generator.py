def generate_soap_note(
    transcript,
    speakers,
    entities
):

    symptoms = ", ".join(
        entities["symptoms"]
    ) or "Not documented"

    duration = ", ".join(
        entities["duration"]
    ) or "Not documented"

    medications = ", ".join(
        entities["medications"]
    ) or "Not documented"

    dosages = ", ".join(
        entities["dosages"]
    ) or "Not documented"

    pain_score = ", ".join(
        entities["pain_score"]
    ) or "Not documented"

    allergies = ", ".join(
        entities["allergies"]
    ) or "Not documented"

    surgery = ", ".join(
        entities["surgical_history"]
    ) or "Not documented"

    subjective = (
        f"Patient reports {symptoms} "
        f"for {duration}. "
        f"Reported pain severity: {pain_score}."
    )

    objective = (
        f"Medication reported: {medications}. "
        f"Dosage: {dosages}. "
        f"Surgical history: {surgery}. "
        f"Allergy information: {allergies}."
    )

    assessment = (
        "Clinical assessment requires "
        "review and confirmation by the clinician."
    )

    plan = (
        "Clinician to verify history, "
        "allergies, examination findings and "
        "treatment plan before signing."
    )

    return {
        "subjective": subjective,
        "objective": objective,
        "assessment": assessment,
        "plan": plan,
        "coding": {
            "icd10": "Review required",
            "cpt": "Review required",
            "confidence": "Prototype"
        }
    }
