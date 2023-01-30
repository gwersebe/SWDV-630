# Gabriel Wersebe
import random

class CheckingAccount:
    def __init__(self, name, address, balance, pin_number=None):
        self.name = name
        self.address = address
        self._balance = balance
        self.account_number = str(random.randint(10000,99999))
        if pin_number:
            self.pin_number = pin_number
        else:
            self.pin_number = str(random.randint(1000,9999))

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount, pin):
        if self.pin_number == pin:
            if self._balance >= amount:
                self._balance -= amount
            else:
                print("Insufficient funds")
        else:
            print("Incorrect Pin")

    def get_balance(self):
        return self._balance

def main():
    accounts = []
    while True:
        print("Checking Account Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            address = input("Enter address: ")
            balance = float(input("Enter starting balance: "))
            pin = input("Enter 4-digit pin number: ")
            account = CheckingAccount(name, address, balance, pin)
            accounts.append(account)
            print("Account created successfully with account number:", account.account_number)
        elif choice == 2:
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    print("Deposit successful.")
                    break
            else:
                print("Account not found.")
        elif choice == 3:
            account_number = input("Enter account number: ")
            pin = input("Enter pin number: ")
            amount = float(input("Enter withdrawal amount: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.withdraw(amount, pin)
                    break
            else:
                print("Account not found.")
        elif choice == 4:
            account_number = input("Enter account number: ")
            for account in accounts:
                if account.account_number == account_number:
                    print("Account balance:", account.get_balance())
                    break
            else:
                print("Account not found.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()