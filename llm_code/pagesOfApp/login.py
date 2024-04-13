import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import asyncio
import sys

sys.path.append('..')

from llm_code.app.api.models.users import users
from llm_code.schemas.user import User
from llm_code.app.core.config.db import engine,meta


Session = sessionmaker(bind=engine)
session = Session()

# Set the Streamlit theme colors directly
st.markdown(
    """
    <style>
    /* Streamlit app background */
    body {
        background-color: #87cefa;
    }
    /* Streamlit app title */
    .stApp {
        color: #ff69b4;
    }
    /* Streamlit button */
    .stButton>button {
        background-color: #800080;
        color: #fff;
    }
    /* Streamlit text */
    .stTextInput>div>div>input {
        color: #87cefa;
    }
    /* Streamlit selectbox */
    .st-af {
        color: #ff69b4;
    }
    .st-d4 {
        color: #800080;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def login():
    st.title("Login")

    # Collect login information from the user
    username = st.text_input("Username", placeholder="Enter your username", max_chars=20)
    password = st.text_input("Password", type="password", placeholder="Enter your password", max_chars=50)

    # Check if the user has submitted the form
    if st.button("Login"):
        # Authenticate the user
        user = session.query(User).filter_by(username=username, password=password).first()
        if user:
            st.success("Login successful!")
        else:
            st.error("Invalid username or password. Please try again.")


# Run the login function
login()
