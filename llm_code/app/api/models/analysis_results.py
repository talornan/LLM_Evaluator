from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from llm_code.app.core.config.db import meta

analysis_results = Table(
    'AnalysisResults', meta,
    Column('result_id', Integer, primary_key=True),
    Column('response_id', Integer, ForeignKey('LLMResponses.response_id'), nullable=False),
    Column('metric_name', String(100), nullable=False),
    Column('metric_value', Float, nullable=False)
)