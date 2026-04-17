#Inheritance

#Single Inheritance

class Parent:
    data = "hello world"
    def add(self):
        return"this is from parent class"
class Child(Parent):
    a=100
obj= Child() 
print(obj.data)      
print(obj.add())

