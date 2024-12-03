def even_odd_range(start, end):
    print("Even numbers:")
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print("\nOdd numbers:")
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i, end=" ")

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
even_odd_range(start, end)
