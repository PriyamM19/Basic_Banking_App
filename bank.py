
from argparse import Action


class Bank:
    def __init__(self, initial_amount = 0.00):
        self.balance = initial_amount


    def transaction_log(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string}\t\t\t BALANCE : {self.balance}\n\n")


    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.transaction_log(f"WITHDREW {amount}")


    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transaction_log(f"DEPOSITED {amount}")

account = Bank(100.100)
while True:
    try:
        action = input("What kind of actions do you wish to perform..??")
    except KeyboardInterrupt:
        print("\nLeaving ATM")
        break
    if action in ["withdrawal", "deposit"]:
        if action == "withdrawal":
            amount = input("How much do you want to WITHDRAW ??")
            account.withdrawal(amount)
        else:
            amount = input("How much do you want to DEPOSIT ??")
            account.deposit(amount)

        print("YOUR ACCOUNT BALANCE IS",account.balance)

    else:
        print("That is NOT A VALID ACTION. TRY AGAIN")
