from pydantic import BaseModel, Field
from typing import Optional, List

class GenerateRequest(BaseModel):
    seed_idea: str = Field(..., description="The core concept for the story")
    genre: str = Field(..., description="Target genre of the script")
    tone: str = Field(..., description="Emotional tone of the script")
    target_audience: Optional[str] = "General"

class PitchResponse(BaseModel):
    logline: str
    concept: str
    executive_pitch: str
    estimated_budget: str

class ScriptResponse(BaseModel):
    scene_heading: str
    action_lines: List[str]
    dialogue: List[dict]
    full_script_markdown: str
