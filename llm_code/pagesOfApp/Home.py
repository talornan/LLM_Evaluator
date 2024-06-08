import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys
sys.path.append('..')
sys.path.append('../..')
sys.path.append('../../..')
sys.path.append('../../../..')
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from llm_code import state
from llm_code.pagesOfApp.authentication import AuthenticationManager
from llm_code.pagesOfApp.style.homeStyle import configure_home_theme

auth_manager = AuthenticationManager()


def home():
    st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

    # Apply custom style from homeStyle.py
    st.markdown(configure_home_theme(), unsafe_allow_html=True)

    if state.is_connected():
        st.markdown('<div class="welcome-message">Hello ' + state.get_user_name() + '</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="greeting-message">Hello guest</div>', unsafe_allow_html=True)

    # st.image('llm_code/logo/newlogo.jpeg', width=150)

    # Welcome message with applied styles
    st.markdown(
        """
        <div class="main-content">
            <h1>Welcome to the LLM Evaluator</h1>
            <p class="text-color-adjusted" style="font-size: 24px;">Unleash the power of language models and explore their potential with our interactive tool!</p>
            <p class="text-color-adjusted" style="font-size: 24px;">Discover insights, analyze performance, and dive deep into the world of natural language understanding.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Center-align all columns
    st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)

    # Create a container for the buttons
    with st.container():
        # Create a row for the buttons
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

        with col3:
            if st.button("Login", key="login_button"):
                switch_page("login")

        with col4:
            if st.button("Signup", key="signup_button"):
                switch_page("signup")

        with col5:
            if st.button("About the app", key="about_button"):
                switch_page("aboutApp")

    st.markdown('</div>', unsafe_allow_html=True)  # Close center-aligning container


home()
