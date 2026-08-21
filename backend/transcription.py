def get_sample_transcript():

    return """
Doctor: What brings you in today?

Patient: I have had sharp lower abdominal pain
for about three days.

Doctor: How severe is the pain?

Patient: Around six out of ten.

Doctor: Are you currently taking any medication?

Patient: I am taking Amoxicillin 500 mg twice daily.

Doctor: Do you have any known drug allergies?

Patient: I am not sure.

Doctor: Have you had any previous surgeries?

Patient: No previous surgeries.
""".strip()


def diarize_transcript(transcript):

    lines = transcript.splitlines()

    result = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.lower().startswith("doctor:"):
            speaker = "Doctor"
            text = line.split(":", 1)[1].strip()

        elif line.lower().startswith("patient:"):
            speaker = "Patient"
            text = line.split(":", 1)[1].strip()

        else:
            speaker = "Unknown"
            text = line

        result.append({
            "speaker": speaker,
            "text": text
        })

    return result
