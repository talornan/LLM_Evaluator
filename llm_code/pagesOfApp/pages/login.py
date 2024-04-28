import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

import asyncio
import sys

sys.path.append('../..')
# Import necessary modules from your project
from llm_code.app.api.models.users import users  # Assuming users model is imported correctly
from llm_code.app.core.config.db import engine
from streamlit_extras.switch_page_button import switch_page

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Set Streamlit theme colors
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
        try:
            # Query the database for the user with the provided username
            user = session.query(users).filter_by(username=username).first()

            if user:
                # If the user exists, check if the password matches
                if user.password == password:
                    st.success("Login successful!")
                    st.balloons()
                    # Check user type and switch to the appropriate page
                    if user.user_type == "prompt_engineer":
                        st.page_link("pages/LLMS_Analysis.py", label="LLMS_Analysis", icon=None)
                    elif user.user_type == "model_developer":
                        st.page_link("pages/LLMS_agg_Analysis.py", label="LLMS_agg_Analysis", icon=None)
                    else:
                        st.error("Unknown user type.")
                else:
                    st.error("Invalid username or password. Please try again.")
            else:
                st.error("User does not exist. Please try again.")
        except SQLAlchemyError as e:
            st.error("An error occurred while processing your request. Please try again later.")
            st.write(e)


# Run the login function
login()
