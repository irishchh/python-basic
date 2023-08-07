
class Bank_Balance:# bank balance is a class
    def __init__(self, name):
        self.name = name
        self.balance = 0.0


    def show_amount(self):
        print(f"{self.name} your total balance is {self.balance}")

    def deposite_amount(self,amount):
        self.balance += amount
        print(f"{self.name},your account has deposited {self.balance}")

    
    def withdraw_amount(self,amount):
        if amount > self.balance:
            print("Insufficient balance to withdraw")
        else:
            self.balance -= amount
            print(f"{self.name}your account has withdraw {self.balance}")
        


om = Bank_Balance("om")
om.show_amount()
om.deposite_amount(1000)
om.withdraw_amount(500)

