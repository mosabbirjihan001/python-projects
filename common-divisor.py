import math

def find_gcd(a, b):
    return math.gcd(a, b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"The GCD of {a} and {b} is {find_gcd(a, b)}")
