# Functions to operate on the Product data in the database

from backend.repositories.db import get_db
from backend.models.product import Product
from backend.errors import ProductNotFoundError

def getAll():

    # Turn every product row in the table into a Product object and then return a list of those

    with get_db() as dbConnection:
        cursor = dbConnection.cursor()

        cursor.execute(
            "SELECT * FROM products"
        )
        rows = cursor.fetchall()

    products = []

    for row in rows:
        product = Product(
            id=row[0],
            name=row[1],
            description=row[2],
            category=row[3],
            price=row[4],
            stock=row[5],
            dateAdded=row[6]
        )

        products.append(product)

    return products


def getById(productId):

    # Create a product object from the row in the products table that matches the productId

    with get_db() as dbConnection:
        cursor = dbConnection.cursor()

        cursor.execute(
            "SELECT * FROM products WHERE product_id = ?",
            (productId,)
        )
        row = cursor.fetchone()

    if not row:
        raise ProductNotFoundError(productId)

    product = Product(
        id=row[0],
        name=row[1],
        description=row[2],
        category=row[3],
        price=row[4],
        stock=row[5],
        dateAdded=row[6])

    return product


def search(field, query):

    # Use SQLite "LIKE" operator to search for a query in the specified field

    with get_db() as dbConnection:
        cursor = dbConnection.cursor()

        cursor.execute(
            f"SELECT * FROM products WHERE {field} LIKE ?",
            (f"%{query}%",)
        )
        rows = cursor.fetchall()
    
    products = []
    for row in rows:
        product = Product(
        id=row[0],
        name=row[1],
        description=row[2],
        category=row[3],
        price=row[4],
        stock=row[5],
        dateAdded=row[6])

        products.append(product)
    return products