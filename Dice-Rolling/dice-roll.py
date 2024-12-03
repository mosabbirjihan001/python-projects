import random

def dice_roll():
    print("Welcome to Dice Rolling Simulator!")
    
    while True:
        roll = input("Type 'roll' to roll the dice, or 'quit' to exit: ").lower()
        if roll == 'quit':
            print("Thanks for playing!")
            break
        
        if roll == 'roll':
            dice_result = random.randint(1, 6)
            print(f"You rolled a {dice_result}!")
        else:
            print("Invalid input. Please type 'roll' to roll or 'quit' to exit.")

dice_roll()
