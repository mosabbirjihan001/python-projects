def sum_of_list(lst):
    return sum(lst)

lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(f"The sum of the list is: {sum_of_list(lst)}")
