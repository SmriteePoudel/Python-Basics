# 5. Online Shopping System (Hybrid Inheritance)

class Customer:
    def customer_info(self):
        print("Customer: Premium User")


class Product(Customer):
    def product_info(self):
        print("Product: Laptop")


class Payment(Customer):
    def payment_info(self):
        print("Payment: Completed")


class Order(Product, Payment):
    def order_status(self):
        print("Order: Successfully Placed")


o = Order()
o.customer_info()
o.product_info()
o.payment_info()
o.order_status()