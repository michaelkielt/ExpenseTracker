import calendar as cal
import datetime as dt
from expense import Expense


def main():
    """
    Main function to run the expense tracker.
    """
    print("Running the expense tracker!")
    expense_file_path = "expenses.csv"
    budget = 800
    expense = get_user_input()
    write_expense_to_file(expense, expense_file_path)
    summarise_expenses(expense_file_path, budget)


def get_user_input():
    """
    Function to get user input for expense details.

    Returns:
        Expense: An instance of Expense class with user-defined attributes.
    """
    expense_name = input("Enter the name of the expense here: ")
    expense_amount = float(input("Enter the amount of the expense in £: "))
    expense_types = [
        "Food",
        "Rent",
        "Work",
        "Fun",
        "Misc"
    ]

    while True:
        print("Please select a category: ")
        for i, type in enumerate(expense_types):
            print(f" {i+1}. {type} ")

        value_range = f"1 - {len(expense_types)}"
        selected_index = int(input(f"Select a number from {value_range}: ")) - 1

        if selected_index in range(len(expense_types)):
            new_expense = Expense(name=expense_name, type=expense_types[selected_index], amount=expense_amount)
            return new_expense
        else:
            print("Invalid index selection, please try again.")


def write_expense_to_file(expense: Expense, expense_file_path):
    """
    Function to write expense details to a file.

    Args:
        expense (Expense): An instance of Expense class.
        expense_file_path (str): Path to the expense file.
    """
    print(f"Saving <{expense}> to {expense_file_path}")
    with open(expense_file_path, "a") as file:
        file.write(f"{expense.name}, {expense.type}, {expense.amount} \n")


def summarise_expenses(expense_file_path, budget):
    """
    Function to summarize expenses and remaining budget.

    Args:
        expense_file_path (str): Path to the expense file.
        budget (float): Monthly budget allocated.
    """
    print("Summarising user expenses")
    expenses = []
    with open(expense_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            expense_name, expense_type, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                type=expense_type,
                amount=float(expense_amount)
            )
            expenses.append(line_expense)

    amount_by_type = {}
    for expense in expenses:
        key = expense.type
        if key in amount_by_type:
            amount_by_type[key] += expense.amount
        else:
            amount_by_type[key] = expense.amount

    print("Summarising expenses by type: ")
    for key, amount in amount_by_type.items():
        print(f" {key}: £{amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"You have spent £{total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"You're remaining budget this month is £{remaining_budget:.2f}")

    now = dt.datetime.now()
    days_in_current_month = cal.monthrange(now.year, now.month)[1]
    remaining_days = days_in_current_month - now.day
    print("Remaining days in the current month: ", remaining_days)

    daily_budget = remaining_budget / remaining_days
    print(f"Your budget per day is: £{daily_budget:.2f}")


if __name__ == '__main__':
    main()
