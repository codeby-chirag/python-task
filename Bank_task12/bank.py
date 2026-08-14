import random


class Account:
    def __init__(self, holder_name, account_no, account_type, amount, interest_rate):
        self.holder_name = holder_name
        self.account_no = account_no
        self.account_type = account_type
        self.balance = amount
        self.interest_rate = interest_rate     
    
    def register(self):
        accounts[self.account_no] = self
        print("Account created successfully!")
        print(f"Account Number: {self.account_no}")
        print(f"Holder Name: {self.holder_name}")
        
    # Withdraw
    def withdraw_money(self, amount):
        if not(amount > 0):
            print("Error: Amount is must more than Rs.0")
        elif amount > self.balance:
            print("Insufficient Balance.")
        else:
            self.balance = self.balance - amount
            print("Transaction Successful.")
            print(f"Current Balance: {self.balance}")
            
    # deposit
    def deposite_money(self, amount):
        if not(amount > 0):
            print("Error: Amount is must more than Rs.0")
        else:
            self.balance += amount
            print("Transaction Successful.")
            print(f"Current Balance: {self.balance}")

class SavingAccount(Account):
    # interest rate float
    # Calculate interest
    def calculate_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest Added: {interest}")
        print(f"Current Balance: {self.balance}")
            
class CurrentAccount(Account):
    # current account no interest
    def calculate_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest Added: {interest}")
        print(f"Current Balance: {self.balance}")

saving_acc = SavingAccount(
    holder_name = "John",
    account_no = 17000343536,
    account_type = "Saving",
    amount = 5000,
    interest_rate = 7.5
) 
 
current_acc = CurrentAccount(
    holder_name = "Tom",
    account_no = 17000252627,
    account_type = "Current",
    amount = 10000,
    interest_rate = 2
)

accounts = {
    saving_acc.account_no: saving_acc,
    current_acc.account_no: current_acc
}

while True:
    print("""Choose the operation you want to perform:
        1. Register new account
        2. Withdraw money
        3. Deposit money
        4. Calculate Interest
        5. Exit"""
    )

    choice = input("\nEnter choice: ")
    
    if choice == "1":
        acc_holder_name = input("Enter Name: ")
        acc_number = 17000000000 + random.randint(0, 999999)
        while acc_number in accounts:
            acc_number = 17000000000 + random.randint(0, 999999)
        
        acc_type = input("Which account you want to open Saving or Current ?: ").strip().title()
        while acc_type != "Saving" and acc_type != "Current":
            acc_type = input("Which account you want to open Saving or Current ?: ").strip().title()
            
        deposite_money = int(input("Enter amount you want to Deposite as first transadction: "))

        if acc_type == "Saving":
            obj = SavingAccount(
                holder_name = acc_holder_name,
                account_no = acc_number,
                account_type = acc_type,
                amount = deposite_money,
                interest_rate = 7.5
            )

        elif acc_type == "Current":
            obj = CurrentAccount(
                holder_name = acc_holder_name,
                account_no = acc_number,
                account_type = acc_type,
                amount = deposite_money,
                interest_rate = 2
            )

        obj.register()

    elif choice == "2":
        while True:
            try:
                acc_num = int(input("Enter Account number: "))
                amount = float(input("Enter Amount you want to Withdraw: "))
                break
            except ValueError:
                print("Enter valid Account number and Amount")
    
        if acc_num not in accounts:
            print("Account does not exist")
            continue
        
        account = accounts[acc_num]
        account.withdraw_money(amount)
            
    elif choice == "3":
        while True:
            try:
                acc_num = int(input("Enter Account number: "))
                amount = float(input("Enter Amount you want to Deposit: "))
                break
            except ValueError:
                print("Enter valid Account number and Amount")
                
        if acc_num not in accounts:
            print("Account does not exist")
            continue
        
        account = accounts[acc_num]
        account.deposite_money(amount)
        
    elif choice == "4":
        while True:
            try:
                acc_num = int(input("Enter Account number: "))
                break
            except ValueError:
                print("Enter valid Account number")
        
        if acc_num not in accounts:
            print("Account does not exist")
            continue
        
        account = accounts[acc_num]
        account.calculate_interest()
    
    elif choice == "5":
        break
    
    else:
        print("Invalid choice. Please try again.")