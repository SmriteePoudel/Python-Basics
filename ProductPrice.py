# 2. Operator Overloading

class Product:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price

p1 = Product(1000)
p2 = Product(2000)

print("Total Price:", p1 + p2)
