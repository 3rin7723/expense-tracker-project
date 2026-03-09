# Expense Tracker Project

# Global list to store all expense dictionaries
expenses = []


def add_expense():
    """Add a new expense to the list."""
    print("\n--- Add New Expense ---")

    category = input("Enter category: ").strip()

    if category == "":
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: $"))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()

    if date == "":
        print("Date cannot be empty.")
        return

    expense = {
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses():
    """Show all expenses."""
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Date: {expense['date']}")


def filter_by_category():
    """Show only expenses in a chosen category."""
    print("\n--- Filter Expenses by Category ---")

    if not expenses:
        print("No expenses found.")
        return

    chosen_category = input("Enter category to filter: ").strip()

    if chosen_category == "":
        print("Category cannot be empty.")
        return

    found = False

    for expense in expenses:
        if expense["category"].lower() == chosen_category.lower():
            print(f"Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Date: {expense['date']}")
            found = True

    if not found:
        print("No expenses found in that category.")


def calculate_total():
    """Calculate and display the total expense amount."""
    print("\n--- Total Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total expenses: ${total:.2f}")


def delete_expense():
    """Delete an expense by category and date."""
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses found.")
        return

    category = input("Enter category of expense to delete: ").strip()
    date = input("Enter date of expense to delete (YYYY-MM-DD): ").strip()

    if category == "" or date == "":
        print("Category and date cannot be empty.")
        return

    for expense in expenses:
        if expense["category"].lower() == category.lower() and expense["date"] == date:
            expenses.remove(expense)
            print("Expense deleted successfully.")
            return

    print("Expense not found.")


def show_menu():
    """Display the menu."""
    print("\n===== Expense Tracker =====")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. Filter expenses by category")
    print("4. Calculate total expenses")
    print("5. Delete specific expense")
    print("6. Exit")


def main():
    """Run the main program loop."""
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


main()

def view_expenses():
    """Show all expenses."""
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Date: {expense['date']}")

def calculate_total():
    """Calculate total amount of all expenses."""
    print("\n--- Total Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total expenses: ${total:.2f}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")
