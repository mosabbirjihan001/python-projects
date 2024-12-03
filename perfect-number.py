def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

n = int(input("Enter a number: "))
if is_perfect_number(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
