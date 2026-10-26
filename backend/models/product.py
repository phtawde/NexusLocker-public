# Product class

class Product:
    def __init__(self, id, name, description, category, price, stock, dateAdded):
        self._id = id
        self._name = name
        self._description = description
        self._category = category
        self._price = price
        self._stock = stock
        self._dateAdded = dateAdded

    def addStock(self, quantity):
        if quantity > 0:
            self._stock += quantity
            return True
        else:
            return False

    def removeStock(self, quantity):
        if self._stock >= quantity and quantity > 0:
            self._stock -= quantity
            return True
        else:
            return False

    def inStock(self):
        if self._stock >= 1:
            return True
        else:
            return False

    ## Getters

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def getCategory(self):
        return self._category

    def getPrice(self):
        return self._price

    def getStock(self):
        return self._stock

    def getDateAdded(self):
        return self._dateAdded

    def getDict(self):
        return {
            "id": self._id,
            "name": self._name,
            "description": self._description,
            "category": self._category,
            "price": self._price,
            "stock": self._stock,
            "dateAdded": self._dateAdded
        }