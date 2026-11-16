class ProductError(Exception):
    pass


class ProductNotFoundError(ProductError):
    pass


class InvalidSearchFieldError(ProductError):
    pass

class OrderError(Exception):
    pass

class OrderNotFoundError(OrderError):
    pass