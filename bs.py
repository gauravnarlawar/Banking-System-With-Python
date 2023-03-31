import os
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful. New balance is: ", self.balance)
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance. You cannot withdraw more than your balance.")
        self.balance -= amount
        print("Withdrawal successful. New balance is: ", self.balance)
    def get_balance(self):
        return self.balance
    def __str__(self):
        return f"Account holder: {self.name}, balance: {self.balance}"
def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter your initial balance: "))
    account = BankAccount(name, balance)
    with open("accounts.txt", "a") as file:
        file.write(f"{name},{balance}\n")
    print(f"Account created successfully. {account}")
def deposit_money():
    name = input("Enter account holder's name: ")
    amount = float(input("Enter amount to deposit: "))
    with open("accounts.txt", "r") as file:
        accounts = file.readlines()
        for account in accounts:
            acc_name, balance = account.strip().split(",")
            if acc_name == name:
                account = BankAccount(name, float(balance))
                account.deposit(amount)
                with open("accounts.txt", "w") as file:
                    for acc in accounts:
                        if acc.strip().split(",")[0] == name:
                            acc = f"{name},{account.get_balance()}\n"
                        file.write(acc)
                break
        else:
            print("Account not found.")
def withdraw_money():
    name = input("Enter account holder's name: ")
    amount = float(input("Enter amount to withdraw: "))
    with open("accounts.txt", "r") as file:
        accounts = file.readlines()
        for account in accounts:
            acc_name, balance = account.strip().split(",")
            if acc_name == name:
                account = BankAccount(name, float(balance))
                try:
                    account.withdraw(amount)
                except ValueError as e:
                    print(e)
                    break
                with open("accounts.txt", "w") as file:
                    for acc in accounts:
                        if acc.strip().split(",")[0] == name:
                            acc = f"{name},{account.get_balance()}\n"
                        file.write(acc)
                break
        else:
            print("Account not found.")
def view_balance():
    name = input("Enter account holder's name: ")
    with open("accounts.txt", "r") as file:
        accounts = file.readlines()
        for account in accounts:
            acc_name, balance = account.strip().split(",")
            if acc_name == name:
                account = BankAccount(name, float(balance))
                print(account)
                break
        else:
            print("Account not found.")
if __name__ == "__main__":
    while True:
        print("\nBank Account Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            view_balance()
        elif choice == 5:
            break