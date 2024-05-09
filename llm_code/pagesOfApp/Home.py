import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
import asyncio
import sys

sys.path.append('..')
sys.path.append('../..')
sys.path.append('../../..')
sys.path.append('../../../..')
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from style.style import configure_streamlit_theme

st.set_page_config(initial_sidebar_state = "collapsed")
def home():
    # Define colors
    background_color = "#f0f0f0"
    title_color = "#ff69b4"
    text_color = "#800080"

    st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)
    st.image('logo/logo2.png', width=150)
    st.title('Welcome to LLM Evaluator')
    st.write('This app helps you evaluate your LLM (Language Model) based on various criteria.')

    # Create a row for the buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Login", key="login_button"):
            switch_page("login")

    with col2:
        if st.button("Signup", key="signup_button"):
            switch_page("signup")
    with col3:
        if st.button("About the app", key="about_button"):
            switch_page("aboutApp")


home()