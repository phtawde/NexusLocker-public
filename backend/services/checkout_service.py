# Checkout-related service functions to bridge api functions to database functions,
# ensuring the front-facing routes never touch the database

from backend.repositories.cart_repo import getByEmail, updateCart
from backend.repositories.order_repo import addOrder, getById, updateOrderDb
from backend.models.cart import Cart
from backend.models.order import Order

def validateCart(Cart):

    # Check cart to validate items, stock and prices
    
    # Checks: Cart contains items; every quantity is valid;
    # every product still exists; enough stock remains; 
    # totals use current database prices.

    return bool


def checkout(email):

    # Get user's cart and checkout out using validateCart and repo functions

    # Checks: User is authenticated by the route; load their cart; validate it;
    # create order, reduce stock, and clear cart within one transaction.

    return bool


def addToCart(product, amount, userId):

    # Get user's cart, add the amount of the specified product to the Cart object,
    # validate the Cart and update the user's Cart in the database

    # Checks: Quantity is a positive integer; product exists;
    # combined cart quantity does not exceed stock.

    return bool