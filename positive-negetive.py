def count_positive_negative(lst):
    positive = len([x for x in lst if x > 0])
    negative = len([x for x in lst if x < 0])
    return positive, negative

lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
positive, negative = count_positive_negative(lst)
print(f"Positive numbers: {positive}, Negative numbers: {negative}")
