# AI Medical Scribe

An AI-powered ambient clinical assistant prototype that converts
doctor-patient conversations into structured clinical documentation.

## Features

- Doctor/patient speaker identification
- Clinical entity extraction
- SOAP note generation
- Safety/missing-information alerts
- ICD-10/CPT coding suggestions
- Clinician review workflow
- Simple web dashboard

## Architecture

Doctor + Patient Conversation
        ↓
Speaker Diarization
        ↓
Clinical NLP
        ↓
SOAP Note Generation
        ↓
Safety & Coding
        ↓
Clinician Review
        ↓
EHR/FHIR Integration (future scope)

## Technology

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- REST API
- Rule-based clinical NLP prototype

## Installation

Create a virtual environment:

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Linux/macOS:
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Run

From the project root:

uvicorn backend.main:app --reload

Open:

http://127.0.0.1:8000

## Important

This is a hackathon prototype and not a medical diagnostic system.
AI-generated information must be reviewed by a qualified clinician.

Do not upload real patient information, PHI, medical audio,
passwords or API keys to this repository.
