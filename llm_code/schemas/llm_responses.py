# schemas/prompts.py
from pydantic import BaseModel


# schemas/llm_responses.py
class LLMResponseBase(BaseModel):
    response_text: str
    llm_model: str
    evaluation_metrics: dict


class LLMResponseCreate(LLMResponseBase):
    prompt_id: int


class LLMResponse(LLMResponseBase):
    response_id: int
    prompt_id: int

    class Config:
        orm_mode = True
