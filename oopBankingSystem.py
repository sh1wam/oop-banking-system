# BANNKING SYSTEM USING OOP

# PARENT CLASS: USER
# HOLDS DETAILS ABOUT AN USER
# HAS A FUNCTION TO SHOW USER DETAILS

# CHILD CLASS: BANK
# STORES DETAILS ABOUT THE BANK BALANCE
# STORE DETAILS ABOUT THE AMOUNT
# ALLOWS FOR DEPOSIT, WITHDRAW, VIEW_BALANCE

# PARENT-CLASS--------------------------------
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details: ")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

# CHILD-CLASS-----------------------------------
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated! : $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance: $", self.balance)

# DRIVER-CODE-------------------------------------------------
johan = Bank("johan", 32, "male")
johan.deposit(500)
johan.withdraw(300)
johan.withdraw(300)
johan.withdraw(200)
johan.deposit(500)
johan.view_balance()