# Functions to operate on the Cart data in the database

from backend.repositories.db import get_db
from backend.models.cart import Cart, CartItem

# Spencer
def initializeCart(email):
    with get_db() as dbConnection:

        cursor = dbConnection.cursor()
        cursor.execute("INSERT INTO carts (email) VALUES (?)",(email,))

    # Create an empty cart row in the database assigned to the user's email
    return True

# Spencer
def getByEmail(email):

    # Check the cart table in the database for a row with a matching email,
    # then copy the data into a Cart object.
    with get_db() as dbConnection:
        cursor = dbConnection.cursor()
        cursor.execute("SELECT * FROM carts WHERE email = ?",(email,))

        row = cursor.fetchone()

        if not row:
            return False
        
        if row is None:
            return None

        id = row[0]
        cursor.execute("SELECT * FROM cart_items WHERE id = ?", (id,))

        item_rows = cursor.fetchall()

        cart_items = []
        
        for item_row in item_rows:
            item = CartItem(
                id = item_row[0],
                product_id = item_row[2],
                quantity = item_row[3]
                )
            cart_items.append(item)

        return Cart(row[0], row[1], cart_items)
    
# Prashant
def updateCart(cartId, cart):

    # Find the row in the cart table with the specified cartId and insert the Data
    # from the passed Cart object

    return bool

# Spencer
def deleteCart(cartId):
    # Find the row in the cart table with the specified cartId and delete the row
    with get_db() as dbConnection:
        cursor = dbConnection.cursor()
        cursor.execute("DELETE FROM carts WHERE cart_id = ?", (cartId,))

    return cursor.rowcount > 0