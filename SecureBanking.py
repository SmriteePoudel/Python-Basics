
class Account:
    def __init__(self, accountNumber, balance):
        self.__accountNumber = accountNumber
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def getBalance(self):
        return self.__balance

    def displayAccount(self):
        print("Account Info")
        print("Account Number:", self.__accountNumber)
        print("Balance:", self.__balance)


class SavingsAccount(Account):
    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber, balance)
        self.__interestRate = interestRate
        self.__interest = 0

    def calculateInterest(self):
        balance = self.getBalance()
        self.__interest = (balance * self.__interestRate) / 100
        return self.__interest

    def getInterest(self):
        return self.__interest

    def displaySavings(self):
        print("Savings Info")
        print("Interest:", self.__interest)


# Class 3: PremiumSavings
class PremiumSavings(SavingsAccount):
    def __init__(self, accountNumber, balance, interestRate, bonus):
        super().__init__(accountNumber, balance, interestRate)
        self.__bonus = bonus
        self.__totalBalance = 0

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
        print("Premium Info")
        print("Bonus:", self.__bonus)
        print("Total Balance:", self.__totalBalance)



obj = PremiumSavings(101, 15000, 10, 2000)

obj.calculateInterest()
obj.calculateTotalBalance()

obj.displayAccount()
obj.displaySavings()
obj.displayPremiumDetails()
obj.checkStatus()