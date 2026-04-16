# Syntax


class Test:
    a = 100
    b = 123


obj = Test()
obj.data = "Hello World"
obj1 = Test()
obj1.data = "This is to locate obj data just in case of obj1"
obj2 = Test()
print(obj)
print(obj == obj1)  # Value address is different so it prints False
print(obj1)
print(obj2)
print(obj.data)
print(obj1.data)


print(obj.a)
print(obj1.a)
print(obj2.a)


# Methods


class Math:
    a = 30
    b = 20

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def result(self):
        return {"add": self.add(), "sub": self.sub()}


obj = Math()
print(obj.add())
print(obj.sub())
print(obj.result())

print("--------------" * 3)


class StingTest:
    data = "Hello World"

    def __str__(self):
        return f"{self.data} this is from str func"


obj = StingTest()
print(obj)

#Constructor

class ConstTest():
    data = "Hello World"
    def __init__(self,a,b,c):
        print(a,b,c)
        print("this is from constructor")
        self.a=a
        self.b=b
        self.c=c
    def add(self):
        print(self.a+self.b+self.c)    





obj=ConstTest(1,2,4)
obj.add()  
  

    


