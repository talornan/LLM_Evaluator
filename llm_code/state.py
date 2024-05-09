
import streamlit as st

st.session_state["is_connected"] =False



def state_connect(username):
    st.session_state["is_connected"] = True
    st.session_state["username"] = username

def is_connected():
    if 'is_connected' in st.session_state:
        return st.session_state["is_connected"]
    return False



def state_disconnect():
    st.session_state["is_connected"] = False
    st.session_state["username"] = None

def get_user_name():
    return st.session_state["username"]