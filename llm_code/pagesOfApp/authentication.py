import re

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
import streamlit as st
import sys



sys.path.append('../..')
from llm_code import state
from llm_code.pagesOfApp.style.style import configure_streamlit_theme
from llm_code.app.api.models.users import users
from llm_code.app.core.config.db import engine
from llm_code.schemas.user import User

# Create a session
Session = sessionmaker(bind=engine)


class UserSessionManager:
    def __init__(self):
        self.session = Session()

    def is_email_in_use(self, email):
        # Query the database to check if the email exists
        return self.session.query(users).filter(users.c.email == email).first() is not None

    def is_username_in_use(self, username):
        # Query the database to check if the username exists
        return self.session.query(users).filter(users.c.username == username).first() is not None

    # Function to validate email format
    @staticmethod
    def validate_email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False

    # Function to check password strength
    @staticmethod
    def check_password_strength(password):
        # Add your password strength criteria here
        if len(password) < 8:
            return False
        return True


class AuthenticationManager:
    def __init__(self):
        self.user_session_manager = UserSessionManager()
        self.logged_in_user = None

    def login(self, username, password):
        # Check if the user is already logged in
        if self.logged_in_user:
            return "User is already logged in"

        try:
            # Query the database for the user with the provided username
            user = self.user_session_manager.session.query(users).filter_by(username=username).first()

            if user:
                # If the user exists, check if the password matches
                if user.password == password:
                    self.logged_in_user = user
                    return "Login successful"
                else:
                    return "Invalid username or password"
            else:
                return "User does not exist"
        except SQLAlchemyError as e:
            return "An error occurred while processing your request. Please try again later."

    def logout(self):
        # Check if the user is logged in
        if self.logged_in_user:
            self.logged_in_user = None
            st.experimental_rerun()
            return "Logout successful"
        else:
            return "No user is currently logged in"

    def register_user(self, user_data):
        try:
            # Extract username, email, password, and confirm_password from user_data
            username = user_data.get("username")
            email = user_data.get("email")
            password = user_data.get("password")
            confirm_password = user_data.get("confirm_password")
            user_type = user_data.get("user_type")

            print("user_name" + username)
            print("email" + email)
            print("password" + username)
            print("confirm_password" + confirm_password)

            # Check if username or email already exists
            if self.user_session_manager.is_username_in_use(username):
                return "Username already in use. Please choose a different one."
            if self.user_session_manager.is_email_in_use(email):
                return "Email already in use. Please use a different one."

            # Validate email format
            if not self.user_session_manager.validate_email(email):
                return "Invalid email format. Please enter a valid email."

            # Check password strength
            if not self.user_session_manager.check_password_strength(password):
                return "Password must be at least 8 characters long."

            # Check if password and confirm password match
            if password != confirm_password:
                print(password)
                print(confirm_password)
                return "Password and confirm password do not match. Please re-enter."

            # Add user to database
            import requests
            user = User(username=username, password=password, user_type=user_type, email=email)

            requests.post("http://localhost:8000/api/user", json=user.dict())

            state.state_connect(username)

            return "User registered successfully"
        except SQLAlchemyError as e:
            return f"Error registering user: {e}"
