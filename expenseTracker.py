import datetime
import sys

listOfExpenses = []
expense_id = 1

def expanseTracker():
    while True:
        print("\nWelcome to the Expense Tracker")
        print("1. Add Expense\n2. Delete Expense\n3. Update Expense\n4. View Expenses\n5. Summary of Expenses\n6. Exit")
        option = input("Please select an option: ")
        if option == '1':
            addExpense()
        elif option == '2':
            deleteExpense()
        elif option == '3':
            updateExpense()
        elif option == '4':
            viewExpense()
        elif option == '5':
            summaryExpense()
        elif option == '6':
            exitProgram()
        else:
            print("Invalid option, please try again.")

def addExpense():
    global expense_id
    date = datetime.datetime.now()
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount: "))
    expense = {
        'id': expense_id,
        'date': date,
        'description': description,
        'amount': amount
    }
    listOfExpenses.append(expense)
    expense_id += 1
    print("Expense added successfully")

def deleteExpense():
    id_to_delete = int(input("Enter the id of the expense you want to delete: "))
    for expense in listOfExpenses:
        if expense['id'] == id_to_delete:
            listOfExpenses.remove(expense)
            print("Expense deleted successfully")
            return
    print("Expense not found")

def updateExpense():
    id_to_update = int(input("Enter the id of the expense you want to update: "))
    for expense in listOfExpenses:
        if expense['id'] == id_to_update:
            description = input("Enter the new description of the expense: ")
            amount = float(input("Enter the new amount: "))
            expense['description'] = description
            expense['amount'] = amount
            print("Expense updated successfully")
            return
    print("Expense not found")

def viewExpense():
    if not listOfExpenses:
        print("No expenses recorded.")
    for expense in listOfExpenses:
        print(f"ID: {expense['id']}, Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']}")

def summaryExpense():
    total = sum(expense['amount'] for expense in listOfExpenses)
    print("Total expenses: ", total)

def exitProgram():
    print("Thank you for using the Expense Tracker.")
    sys.exit()

# Start the expense tracker
expanseTracker()
