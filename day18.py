#Encapsulation- Data access modifier
class Modifier:
    __a="Private turned public"
   
    b=__a

class Test(Modifier):
    d=2


obj=Test()
print(obj.b) # this is public variable and can be accessed outside the class
#obj1=Modifier()
#print(obj1.__a) # this is private variable and cannot be accessed outside the class

#It works same for method also 

def __test():
    print("this is private method")


    