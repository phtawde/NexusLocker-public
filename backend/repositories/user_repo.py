# Functions to operate on the User data in the database

from backend.repositories.db import get_db
from backend.models.user import User

def getByEmail(email):
    # Search User table and make a User object from the row that matches the email

    with get_db() as dbConnection:
        cursor = dbConnection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?",(email,))
        
        row = cursor.fetchone()
        
    if row is None: 
        return None
    
    user = User(
            email = row[0],
            firstName = row[1],
            lastName = row[2],
            isAdmin = row[3],
            passwordHash = row[4]
        )

    return user


def addUser(user):

    # Turn a User object into a row in the User table

    attributes = user.getAttributes()
    attributes.append(user.getPasswordHash())

    with get_db() as dbConnection:
        cursor = dbConnection.cursor()
        cursor.execute(
            """
            INSERT INTO users (
                email,
                first_name,
                last_name,
                is_admin,
                password_hash
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            tuple(attributes),
        )

    return True