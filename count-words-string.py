def count_words(s):
    return len(s.split())

string = input("Enter a string: ")
print(f"The number of words is: {count_words(string)}")
