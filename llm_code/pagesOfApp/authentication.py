import re
import bcrypt

# Dummy database to store registered users
registered_users = {}


def register(username, email, password):
    # Check if username or email already exists
    if username in registered_users:
        return False, "Username already exists. Please choose a different one."
    if email in [user['email'] for user in registered_users.values()]:
        return False, "Email already exists. Please use a different one."

    # Check if email is valid
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Invalid email address. Please enter a valid email."

    # Check if password is at least 6 characters long and contains uppercase, lowercase, and numbers
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    if not re.search(r"\d", password) or not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter, one lowercase letter, and one number."

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Store user information in the database
    registered_users[username] = {'email': email, 'password': hashed_password}
    return True, "Registration successful. You can now log in."


def authenticate(username, password):
    # Check if the username exists
    if username not in registered_users:
        return False, "User not found. Please check your username."

    # Verify the password
    stored_password = registered_users[username]['password']
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        return True, "Authentication successful. Welcome back, {}!".format(username)
    else:
        return False, "Incorrect password. Please try again."
