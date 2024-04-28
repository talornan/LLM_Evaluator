import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
import asyncio
import sys

sys.path.append('..')


# Define homepage function
def home():
    # Define colors
    background_color = "#f0f0f0"  # Light gray
    title_color = "#ff69b4"  # Pink
    text_color = "#800080"  # Purple

    # Set Streamlit theme colors
    st.markdown(
        f"""
        <style>
        /* Streamlit app background */
        body {{
            background-color: {background_color};
        }}
        /* Streamlit app title */
        .stApp {{
            color: {title_color};
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        /* Streamlit text */
        .stText, .stMarkdown {{
            color: {text_color};
            font-size: 18px;
        }}
        /* Button styling */
        .button {{
            background-color: #ff69b4; /* Pink */
            color: #fff; /* White */
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
            margin-right: 20px;
        }}
        .button:hover {{
            background-color: #9370DB; /* Purple */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Welcome to LLM Evaluator')
    st.write('This app helps you evaluate your LLM (Language Model) based on various criteria.')

    # Create a row for the buttons
    col1, col2 = st.columns(2)

    # Add buttons to the columns with custom CSS
    with col1:
        if st.button("Login", key="login_button"):
            switch_page("login")

    with col2:
        if st.button("Signup", key="signup_button"):
            switch_page("signup")


home()
