class ConstTest:
    data = "Hello World"

    def __init__(self, a, b, c):
        print(a, b, c)
        print("this is from constructor")
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        self.d = 100
        print(self.a + self.b + self.c)


obj = ConstTest(1, 2, 4)
obj.add()
print(obj.d)


#Deposit and withdrawl in ATM



class ATM():
    def __init__(self):
        self.balance = 10000


    def withdraw(self,amount):
        if amount>self.balance:
            return "Amount is greater than current balance"
        self.balance = self.balance - amount
        return f'{amount} is withdraw and current balance is {self.current_balance()}'

    def deposit(self, amount):
        if amount<0:
            return "Number must be positive"
        self.balance = self.balance + amount
        return f'{amount} is deposit and current balance is {self.current_balance()}'


    def current_balance(self):
        return self.balance

obj = ATM()
print(obj.deposit(1000))
print(obj.withdraw(200))
print(obj.withdraw(20000))
print(obj.deposit(-1000))


#Online shopping cart

class shopping_cart():
    def __init__(self,name,item):
        
        self.name= name
        self.item=item 
        if isinstance(item,list):
            for i in item:
                self.total=0
                self.total=self.total+i["price"]

            

            
        else:    
            print("Item must be in list")
        print(f'{name} has total price of {self.total}')    

        if self.total>1000:
            discount=self.total*(10/100)
            self.total=self.total-discount
            print("You get 10% discount")


    def order_summary(self):
        return f'{self.name} has total price of {self.total}'
        #discount baki 
        
    
            
            
item=[{
    "item":"Mobile",
    "price":10000
},
{
    "item":"Laptop",
    "price":50000
},
{"item":"TV"
 ,"price":30000},
 {"item":"Fridge",
  "price":20000}
]
obj=shopping_cart("Smriti",item)   
obj.order_summary()        
            
       
