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
