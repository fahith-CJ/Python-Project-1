from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
# Ensure you import your bank_operator correctly, depending on how it is structured
# If it's a module, the way you're importing it looks fine:
# from bank_operator import bank_operator

# If it's a class, use:
# from bank_operator import BankOperator
# And initialize the object before using it, like so:
# bank_operator = BankOperator()

console = Console()

def menu():
    # Assuming bank_operator is already instantiated and methods are available for use
    # Example: bank_operator = BankOperator() if it's a class
    
    while True:
        console.clear()

        table = Table(title="🏦 Bank System Menu", title_style="bold magenta")
        table.add_column("Option", style="cyan", justify="center")
        table.add_column("Description", style="white")

        table.add_row("1", "Create User")
        table.add_row("2", "List Users")
        table.add_row("3", "Add Account")
        table.add_row("4", "Deposit")
        table.add_row("5", "Withdraw")
        table.add_row("6", "View Transactions")
        table.add_row("7", "Exit")

        console.print(table)

        # Use a loop to ensure the user selects a valid option
        while True:
            choice = Prompt.ask("👉 Choose option", choices=[str(i) for i in range(1, 8)], default="7")
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                break
            else:
                console.print("Invalid choice. Please select a valid option.", style="bold red")

        # Perform actions based on the user's choice
        if choice == '1':
            # Call the method for creating a user
            bank_operator.create_user()
        elif choice == '2':
            # List all users
            bank_operator.list_users()
        elif choice == '3':
            # Create an account for the user
            bank_operator.create_account()
        elif choice == '4':
            # Deposit money into an account
            bank_operator.deposit_money()
        elif choice == '5':
            # Withdraw money from an account
            bank_operator.withdraw_money()
        elif choice == '6':
            # View transactions
            bank_operator.view_transactions()
        elif choice == '7':
            # Exit the program
            console.print("\n👋 Exiting... Thank you for using the Bank System!", style="bold green")
            break

if __name__ == "__main__":
    menu()
    