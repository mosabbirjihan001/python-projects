def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
print(f"The number of vowels in the string is {count_vowels(string)}.")
