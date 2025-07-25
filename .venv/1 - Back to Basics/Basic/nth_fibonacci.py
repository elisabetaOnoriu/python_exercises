def fibonacci(n):
    if n < 0:
        raise ValueError("The number must be zero or positive.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

try:
    n = int(input("Enter a whole number n: "))
    result = fibonacci(n)
    print(f"The {n}-th Fibonacci number is {result}")
except ValueError as e:
    print(f"Error: {e}")
