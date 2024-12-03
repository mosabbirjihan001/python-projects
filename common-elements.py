def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = [int(x) for x in input("Enter elements of first list separated by space: ").split()]
lst2 = [int(x) for x in input("Enter elements of second list separated by space: ").split()]
print(f"Common elements: {common_elements(lst1, lst2)}")
