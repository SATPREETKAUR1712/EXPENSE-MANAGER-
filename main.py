from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  # Local MongoDB URI
db = client['expense_manager']
expenses_collection = db['expenses']

# Function to add an expense
def add_expense(amount, category):
    expense = {
        "amount": amount,
        "category": category
    }

    expenses_collection.insert_one(expense)
    print("Expense added successfully!")

# Function to list all expenses
def list_expenses():
    expenses = expenses_collection.find()
    if expenses_collection.count_documents({}) == 0:
        print("No expenses found.")
    else:
        print("List of Expenses:")
        for expense in expenses:
            print(f"ID: {expense['_id']}, Amount: {expense['amount']}, Category: {expense['category']}")

# Function to delete an expense
def delete_expense(amount):
    result = expenses_collection.delete_one({"amount": amount})
    if result.deleted_count > 0:
        print(f"Expense of amount {amount} deleted successfully!")
    else:
        print(f"No expense found with the amount {amount}. Please try again.")

# Function to edit an expense
def edit_expense(amount, new_category):
    result = expenses_collection.update_one({"amount": amount}, {"$set": {"category": new_category}})
    if result.modified_count > 0:
        print(f"Expense with amount {amount} updated successfully!")
    else:
        print(f"No expense found with the amount {amount}. Please try again.")

# Function to safely get a float amount from user 
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# user interface
while True:
    print("\nExpense Manager")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Delete Expense")
    print("4. Edit Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Add an expense
        amount = get_float_input("Enter the amount: ")  # Ensure valid float input
        category = input("Enter the category (e.g., food, transport): ")
        add_expense(amount, category)
    elif choice == "2":
        # List all expenses
        list_expenses()
    elif choice == "3":
        # Delete an expense
        amount = get_float_input("Enter the amount of the expense to delete: ")
        delete_expense(amount)
    elif choice == "4":
        # Edit an expense
        amount = get_float_input("Enter the amount of the expense to edit: ")
        new_category = input("Enter the new category: ")
        edit_expense(amount, new_category)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
