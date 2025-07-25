def fast_power(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

print("Enter two numbers to raise the first to the power of the second, one at a time:")
base = int(input("Base (first number): "))
exponent = int(input("Exponent (second number): "))

result = fast_power(base, exponent)

print(f"{base} to the power of {exponent} is {result}")
