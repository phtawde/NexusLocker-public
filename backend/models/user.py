# User class

class User:
    def __init__(self, email, firstName, lastName, isAdmin, passwordHash):
        self._email = email
        self._firstName = firstName
        self._lastName = lastName
        self._isAdmin = isAdmin
        self._passwordHash = passwordHash

    def getEmail(self):
        return self._email

    def getName(self):
        return [self._firstName, self._lastName]

    def checkAdmin(self):
        return self._isAdmin

    def getPasswordHash(self):
        return self._passwordHash

    def getAttributes(self):
        return [self._email, self._firstName,
                self._lastName, self._isAdmin]