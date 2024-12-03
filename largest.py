def find_largest_smallest(lst):
    return max(lst), min(lst)

lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
largest, smallest = find_largest_smallest(lst)
print(f"Largest: {largest}, Smallest: {smallest}")
