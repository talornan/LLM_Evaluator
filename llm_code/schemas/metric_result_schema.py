from pydantic import BaseModel


class MetricResultSchema(BaseModel):
    username: str
    metric_name: str
    prompt: str
    prompt_generation: str
    metric_value: float
    model_id: str

