from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
import asyncio
import sys

sys.path.append('../..')
from llm_code.app.core.config.db import meta

analysis_results = Table(
    'AnalysisResults', meta,
    Column('prompt', String(100), primary_key=True),
    Column('response', String(800), nullable=False),
    Column('metric_name', String(100), nullable=False),
    Column('metric_value', String(100), nullable=False),
    Column('model_name', String(100), nullable=False)
)
