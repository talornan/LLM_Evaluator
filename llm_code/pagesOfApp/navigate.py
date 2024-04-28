import streamlit as st
import sys

sys.path.append('..')
# Import login and signup functions
from streamlit_extras.switch_page_button import switch_page

login_page = st.button("login")
signup_page = st.button("signup")

if login_page:
    switch_page("login")
if signup_page:
    switch_page("signup")