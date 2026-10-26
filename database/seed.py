import json
import sqlite3
from pathlib import Path
from werkzeug.security import generate_password_hash

DATABASE = "database/nexuslocker.db"
JSON_FILE = "database/products.json"

users = [
    (
        "tester.a@gmail.com",
        "Tester",
        "A",
        False,
        generate_password_hash("admin123")
    ),
    (
        "tester.b@gmail.com",
        "Tester",
        "B",
        False,
        generate_password_hash("admin123")
    )
]


def load_products():
    
    # Load products from JSON and map them to the database schema.

    with open(JSON_FILE, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    # Support a JSON list or an object containing a products list
    if isinstance(data, dict):
        data = data.get("products", [])

    products = []

    for product in data:
        products.append((
            product.get("productName", ""),
            product.get("description", ""),
            product.get("category", ""),
            product.get("price", 0),
            product.get("stock", 0),
            product.get("dateAdded") or "2026-10-01 09:00:00"
        ))

    return products


def seed_products(cursor):

    # Insert products from JSON into the products table.

    products = load_products()

    cursor.executemany(
        """
        INSERT INTO products (
            name,
            description,
            category,
            price,
            stock,
            date_added
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        products
    )

    print(f"Inserted {len(products)} products from JSON.")


def seed_users(cursor):

    # Insert sample users without duplicating existing email addresses.

    cursor.executemany(
        """
        INSERT OR IGNORE INTO users (
            email,
            first_name,
            last_name,
            is_admin,
            password_hash
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        users
    )

    print("Users seeded successfully.")


def main():
    Path(DATABASE).parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DATABASE)

    try:
        cursor = conn.cursor()

        seed_products(cursor)
        seed_users(cursor)

        conn.commit()
        print("Database seeding complete!")

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    main()