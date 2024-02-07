from expense import Expense


def main():
    # Get user input for specific expense
    get_user_input()
    # Write user expense to a file
    
    # Read file and break down expenses
    
    pass 

def get_user_input():
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
            new_expense = Expense(expense_name, expense_amount, expense_types[selected_index])
            return new_expense
        else:
            print("Invalid index selection, please try again.")

def write_expense_to_file():
    print("checking 2 works")
    pass

def summarise_expenses():
    print("checking 3 works")
    pass

if __name__ == '__main__':
    main()