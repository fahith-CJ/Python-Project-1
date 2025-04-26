class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self): 
        # Calculates the total balance across all accounts.
        return sum(account.get_balance() for account in self.accounts)

    def get_account_count(self):
        # Returns the count of accounts associated with the user.
        return len(self.accounts)

    def remove_account(self, account):
        # Removes an account if it exists.
        if account in self.accounts:
            self.accounts.remove(account)
            return f"Account {account.get_account_type()} removed successfully."
        return "Error: Account not found."

    def is_valid_email(self, email):
        # Validates the email format using regex.
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def __str__(self):
        # Provides a readable string representation of the user.
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: Rs. {self.get_total_balance():,.2f}"
