# Functions to operate on the Order data in the database

from backend.repositories.db import get_db
from backend.models.order import Order
from backend.errors import OrderNotFoundError


def addOrder(Cart):

    # Insert the passed Cart object's data into a new row in the order table
    
    return bool

# Seth
def getById(orderId):

    # Check the order table in the database for a row with a matching orderId,
    with get_db() as dbConnection:
        cursor = dbConnection.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id = ?", (orderId,))
        row = cursor.fetchone()

    if not row:
        raise OrderNotFoundError(orderId)

    # then copy the data into an Order object.
    order = Order(
        order_id=row[0],
        user_email=row[1],
        date_placed=row[2],
        order_status=row[3],
        subtotal=row[4],
    )

    return order

# Seth
def getByEmail(email):

    # Check the order table in the database for a row with a matching email.

    with get_db() as dbConnection:
        cursor = dbConnection.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_email = ?", (email,))
        rows = cursor.fetchall()

    orders = []

    for row in rows:
        order = Order(
            order_id=row[0],
            user_email=row[1],
            date_placed=row[2],
            order_status=row[3],
            subtotal=row[4],
        )

        orders.append(order)

    return orders

# Jose
def updateOrderDb(orderId, order):

    with get_db() as dbConnection:
        cursor = dbConnection.cursor()
        cursor.execute(
            """
            UPDATE orders
            SET user_email = ?, date_placed = ?, order_status = ?, subtotal = ?
            WHERE order_id = ?
            """,
            (
                order.user_email,
                order.date_placed,
                order.order_status,
                order.subtotal,
                orderId,
            ),
        )

        return cursor.rowcount == 1


# Jose
def deleteOrderDb(orderId):

    with get_db() as dbConnection:
        cursor = dbConnection.cursor()
        cursor.execute(
            "DELETE FROM orders WHERE order_id = ?",
            (orderId,),
        )

        return cursor.rowcount == 1