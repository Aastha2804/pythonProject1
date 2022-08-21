import random
import datetime


class savings:

    def __init__(self, accountno, name, balance):
        self.Name = name
        self.Balance = balance
        self.Accountno = accountno

    @staticmethod
    def generateAno():
        accountno = "3"
        for i in range(0, 10):
            accountno = accountno + str(random.randint(0.9))
        return accountno

    def display(self):
        print("Account info", self.Accountno)
        print("Name is", self.Balance)
        print("Balance is", self.Accountno)

    def deposit(self):
        amount = int(input("Please enter the amount you want to deposit"))
        if amount > 0:
            self.Balance = self.Balance + amount
            print(f"The update balance is {self.Balance}")
            print(f"your amount has been successfully credited with Rs {amount} at {datetime.datetime.now()}")
            savings.miniData.append(
                f"your amount has been successfully credited with Rs {amount} at {datetime.datetime.now()}")

    def withdraw(self):
        amount = int(input("Please enter the amount you want to withdraw"))
        if amount > 0:
            self.Balance = self.Balance - amount
            print(f"The update balance is {self.Balance}")
            print(f"your amount has been successfully debited with Rs {amount} at {datetime.datetime.now()}")
            savings.miniData.append(
                f"your amount has been successfully debited with Rs {amount} at {datetime.datetime.now()}")

    miniData = []

    @classmethod
    def handleMinistatement(cls):
        for i in cls.miniData:
            print(i)


print("Welcome to SBI")
print("s-savings account, c - current account")
option = input("enter any 1 of the above option:")
if option == "s".lower():
    print("welcome to savings account")
    cname = input("please enter customer name:")
    cbalance = int(input("please enter account balance"))
    ano = savings.generateAno()
    s = savings(cname, cbalance, ano)
    s.display()
elif option == "c".lower():
    print("welcome to current account")
else:
    print("invalid option!!")
