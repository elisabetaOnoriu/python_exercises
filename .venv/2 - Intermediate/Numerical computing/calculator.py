class Calculator:

    def Add(self, a, b):
        return a + b

    def Subtract(self, a, b):
        return a - b

    def Multiply(self, a, b):
        return a * b

    def Divide(self, a, b):
        return a / b

    def Power(self, a, b):
        return a**b


a = 5
b = 4
calculator = Calculator()
print(calculator.Add(a, b))
print(calculator.Subtract(a, b))
print(calculator.Multiply(a, b))
print(calculator.Divide(a, b))
print(calculator.Power(a, b))
