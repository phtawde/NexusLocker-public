# Product-related service functions to bridge api functions to database functions

from backend.repositories.product_repo import search, getAll
from backend.errors import InvalidSearchFieldError

def searchProducts(field, query):

    # Validate search fields and call repo function "search"

    productColumns = ["id", "name", "description", "price", "stock", "dateAdded"]

    if field not in productColumns:
        raise InvalidSearchFieldError(field)

    return search(field, query)


def getLatestProducts(count):

    # Sort product by add date and then get the first "count" from the product list

    products = getAll()

    products.sort(
        key=lambda product: product.getDateAdded(), reverse=True
    )

    return products[:count]


def getAllProducts():

    # Middle-man function so repo function "getAll" isn't exposed directly

    products = getAll()

    return products 