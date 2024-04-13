from pydantic import BaseModel


class AnalysisResultBase(BaseModel):
    metric_name: str
    metric_value: float


class AnalysisResultCreate(AnalysisResultBase):
    response_id: int


class AnalysisResult(AnalysisResultBase):
    result_id: int
    response_id: int

    class Config:
        orm_mode = True
