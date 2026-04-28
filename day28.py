class Animal:
    def make_sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.make_sound()
c.make_sound()




#Payment system 
class Payment:
    def pay(self):
        print("Choose payment method")

class Esewa(Payment):
    def pay(self):
        print("Payment done using eSewa")

class Khalti(Payment):
    def pay(self):
        print("Payment done using Khalti")

e = Esewa()
k = Khalti()

e.pay()
k.pay()
