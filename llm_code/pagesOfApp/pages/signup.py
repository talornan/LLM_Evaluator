import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging
import re  # Import regular expression module for email validation
import asyncio
import sys
import sqlite3

from llm_code.app.core.config.db import engine

sys.path.append('../..')

from llm_code.schemas.user import User
from llm_code.app.api.endpoints.UsersApi import create_user
from llm_code.pagesOfApp.style.style import configure_streamlit_theme

st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def is_email_in_use(email):
    # Create a session

    # Query the database to check if the email exists
    user = session.query(User).filter(User.email == email).first()

    # Close the session
    session.close()

    # If user is not None, email is in use
    return user is not None


def is_username_in_use(username):
    # Create a session

    # Query the database to check if the username exists
    user = session.query(User).filter(User.username == username).first()

    # Close the session
    session.close()

    # If user is not None, username is in use
    return user is not None

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
    username = st.text_input("Username", placeholder="Enter your username")
    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
    user_type = st.selectbox("User Type", ["prompt_engineer", "model_developer"])

    # Signup button
    if st.button("Sign Up"):
        # Perform validation checks
        if not validate_email(email):
            st.error("Invalid email format. Please enter a valid email address.")
        elif not check_password_strength(password):
            st.error("Password should be at least 8 characters long.")
        elif is_email_in_use(email):
            st.error("Email is already in use. Please choose a different email address.")
        elif is_username_in_use(username):
            st.error("Username is already in use. Please choose a different username.")
        else:
            add_user(username, email, password, user_type)
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
