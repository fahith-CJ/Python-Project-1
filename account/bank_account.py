from account.transaction import Transaction
from account.user import User

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        # Validate initial balance
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Invalid initial balance! Must be a non-negative number.")
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = "Generic"
        self.user = User(name, email)

    def deposit(self, amount):
        # Validate deposit amount
        if not isinstance(amount