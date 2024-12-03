def second_largest(lst):
    unique_numbers = list(set(lst))  # Remove duplicates
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = second_largest(lst)
if result is None:
    print("There is no second largest number.")
else:
    print(f"The second largest number is {result}.")
