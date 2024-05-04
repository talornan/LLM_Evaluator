import asyncio
import logging
import re
import sys

import streamlit as st
from sqlalchemy.orm import sessionmaker

from llm_code.app.api.models.users import users
from llm_code.app.core.config.db import engine

sys.path.append('../..')

from llm_code.schemas.user import User
from llm_code.app.api.endpoints.UsersApi import create_user
from llm_code.pagesOfApp.style.style import configure_streamlit_theme

from llm_code.pagesOfApp.style.style import configure_streamlit_theme
from llm_code.pagesOfApp.authentication import AuthenticationManager

st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)

# Initialize AuthenticationManager
auth_manager = AuthenticationManager()


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
    username = st.text_input("Username", placeholder="Enter your username")
    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
    user_type = st.selectbox("User Type", ["prompt_engineer", "model_developer"])

    # Signup button
    if st.button("Sign Up"):
        # Perform validation checks
        user_data = {
            "username": username,
            "email": email,
            "password": password,
            "user_type": user_type
        }
        result = auth_manager.register_user(user_data)
        st.write(result)  # Display result message

        # Button to navigate to login page
        # Create a row for the buttons
        col1, col2 = st.columns(2)

        with col1:
            st.page_link("Home.py", label="home", icon="🏠")

        with col2:
            st.page_link("pages/login.py", label="login", icon=None)
    else:
        st.page_link("Home.py", label="home", icon="🏠")


signup()
