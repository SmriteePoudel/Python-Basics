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
    def __init__(self,a,b):
        print("this is from child class")
        super().__init__(a,b)
            # super() is used to call the constructor of parent class

    def result(self):
        return self.add()


obj = Child(1,2)
print(obj.result())



#Multiple Inheritance

class GrandParent(Child):
    def summary(self):
        return "this is from grand parent class all summary data"
obj=GrandParent()
print(obj.summary())    



  
              
     