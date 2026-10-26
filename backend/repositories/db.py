# DB connection contructor

import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATABASE_PATH = PROJECT_ROOT / "database" / "nexuslocker.db"


def get_db():
    return sqlite3.connect(DATABASE_PATH)