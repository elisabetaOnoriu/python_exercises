def factorial_mod(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

n = int(input("Enter a number n to compute n!: "))
mod = int(input("Enter a modulus (e.g. 1000000007): "))

print(f"{n}! mod {mod} = {factorial_mod(n, mod)}")
