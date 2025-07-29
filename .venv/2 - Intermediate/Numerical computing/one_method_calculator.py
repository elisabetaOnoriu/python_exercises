class Calculator:
    def __init__(self):
        self.operations = {
            "add": lambda a, b: a + b,
            "subtract": lambda a, b: a - b,
            "multiply": lambda a, b: a * b,
            "divide": lambda a, b: "Error: division by zero" if b == 0 else a / b,
            "power": lambda a, b: a**b,
        }

    def calculate(self, operation, a, b):
        func = self.operations.get(operation)
        if func:
            return func(a, b)
        return "Invalid operation"


calculator = Calculator()

print(calculator.calculate("add", 3, 4))
print(calculator.calculate("power", 2, 10))
print(calculator.calculate("divide", 10, 0))
print(calculator.calculate("unknown", 1, 1))
