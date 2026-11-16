# Cart Classes

# Spencer
class Cart:
    def __init__(self, id, user_email, cart_items):
        self.cart_id = id
        self.user_email = user_email
        self.cart_items = cart_items

    def addItem(self, cart_item):
        # add cart_item object to cart
        if not isinstance(cart_item, CartItem):
            raise TypeError("cart_item must be a CartItem")

        self.cart_items.append(cart_item)
        return True
    
    def removeItem(self, cart_item):
        # Remove cartitem object from Cart
        if not isinstance(cart_item, CartItem):
            return False
        try:
            self.cart_items.remove(cart_item)
            return True
        except ValueError:
            return False
        

    def calculateTotal(self):
        return

    def isEmpty(self):
        return not self.cart_items

    def getId(self):
        return self.cart_id

    def getUserEmail(self):
        return self.user_email

    
# Spencer
class CartItem:
    def __init__(self, id, product_id, quantity):
        self.id = id
        self.product_id = product_id
        self.updateQuantity(quantity)

    def updateQuantity(self, quantity):
        if type(quantity) is not int:
            raise ValueError("Quantity must be an int.")

        if quantity < 1:
            raise ValueError("Quantity must be more than 0.")

        self.quantity = quantity
        return True

    def getId(self):
        return self.id

    def getProductId(self):
        return self.product_id

    def getQuantity(self):
        return self.quantity
