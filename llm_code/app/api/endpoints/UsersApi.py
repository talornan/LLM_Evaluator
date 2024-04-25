import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from sqlalchemy import Table, Column, Integer, String, Enum
from llm_code.app.api.models.users import users
from llm_code.app.core.config.db import con
from llm_code.schemas.user import User
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.post("/api/user", response_model=User)
async def create_user(user_input: User):
    try:

        # Insert user data into the database
        data = con.execute(users.insert().values(
            username=user_input.username,
            password=user_input.password,
            user_type=user_input.user_type,
            email=user_input.email
        ))
        con.commit()  # Commit the transaction after insertion

        # Check if insertion was successful
        if data.rowcount == 1:
            # Return a response with the inserted user details
            return {
                "user_id": data.inserted_primary_key[0],
                "username": user_input.username,
                "password": user_input.password,
                "user_type": user_input.user_type,
                "success": True,
                "msg": "User created successfully"
            }
        else:
            # If insertion failed, raise an error response
            raise HTTPException(status_code=500, detail="Failed to create user")
    except SQLAlchemyError as e:
        # Log the error message
        logging.error(f"Error creating user: {e}")
        # Return an error response
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/api/user")
async def get_users():
    try:
        # Create a select statement for all columns from the 'Users' table
        query = select(users)

        # Execute the query
        result = con.execute(query)

        # Fetch all rows from the result
        rows = result.fetchall()

        # Convert rows to a list of dictionaries
        users_list = []
        for row in rows:
            user_dict = dict(row)
            users_list.append(user_dict)

        return users_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
