class Expense:
    """
    Class representing an expense.

    Attributes:
        name (str): The name of the expense.
        type (str): The type or category of the expense.
        amount (float): The amount of money spent on the expense.
    """
    
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount
    """
        Initialises an Expense object.

        Args:
            name (str): The name of the expense.
            type (str): The type or category of the expense.
            amount (float): The amount of money spent on the expense.
        """
    def __repr__(self) -> str:
        return f"Expense: {self.name}, {self.type}, £{self.amount}"
    """
        Returns a string representation of the Expense object.

        Returns:
            str: A string representation of the Expense object.
    """