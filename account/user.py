class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        """Adds an account to the user's account list."""
        self.accounts.append(account)

    def get_total_balance(self): 
        """Calculates the total balance across all accounts."""
        return round(sum(account.get_balance() for account in self.accounts), 2)

    def get_account_count(self):
        """Returns the count of accounts associated with the user."""
        return len(self.accounts)

    def remove_account(self, account):
        """Removes an account if it exists."""
        if account in self.accounts:
            self.accounts.remove(account)
            return f"Account {account.get_account_type()} removed successfully."
        return "Error: Account not found."

    def is_valid_email(self, email):
        """Validates the email format using regex."""
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))

    def __str__(self):
        """Provides a readable string representation of the user."""
        account_details = ', '.join([acc.get_account_type() for acc in self.accounts])
        return (
            f"{self.name} ({self.email}) - {self.get_account_count()} account(s), "
            f"Total Balance: Rs. {self.get_total_balance():,.2f}. Accounts: {account_details or 'None'}"
        )
