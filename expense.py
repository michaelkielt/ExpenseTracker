class Expense:
    
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount

    def __repr__(self) -> str:
        return f"Expense: {self.name}, {self.type}, £{self.amount}"