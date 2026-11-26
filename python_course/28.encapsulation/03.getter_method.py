class ATM:
    def __init__(self):
        self.__secret_pin = "0000"
        self.__account_balance = 5000

    def view_balance(self):
        print("Account Balance is: ",self.__account_balance)

    def withdraw(self, amt):
        if self.__secret_pin == input("Enter Pin: "):
            if self.account_balance >= amt:
                self.account_balance = self.__account_balance - amt
                print("Updated Balance is: ", self.__account_balance)
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect Pin")

    def retrieve_balance(self):
        return self.__account_balance

obj1 = ATM()

#obj1.view_balance()

# print(obj1._ATM__account_balance)

# print(obj1.__account_balance)
# print(obj1.__secret_pin)

# obj1.withdraw(500)

# obj1.__secret_pin = "1234"
# obj1.account_balance = 0

# print(obj1.__account_balance)
# print(obj1.__secret_pin)

# obj1.withdraw(500)


balance = obj1.retrieve_balance()
print(balance)
