def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

n = int(input("Enter a number: "))
print(f"The factors of {n} are: {find_factors(n)}")
