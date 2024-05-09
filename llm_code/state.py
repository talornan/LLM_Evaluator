
import streamlit as st

st.session_state["is_connected"] =False



def state_connect(username):
    st.session_state["is_connected"] = True
    st.session_state["username"] = username

def state_disconnect():
    st.session_state["is_connected"] = False
    st.session_state["username"] = None

def get_user_name():
    return st.session_state["username"]