# schemas/llm_models.py
from pydantic import BaseModel


class LLMModelBase(BaseModel):
    model_name: str
    developer_id: int


class LLMModelCreate(LLMModelBase):
    pass


class LLMModel(LLMModelBase):
    model_id: int

    class Config:
        orm_mode = True