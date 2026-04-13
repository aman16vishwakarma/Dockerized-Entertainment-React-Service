from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from .models import GenerateRequest, PitchResponse, ScriptResponse
from .ai_engine import AgenticPipeline
import time

app = FastAPI(
    title="Nomad Cosmic API",
    description="Agentic Entertainment Backend Services",
    version="0.1.0"
)

# Initialize our multi-agent engine
pipeline = AgenticPipeline()

@app.get("/")
async def health_check():
    return {"status": "healthy", "engines": "online"}

@app.post("/api/v1/generate-pitch", response_model=PitchResponse)
async def generate_pitch(req: GenerateRequest):
    """
    Endpoint for the Planner & Writer Agents to construct the logline and pitch.
    """
    try:
        # Currently migrating to asynchronous Groq/Gemini calls
        pitch_data = pipeline.run_pitch_generation(
            idea=req.seed_idea,
            genre=req.genre,
            tone=req.tone
        )
        return pitch_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/generate-script", response_model=ScriptResponse)
async def generate_script(req: GenerateRequest):
    """
    Endpoint for the Director Agent to draft the screenplay scene.
    """
    try:
        script_data = pipeline.run_script_generation(
            idea=req.seed_idea,
            genre=req.genre,
            tone=req.tone
        )
        return script_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
