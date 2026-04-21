# Class 1: Account
class Account:
    def __init__(self):
        self.__accountNumber = 0  
        self.__balance = 0.0        

    def setAccount(self):
        self.__accountNumber = input("Enter Account Number: ")
        self.__balance = float(input("Enter Initial Balance: "))

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def getBalance(self):
        return self.__balance

    def displayAccount(self):
        print(" Account Info ")
        print("Account Number:", self.__accountNumber)
        print("Balance:", self.__balance)



class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.__interestRate = 0.0
        self.__interest = 0

    def setSavingsDetails(self):
        self.__interestRate = float(input("Enter Interest Rate: "))

    def calculateInterest(self):
        
        balance = self.getBalance()
        self.__interest = (balance * self.__interestRate) / 100
        return self.__interest

    def getInterest(self):
        return self.__interest

    def displaySavings(self):
        print("--- Savings Info ---")
        print("Interest:", self.__interest)


class PremiumSavings(SavingsAccount):
    def __init__(self):
        super().__init__()
        self.__bonus = 0
        self.__totalBalance = 0

    def setBonus(self):
        self.__bonus = float(input("Enter Bonus: "))

    def calculateTotalBalance(self):
        balance = self.getBalance()
        interest = self.getInterest()
        self.__totalBalance = balance + interest + self.__bonus
        return self.__totalBalance

    def checkStatus(self):
        if self.__totalBalance > 20000:
            print("VIP Customer")
        else:
            print("Regular Customer")

    def displayPremiumDetails(self):
        print("--- Premium Info ---")
        print("Bonus:", self.__bonus)
        print("Total Balance:", self.__totalBalance)



obj = PremiumSavings()
obj.setAccount()
obj.setSavingsDetails()
obj.calculateInterest()
obj.setBonus()
obj.calculateTotalBalance()

obj.displayAccount()
obj.displaySavings()
obj.displayPremiumDetails()
obj.checkStatus()




#EKuta child class ko matra object use garera garni 