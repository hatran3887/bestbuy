class Product:

    def __init__(self, name, price, quantity):
        if type(name) != str or not name:
            raise ValueError("Product name is required")
        if type(price) not in (float, int) or price < 0:
            raise ValueError("Product price is required")
        if type(quantity) != int or quantity < 0:
            raise ValueError("Product quantity is required")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}')


    def buy(self, quantity):
        if type(quantity) != int or quantity <= 0:
            raise ValueError("Product quantity is required")
        if quantity > self.quantity:
            raise ValueError("Out of stock")
        self.quantity -= quantity
        return quantity * self.price