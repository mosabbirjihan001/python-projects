def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

n = int(input("Enter a number: "))
print(f"The sum of digits is {sum_of_digits(n)}.")
