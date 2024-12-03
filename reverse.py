def reverse_number(n):
    return int(str(n)[::-1])

n = int(input("Enter a number: "))
print(f"The reversed number is: {reverse_number(n)}")
