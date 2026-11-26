class ATM:
    def __init__(self):
        self.secret_pin = "0000"
        self.account_balance = 5000


    def withdraw(self, amt):
        if self.secret_pin == input("Enter Pin: "):
            if self.account_balance >= amt:
                self.account_balance = self.account_balance - amt
                print("Updated Balance is: ", self.account_balance)
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect Pin")

obj1 = ATM()

print(obj1.account_balance)
print(obj1.secret_pin)

obj1.withdraw(500)

obj1.secret_pin = "1234"
obj1.account_balance = 0

print(obj1.account_balance)
print(obj1.secret_pin)

obj1.withdraw(500)