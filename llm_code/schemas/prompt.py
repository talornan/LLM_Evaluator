# schemas/prompts.py
from pydantic import BaseModel


class Prompt(BaseModel):
    prompt_id: int
    prompt_text: str
