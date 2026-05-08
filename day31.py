class Account:
    def setAccount(self):
        self.__accountNumber = int(input("Enter Account Number: "))
        self.__balance = float(input("Enter Balance: "))

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def getBalance(self):
        return self.__balance

    def displayAccount(self):
        print("Account Info")
        print("Account Number:", self.__accountNumber)
        print("Balance:", self.__balance)


class SavingsAccount(Account):
    def setSavingsDetails(self):
        self.__interestRate = float(input("Enter Interest Rate: "))
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


class PremiumSavings(SavingsAccount):
    def setPremiumDetails(self):
        self.__bonus = float(input("Enter Bonus Amount: "))
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


obj = PremiumSavings()

obj.setAccount()
obj.setSavingsDetails()
obj.setPremiumDetails()

obj.calculateInterest()
obj.calculateTotalBalance()

obj.displayAccount()
obj.displaySavings()
obj.displayPremiumDetails()
obj.checkStatus()