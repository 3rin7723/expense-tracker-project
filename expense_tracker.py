# Expense Tracker Program

# Dictionary to store expenses
expenses = {}

# Function to add expense
def add_expense(expenses):
    try:
        expense_id = len(expenses) + 1
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")

        expenses[expense_id] = {
            "category": category,
            "amount": amount,
            "date": date
        }

        print("Expense added successfully.")

    except ValueError:
        print("Invalid amount entered.")


# Function to view expenses
def view_expenses(expenses):

    if not expenses:
        print("No expenses recorded.")
        return

    for expense_id, details in expenses.items():
        print(
            f"ID: {expense_id} | Category: {details['category']} | Amount: ${details['amount']} | Date: {details['date']}"
        )


# Function to calculate total expenses
def total_expenses(expenses):

    total = 0

    for details in expenses.values():
        total += details["amount"]

    print("Total expenses: $", total)


# Function to delete expense
def delete_expense(expenses):

    expense_id = int(input("Enter expense ID to delete: "))

    if expense_id in expenses:
        del expenses[expense_id]
        print("Expense deleted.")
    else:
        print("Expense not found.")


# Menu
def menu():

    while True:

        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


menu()
