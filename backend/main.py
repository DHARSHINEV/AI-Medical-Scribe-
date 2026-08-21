from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .transcription import get_sample_transcript, diarize_transcript
from .clinical_nlp import extract_entities
from .soap_generator import generate_soap_note
from .safety import generate_safety_alerts


app = FastAPI(
    title="AI Medical Scribe",
    description="Ambient clinical documentation prototype",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TranscriptRequest(BaseModel):
    transcript: str


@app.get("/api/health")
def health():
    return {
        "status": "online",
        "service": "AI Medical Scribe"
    }


@app.get("/api/demo")
def demo():

    transcript = get_sample_transcript()

    speakers = diarize_transcript(transcript)

    entities = extract_entities(transcript)

    soap = generate_soap_note(
        transcript,
        speakers,
        entities
    )

    alerts = generate_safety_alerts(
        transcript,
        entities
    )

    return {
        "transcript": transcript,
        "speakers": speakers,
        "entities": entities,
        "soap": soap,
        "alerts": alerts
    }


@app.post("/api/analyze")
def analyze(request: TranscriptRequest):

    transcript = request.transcript.strip()

    if not transcript:
        return {
            "error": "Transcript cannot be empty"
        }

    speakers = diarize_transcript(transcript)

    entities = extract_entities(transcript)

    soap = generate_soap_note(
        transcript,
        speakers,
        entities
    )

    alerts = generate_safety_alerts(
        transcript,
        entities
    )

    return {
        "transcript": transcript,
        "speakers": speakers,
        "entities": entities,
        "soap": soap,
        "alerts": alerts
    }


# Serve frontend
app.mount(
    "/",
    StaticFiles(
        directory="frontend",
        html=True
    ),
    name="frontend"
)
