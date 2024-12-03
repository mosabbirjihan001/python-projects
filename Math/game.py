import random
import time

def math_challenge_game():
    print("Welcome to the Math Challenge Game!")
    print("Solve math problems to score points. Your score will increase as the difficulty grows.")
    print("You lose points for incorrect answers.")
    print("To quit the game, type 'quit' anytime.")
    
    score = 0
    level = 1
    difficulty = 10  # Defines the upper limit of numbers for each problem
    max_attempts = 3  # You get 3 attempts per question
    
    # List of operations
    operations = ['+', '-', '*', '/']
    
    while True:
        print(f"\nLevel {level} - Your score: {score}")
        
        # Generate random math problems
        operation = random.choice(operations)
        num1 = random.randint(1, difficulty)
        num2 = random.randint(1, difficulty)
        
        # Avoid division by zero
        if operation == '/' and num2 == 0:
            num2 = random.randint(1, difficulty)
        
        correct_answer = 0
        
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == '*':
            correct_answer = num1 * num2
        elif operation == '/':
            correct_answer = round(num1 / num2, 2)  # Round to 2 decimal places
        
        print(f"Solve: {num1} {operation} {num2}")
        
        attempts = 0
        while attempts < max_attempts:
            user_input = input(f"Your answer (Attempt {attempts + 1}/{max_attempts}): ")
            
            if user_input.lower() == 'quit':
                print("Thanks for playing!")
                print(f"Your final score: {score}")
                return
            
            try:
                user_answer = float(user_input)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if user_answer == correct_answer:
                print("Correct!")
                score += 10  # Award points for correct answers
                level += 1  # Increase difficulty
                difficulty += 5  # Increase the range of numbers for the next level
                break
            else:
                print("Incorrect!")
                score -= 5  # Deduct points for incorrect answers
                attempts += 1
                
                if attempts == max_attempts:
                    print(f"The correct answer was: {correct_answer}")
        
        if score < 0:
            print("You lost too many points. Game over!")
            break
        
        time.sleep(1)  # Short delay for the next question

math_challenge_game()
