import logging

import uvicorn
from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError
import asyncio
import sys

sys.path.append('../..')
from llm_code.app.api.models.prompts import prompts
from llm_code.app.core.config.db import con
from llm_code.schemas.prompt import Prompt
from sqlalchemy import Table, Column, Integer, Text, String, DateTime, ForeignKey, select

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.post("/api/prompt", response_model=Prompt)
async def create_prompt(prompt_input: dict):
    try:
        prompt_text = prompt_input.get("prompt_text")
        if prompt_text:
            # Insert data into the database
            data = con.execute(prompts.insert().values(
                prompt_text=prompt_text,
            ))
            con.commit()  # Commit the transaction after insertion

            # Check if insertion was successful
            if data.rowcount == 1:
                # Return a response with the inserted prompt details
                return {
                    "prompt_id": data.inserted_primary_key[0],
                    "prompt_text": prompt_text,
                    "success": True,
                    "msg": "Prompt stored successfully"
                }
            else:
                # If insertion failed, return an error response
                raise HTTPException(status_code=500, detail="Failed to store prompt")
        else:
            raise HTTPException(status_code=400, detail="Missing prompt_text in request body")
    except SQLAlchemyError as e:
        # Log the error message
        logging.error(f"Error storing prompt: {e}")
        # Return an error response
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/api/prompt")
async def get_prompts():
    try:
        # Create a select statement for all columns from the 'prompts' table
        query = select(prompts)

        # Execute the query
        result = con.execute(query)

        # Fetch all rows from the result
        rows = result.fetchall()

        # Convert rows to a list of dictionaries
        prompts_list = []
        for row in rows:
            prompt_dict = {}
            for i, col in enumerate(prompts.columns):
                prompt_dict[col.name] = row[i]
            prompts_list.append(prompt_dict)

        return prompts_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
