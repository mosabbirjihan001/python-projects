from collections import Counter

def count_frequency(lst):
    return dict(Counter(lst))

lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(f"The frequency of elements: {count_frequency(lst)}")
