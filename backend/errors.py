class ProductError(Exception):
    pass


class ProductNotFoundError(ProductError):
    pass


class InvalidSearchFieldError(ProductError):
    pass