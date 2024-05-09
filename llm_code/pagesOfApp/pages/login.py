import streamlit as st
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy.exc import SQLAlchemyError

import sys

from sqlalchemy.sql.functions import user

from llm_code import state

sys.path.append('../..')
# Import necessary modules from your project
from llm_code.app.api.models.users import users  # Assuming users model is imported correctly
from llm_code.app.core.config.db import engine
from llm_code.pagesOfApp.style.style import configure_streamlit_theme
from llm_code.pagesOfApp.authentication import AuthenticationManager

st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)
auth_manager = AuthenticationManager()


def login():
    st.title("Login")

    # Collect login information from the user
    username = st.text_input("Username", placeholder="Enter your username", max_chars=20)
    password = st.text_input("Password", type="password", placeholder="Enter your password", max_chars=50)

    if st.button("Login"):
        # Call the login method of AuthenticationManager
        login_result = auth_manager.login(username, password)

        if login_result == "Login successful":
            st.sidebar.write(f"Hello, {username}!")
            state.state_connect(username)
            st.success("Login successful!")
            st.balloons()
            st.write(f"Welcome, {username}!")
            # Check user type and switch to the appropriate page
            if auth_manager.logged_in_user.user_type == "prompt_engineer":
                st.page_link("pages/LLMS_Analysis.py", label="LLMS_Analysis", icon="📊")
            elif auth_manager.logged_in_user.user_type == "model_developer":
                st.page_link("pages/LLMS_agg_Analysis.py", label="LLMS_agg_Analysis", icon=None)
            else:
                st.error("Unknown user type.")
        else:
            st.error(login_result)

    else:
        st.page_link("Home.py", label="home", icon="🏠")


def logout():
    # Call the logout method of AuthenticationManager
    logout_result = auth_manager.logout()

    if logout_result == "Logout successful":
        st.sidebar.write("Logout successful")
    else:
        st.error(logout_result)


# Check if the user is logged in
if auth_manager.logged_in_user:
    st.sidebar.write(f"Hello, {auth_manager.logged_in_user.username}!")
    if st.sidebar.button("Logout"):
        logout()
else:
    login()