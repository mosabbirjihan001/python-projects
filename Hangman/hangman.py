import random

def hangman():
    print("Welcome to Hangman!")
    
    words = ["python", "java", "javascript", "ruby", "html", "css", "programming"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6  # You can make 6 incorrect guesses
    
    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"Word: {display_word}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
        elif guess in word:
            guessed_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    
    if attempts == 0:
        print(f"You've run out of attempts. The word was: {word}")

hangman()
