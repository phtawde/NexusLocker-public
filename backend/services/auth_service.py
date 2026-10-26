# User-related service functions to bridge api functions to database functions

from backend.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from backend.repositories.user_repo import addUser, getByEmail

def register(email, firstName, lastName, password):

    # Route register api data to repo table function

    fields = (email, firstName, lastName, password)

    if not all(isinstance(value, str) for value in fields):
        raise ValueError("All fields must be provided as strings.")

    email = email.strip().lower()
    firstName = firstName.strip()
    lastName = lastName.strip()

    if not all((email, firstName, lastName, password)):
        raise ValueError("All fields are required.")

    if getByEmail(email) is not None:
        raise ValueError("Email is already registered.")

    # Convert plaintext password to hashed password

    passwordHash = generate_password_hash(password)
    newUser = User(email, firstName, lastName, False, passwordHash)

    return addUser(newUser)


def login(email, password):

    # Check if entered password matches the hash stored in the database

    if not isinstance(email, str) or not isinstance(password, str):
        return None

    email = email.strip().lower()

    if not email or not password:
        return None

    user = getByEmail(email)

    if user is None:
        return None

    verified = check_password_hash(user.getPasswordHash(), password)

    if verified:
        return email

    return None