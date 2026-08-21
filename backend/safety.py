def generate_safety_alerts(
    transcript,
    entities
):

    alerts = []

    # Allergy check
    if not entities["allergies"]:

        alerts.append({
            "level": "warning",
            "message": "Allergy history was not documented."
        })

    elif "unclear" in entities["allergies"][0].lower():

        alerts.append({
            "level": "warning",
            "message": "Allergy history is unclear. Verify with patient."
        })

    # Medication check
    if entities["medications"]:

        alerts.append({
            "level": "info",
            "message": "Medication detected. Verify drug, dose and frequency."
        })

    # Symptom check
    if entities["symptoms"]:

        alerts.append({
            "level": "info",
            "message": "Clinical symptom detected. Review assessment."
        })

    if not alerts:

        alerts.append({
            "level": "success",
            "message": "No prototype safety alerts detected."
        })

    return alerts
