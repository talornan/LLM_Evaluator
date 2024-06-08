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

# hide the sidebar
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

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
            state.state_connect(username)
            st.success("Login successful!")
            st.balloons()
            if state.is_connected():
                st.markdown('<div class="welcome-message">Hello ' + state.get_user_name() + '</div>',
                            unsafe_allow_html=True)
            # Check user type and switch to the appropriate page
            if auth_manager.logged_in_user.user_type == "prompt_engineer":
                st.page_link("pages/LLMS_Analysis.py", label="TO LLMS Analysis Click Here", icon="📊")
            elif auth_manager.logged_in_user.user_type == "model_developer":
                st.page_link("pages/LLMS_agg_Analysis.py", label=" TO LLMS agg Analysis Click Here ", icon="📊")
            else:
                st.error("Unknown user type.")
        else:
            st.error(login_result)

    else:
        st.page_link("Home.py", label="home", icon="🏠")


def logout():
    if state.is_connected():
        if st.button("Logout"):
            auth_manager.logout()
            state.state_disconnect()
            st.experimental_rerun()
    else:
        st.write("Not logged in")


if state.is_connected():
    st.markdown('<div class="welcome-message">Hello ' + state.get_user_name() + '</div>', unsafe_allow_html=True)
    # if auth_manager.logged_in_user.user_type == "prompt_engineer":
    #     st.page_link("pages/LLMS_Analysis.py", label="TO LLMS Analysis Click Here", icon="📊")
    # elif auth_manager.logged_in_user.user_type == "model_developer":
    #     st.page_link("pages/LLMS_agg_Analysis.py", label=" TO LLMS agg Analysis Click Here ", icon="📊")
    # else:
    #     st.page_link("Home.py", label="home", icon="🏠")

    logout()
else:
    login()
