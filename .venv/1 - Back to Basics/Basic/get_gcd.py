def get_gcd():
    a = int(input("Insert a number: "))
    b = int(input("Insert another number: "))
    initial_a = a
    initial_b = b

    while b:
        a, b = b, a % b

    print(f"{initial_a} and {initial_b} greatest common divisor is: {a}")

get_gcd()
