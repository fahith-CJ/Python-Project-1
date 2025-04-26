from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
        return
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if not users:
        print("No users available.\n")
        return
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    if not users:
        print("No users available to create an account for.\n")
        return
    list_users()
    try:
        idx = int(input("Select user number: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        return

    print("Account Type:")
    print("1. Savings Account")
    print("2. Student Account")
    print("3. Current Account")
    try:
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
        return

    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)
    else:
        print("Invalid choice!")
        return

    users[idx].add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    if not users:
        print("No users available.\n")
        return
    list_users()
    try:
        idx = int(input("Select user number: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        return

    user = users[idx]
    if not user.accounts:
        print("No accounts available for this user.\n")
        return
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")

    try:
        acc_idx = int(input("Select account: ")) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid account selection.\n")
            return
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
        return

    user.accounts[acc_idx].deposit(amount)
    print("Deposit successful!\n")

def withdraw_money():
    if not users:
        print("No users available.\n")
        return
    list_users()
    try:
        idx = int(input("Select user number: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
    except ValueError:
