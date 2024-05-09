import logging
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError
import asyncio
import sys

from llm_code.app.api.models import metric_result
from llm_code.schemas.metric_result_schema import MetricResultSchema

sys.path.append('../..')
from llm_code.app.api.models.analysis_results import analysis_results
from llm_code.app.core.config.db import con
from llm_code.schemas.analysis_result import Analysis_Result, AggRequest, AggResponse
from sqlalchemy import Table, Column, Integer, Text, String, DateTime, ForeignKey, select, func

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)


# @app.post("/api/analysis_result", response_model=Analysis_Result)
# async def create_analysis_result(analysis_result_input: dict):
#     try:
#         prompt = analysis_result_input.get("prompt")
#         response = analysis_result_input.get("response")
#         metric_name = analysis_result_input.get("metric_name")
#         metric_value = analysis_result_input.get("metric_value")
#         model_name = analysis_result_input.get("model_name")
#
#         if prompt and response and metric_name and metric_value and model_name:
#             # Insert data into the database
#             data = con.execute(analysis_results.insert().values(
#                 prompt=prompt,
#                 response=response,
#                 metric_name=metric_name,
#                 metric_value=metric_value,
#                 model_name=model_name
#             ))
#             con.commit()  # Commit the transaction after insertion
#
#             # Check if insertion was successful
#             if data.rowcount == 1:
#                 # Return a response with the inserted analysis result details
#                 return {
#                     "result_id": data.inserted_primary_key[0],
#                     "prompt": prompt,
#                     "response": response,
#                     "metric_name": metric_name,
#                     "metric_value": metric_value,
#                     "model_name": model_name,
#                     "success": True,
#                     "msg": "Analysis result stored successfully"
#                 }
#             else:
#                 # If insertion failed, return an error response
#                 raise HTTPException(status_code=500, detail="Failed to store analysis result")
#         else:
#             raise HTTPException(status_code=400, detail="Missing required fields in request body")
#     except SQLAlchemyError as e:
#         # Log the error message
#         logging.error(f"Error storing analysis result: {e}")
#         # Return an error response
#         raise HTTPException(status_code=500, detail="Internal server error")
#

@app.post("/api/analysis_result", response_model=List[AggResponse])
async def get_analysis_results(agg_request: AggRequest):
    try:
        stmt = (
            select(
                metric_result.metric_result.c.model_id,
                metric_result.metric_result.c.metric_name,
                func.avg(metric_result.metric_result.c.metric_value).label('average'),
                func.max(metric_result.metric_result.c.metric_value).label('maximum'),
                func.min(metric_result.metric_result.c.metric_value).label('minimum'),
                func.sum(metric_result.metric_result.c.metric_value).label('total'),
                func.count(metric_result.metric_result.c.metric_value).label('count')
            ).
                where(
                (metric_result.metric_result.c.model_id.in_(agg_request.model_ids)) &
                (metric_result.metric_result.c.metric_name.in_(agg_request.metrics_name))
            ).
                group_by(metric_result.metric_result.c.model_id,
                         metric_result.metric_result.c.metric_name)
        )
        result = con.execute(stmt)

        rows = result.fetchall()
        response_list = []
        for row in rows:
            response_list.append(AggResponse(
                model_id=row.model_id,
                metric_name=row.metric_name,
                average=row.average,
                maximum=row.maximum,
                minimum=row.minimum,
                total=row.total,
                count=row.count
            ))
        return response_list

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/insert_metric_result")
async def insert_metric(metric_result_schema: MetricResultSchema):
    try:
        # Execute the insertion query
        data = con.execute(metric_result.metric_result.insert().values(
            username=metric_result_schema.username,
            metric_name=metric_result_schema.metric_name,
            prompt=metric_result_schema.prompt,
            prompt_generation=metric_result_schema.prompt_generation,
            metric_value=metric_result_schema.metric_value,
            model_id=metric_result_schema.model_id
        ))

        # Commit the transaction after insertion
        con.commit()

        # Check if the insertion was successful
        if data.rowcount == 1:
            # Return a response with the inserted user details
            return {
                "success": True,
                "msg": "Metric created successfully"
            }
        else:
            # If insertion failed, raise an error response
            raise HTTPException(status_code=500, detail="Failed to create metric")
    except SQLAlchemyError as e:
        # Log the error message
        logging.error(f"Error creating Metric: {e}")
        # Return an error response
        raise HTTPException(status_code=500, detail="Internal server error")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
