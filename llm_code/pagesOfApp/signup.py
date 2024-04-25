import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
import logging
import re  # Import regular expression module for email validation
import asyncio
import sys

sys.path.append('..')

from llm_code.app.api.models.users import users
from llm_code.schemas.user import User
from llm_code.pagesOfApp.login import login  # Import the login function
from llm_code.app.core.config.db import engine, meta
from llm_code.app.api.endpoints.UsersApi import create_user, get_users

# Set Streamlit theme colors
st.markdown(
    """
    <style>
    /* Streamlit app background */
    body {
        background-color: #87cefa; /* light blue */
    }
    /* Streamlit text color */
    .stTextInput>div>div>input {
        color: #800080; /* purple */
    }
    /* Streamlit button */
    .stButton>button {
        background-color: #ff69b4; /* pink */
        color: #fff; /* white */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Function to validate email format
def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


# Function to check password strength
def check_password_strength(password):
    # Add your password strength criteria here
    if len(password) < 8:
        return False
    return True


# Define the add_user function as asynchronous
async def add_user_async(username, email, password, user_type):
    try:
        user_data = {
            "username": username,
            "email": email,
            "password": password,
            "user_type": user_type
        }
        # Use await to asynchronously send the POST request
        response = await create_user(User(**user_data))
        if response.get("success"):
            st.success("User added successfully!")
        else:
            st.error("Failed to add user. Please try again later.")

    except Exception as e:
        st.error(f"Error adding user: {e}")
        logging.error(f"Error adding user: {e}")


# Define a helper function to run the add_user_async function
def add_user(username, email, password, user_type):
    asyncio.run(add_user_async(username, email, password, user_type))


def signup():
    st.title("Signup")

    # Collect user input
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    user_type = st.selectbox("User Type", ["prompt_engineer", "model_developer"])

    # Signup button
    if st.button("Sign Up"):
        # Perform validation checks
        if not validate_email(email):
            st.error("Invalid email format. Please enter a valid email address.")
        elif not check_password_strength(password):
            st.error("Password should be at least 8 characters long.")
        else:
            # Run the add_user function asynchronously
            add_user(username, email, password, user_type)


signup()