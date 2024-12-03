def decimal_to_binary(n):
    return bin(n)[2:]

n = int(input("Enter a decimal number: "))
print(f"The binary equivalent is: {decimal_to_binary(n)}")
