def binary_to_decimal(binary_str):
    return int(binary_str, 2)

binary_str = input("Enter a binary number: ")
print(f"The decimal equivalent is: {binary_to_decimal(binary_str)}")
