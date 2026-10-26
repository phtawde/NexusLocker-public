import sqlite3

def initialize():

    # Create Database File

    conn = sqlite3.connect("database/nexuslocker.db")

    with open("database/schema.sql") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize()