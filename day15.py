# Inheritance

# Single Inheritance


class Parent:
    data = "hello world"

    def add(self):
        return "this is from parent class"


class Child(Parent):
    a = 100


obj = Child()
print(obj.data)
print(obj.add())


# Inheritance with constructor
class Parent:
    a = 1010
    b = 1000

    def __init__(self):
        print("this is from parent class")

    def add(self):
        return self.a + self.b


class Child(Parent):
    def __init__(self):
        print("this is from child class")
        super().__init__()
            # super() is used to call the constructor of parent class

    def result(self):
        return self.add()


obj = Child()
print(obj.result())
