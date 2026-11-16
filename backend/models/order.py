# Order Classes

# Prashant
class Order:
    def __init__(
        self,
        order_id,
        user_email,
        date_placed,
        order_status,
        subtotal,
    ):
        self.order_id = order_id
        self.user_email = user_email
        self.date_placed = date_placed
        self.order_status = order_status
        self.subtotal = subtotal

    def getId(self):
        return self.order_id

    def getUserEmail(self):
        return self.user_email

    def getDatePlaced(self):
        return self.date_placed

    def getOrderStatus(self):
        return self.order_status

    def getSubtotal(self):
        return self.subtotal

    def getDict(self):
        return {
            "id": self.order_id,
            "userEmail": self.user_email,
            "datePlaced": self.date_placed,
            "orderStatus": self.order_status,
            "subtotal": self.subtotal,
        }


# Prashant
class OrderItem:
    def __init__(
        self,
        order_item_id,
        order_id,
        product_id,
        quantity,
        purchase_price,
    ):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.purchase_price = purchase_price

    def getId(self):
        return self.order_item_id

    def getOrderId(self):
        return self.order_id

    def getProductId(self):
        return self.product_id

    def getQuantity(self):
        return self.quantity

    def getPurchasePrice(self):
        return self.purchase_price

    def getLineTotal(self):
        return self.quantity * self.purchase_price

    def getDict(self):
        return {
            "id": self.order_item_id,
            "orderId": self.order_id,
            "productId": self.product_id,
            "quantity": self.quantity,
            "purchasePrice": self.purchase_price,
            "lineTotal": self.getLineTotal(),
        }
