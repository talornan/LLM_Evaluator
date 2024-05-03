import logging

import uvicorn
from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError
import asyncio
import sys

sys.path.append('../..')
from llm_code.app.api.models.analysis_results import analysis_results
from llm_code.app.core.config.db import con
from llm_code.schemas.analysis_result import Analysis_Result
from sqlalchemy import Table, Column, Integer, Text, String, DateTime, ForeignKey, select

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.post("/api/analysis_result", response_model=Analysis_Result)
async def create_analysis_result(analysis_result_input: dict):
    try:
        prompt = analysis_result_input.get("prompt")
        response = analysis_result_input.get("response")
        metric_name = analysis_result_input.get("metric_name")
        metric_value = analysis_result_input.get("metric_value")
        model_name = analysis_result_input.get("model_name")

        if prompt and response and metric_name and metric_value and model_name:
            # Insert data into the database
            data = con.execute(analysis_results.insert().values(
                prompt=prompt,
                response=response,
                metric_name=metric_name,
                metric_value=metric_value,
                model_name=model_name
            ))
            con.commit()  # Commit the transaction after insertion

            # Check if insertion was successful
            if data.rowcount == 1:
                # Return a response with the inserted analysis result details
                return {
                    "result_id": data.inserted_primary_key[0],
                    "prompt": prompt,
                    "response": response,
                    "metric_name": metric_name,
                    "metric_value": metric_value,
                    "model_name": model_name,
                    "success": True,
                    "msg": "Analysis result stored successfully"
                }
            else:
                # If insertion failed, return an error response
                raise HTTPException(status_code=500, detail="Failed to store analysis result")
        else:
            raise HTTPException(status_code=400, detail="Missing required fields in request body")
    except SQLAlchemyError as e:
        # Log the error message
        logging.error(f"Error storing analysis result: {e}")
        # Return an error response
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/api/analysis_result")
async def get_analysis_results():
    try:
        query = select(analysis_results)

        # Execute the query
        result = con.execute(query)

        # Fetch all rows from the result
        rows = result.fetchall()

        # Convert rows to a list of dictionaries
        analysis_results_list = []
        for row in rows:
            analysis_result_dict = {}
            for i, col in enumerate(analysis_results.columns):
                analysis_result_dict[col.name] = row[i]
            analysis_results_list.append(analysis_result_dict)

        return analysis_results_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
