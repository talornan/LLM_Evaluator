import streamlit as st

# Import login and signup functions
from llm_code.pagesOfApp.login import login
from llm_code.pagesOfApp.signup import signup


# Define homepage function
def home():
    st.title('Welcome to LLM Evaluator')
    st.write('This app helps you evaluate your LLM (Language Model) based on various criteria.')


home()
