import calendar  # To get month names
import argparse
import json
from datetime import datetime


# Load existing expenses from a file
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    # If the file is missing or has invalid JSON, initialize an empty list
    expenses = []


def addExpense():
    if not args.description or args.amount is None:
        print("Error: Please provide both a description and a positive amount for the expense.")
        return

    if args.amount <= 0:
        print("Error: Amount must be greater than zero.")
        return

    # Check for duplicate descriptions (case-insensitive)
    if any(expense["description"].lower() == args.description.lower() for expense in expenses):
        print(f"Error: Expense with description '{args.description}' already exists.")
        return

    # Create a new expense dictionary
    expense = {
        "id": max((expense["id"] for expense in expenses), default=0) + 1,  # Auto-increment ID   
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "description": args.description,
        "type":args.type,
        "amount": args.amount
    }
    expenses.append(expense)
    print(f"Expense added successfully (ID: {expense['id']})")
    saveFile()


def listExpenses():
    # If a type is provided, filter expenses by type
    if args.type:
        # Filter expenses by type
        filtered_expenses = [expense for expense in expenses if expense["type"] == args.type]
        
        # Display filtered expenses
        if filtered_expenses:
            print(f"{'ID':<5}{'Date':<20}{'Description':<15}{'Expense Type':<15}{'Amount':<10}")
            print("-" * 50)
            for expense in filtered_expenses:
                print(f"{expense['id']:<5}{expense['date']:<20}{expense['description']:<15}{expense['type']:<15}${expense['amount']:<10}")
        else:
            print(f"No expense found with type '{args.type}'.")
    else:
        # If no type is provided, list all expenses
        if expenses:
            print(f"{'ID':<5}{'Date':<20}{'Description':<15}{'Expense Type':<15}{'Amount':<10}")
            print("-" * 50)
            for expense in expenses:
                # Handle 'type' being None
                expense_type = expense.get('type', 'N/A') if expense.get('type') is not None else 'N/A'
                # Handle 'amount' being None
                expense_amount = expense.get('amount', 0.0) if expense.get('amount') is not None else 0.0
                
                print(f"{expense['id']:<5}{expense['date']:<20}{expense['description']:<15}{expense_type:<15}${expense_amount:<10.2f}")
        else:
            print("No expense found.")



def deleteExpense():
    try:
        # Convert 1-based ID to 0-based index
        index = args.id - 1

        # Validate index range
        if 0 <= index < len(expenses):
            deleted_expense = expenses.pop(index)
            print(f"Expense '{deleted_expense['description']}' (ID: {args.id}) has been deleted.")

            # Save expenses to the file
            saveFile()
        else:
            print(f"Error: Expense with ID #{args.id} was not found.")
    except ValueError:
        print("Error: Please provide a valid numeric ID.")
    except IndexError:
        print("Error: Invalid ID range.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def expenseSummary():
    if args.month:
        # Validate the month argument
        if 1 <= args.month <= 12:
            # Filter expenses for the given month
            total_amount = sum(
                expense['amount'] for expense in expenses
                if datetime.strptime(expense['date'], "%Y-%m-%d %H:%M:%S").month == args.month
            )
            monthname = calendar.month_name[args.month]  # Get the month's name
            print(f"Total Expenses for {monthname}: ${total_amount}")
        else:
            print("Error: Please provide a valid month (1-12).")

    elif args.type:
        # Filter expenses by type
        total_amount = sum(
                expense['amount'] for expense in expenses if expense["type"] == args.type
            )
        print(f"Total Expenses for Expense Type '{args.type}': ${total_amount}")

    else:
        if expenses:
             # Calculate the total amount of all expenses
            total_amount = sum(expense['amount'] for expense in expenses)
            # Display the summary
            print(f"Total Expenses: ${total_amount}")
        else:
            print("No expenses recorded.")

    
def saveFile():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)



# Initialize the parser
parser = argparse.ArgumentParser(description="Expense tracker CLI to manage your finances")
parser.add_argument("operation", type=str, help="Operation to execute: add, list, summary, delete")
parser.add_argument("--description", nargs="?", type=str, help="The expense description (for 'add' or 'update' operations)")
parser.add_argument("--type", nargs="?", type=str, help="type of the expense:housing, transportation, food, business ")
parser.add_argument("--amount", nargs="?", type=float, help="Amount of the expense")
parser.add_argument("--id", nargs="?", type=int, help="-")
parser.add_argument("--month", nargs="?", type=int, help="-")



# Parse arguments
args = parser.parse_args()

# Handle operations
if args.operation == "add":
    addExpense()

elif args.operation == "list":
    listExpenses()

elif args.operation == "summary":
    expenseSummary()

elif args.operation == "delete":
    deleteExpense()

else:
    print(f"Error: Unsupported operation '{args.operation}'. Use -h for help.")