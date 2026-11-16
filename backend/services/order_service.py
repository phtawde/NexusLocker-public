# Order-related service functions to bridge api functions to database functions,
# ensuring the front-facing routes never touch the database

from backend.repositories.cart_repo import getByCustomer, updateCart
from backend.repositories.order_repo import addOrder, getById, updateOrder
from backend.models.cart import Cart
from backend.models.order import Order


def updateOrder(orderId, Order):

    # Call updateOrderDb function in order_repo

    return bool


def deleteOrder(orderId):

    # Call deleteOrder function in order_repo 

    return bool


def getOrderById(orderId):

    # Call getById function in order_repo

    return Order


def getOrderByCustomer(email):

    # Call getByEmail function in order_repo

    return Order