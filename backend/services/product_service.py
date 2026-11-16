# Product-related service functions to bridge api functions to database functions,
# ensuring the front-facing routes never touch the database

from backend.repositories.product_repo import search, getAll, getById
from backend.errors import InvalidSearchFieldError

def searchProducts(field, query):

    # Validate search fields and call repo function "search"

    productColumns = ["product_id", "name", "description", "price", "stock", "dateAdded"]

    if field not in productColumns:
        raise InvalidSearchFieldError(field)
 
    return search(field, query)

def getProductById(productId):

    # Middle-man function so repo function "getById" isn't exposed directly

    product = getById(productId)

    return product

def getLatestProducts(count):

    # Sort product by add date and then get the first "count" from the product list

    if type(count) is not int:
        raise ValueError("Count must be an int.")

    if count < 1:
        raise ValueError("Count must be more than 0.")

    products = getAll()

    products.sort(
        key=lambda product: product.getDateAdded(), reverse=True
    )

    return products[:count]


def getAllProducts():

    # Middle-man function so repo function "getAll" isn't exposed directly

    products = getAll()

    return products 