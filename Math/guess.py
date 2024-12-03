import random

def math_game():
    print("Welcome to the Number Guessing Game!")
    print("You need to guess the number closest to the result.")
    print("The numbers for each round are hidden. After you guess, the game will calculate the result.")
    print("You get 1 point for the closest guess, and -1 for incorrect guesses.")
    print("If a player's score reaches -10, they are eliminated.")
    print("If two or more players choose the same number, the round is disqualified, and they get -1 point.")
    print("If someone guesses the correct answer, others lose 2 points!")

    # Game settings
    players = {}
    eliminated_players = set()
    rounds = 5

    # Get player names and initialize their scores
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        name = input(f"Enter name for player {i + 1}: ")
        players[name] = 0  # Initialize score to 0

    for round_number in range(1, rounds + 1):
        if len(players) <= 1:  # End game if only one player remains
            break

        print(f"\nRound {round_number}:")

        # Generate random numbers for the round (hidden to the players)
        numbers = [random.randint(1, 100) for _ in range(6)]  # Generate 6 random numbers

        # Players make their guesses
        guesses = {}
        for player in players:
            if player not in eliminated_players:
                while True:
                    try:
                        guess = float(input(f"{player}, enter your guess: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                guesses[player] = guess

        # Calculate the target number (average * 0.8)
        total_sum = sum(numbers)
        average = total_sum / len(numbers)
        target_number = average * 0.8

        print(f"\nThe random numbers were: {numbers}")
        print(f"The calculated target: ({total_sum} / 6) * 0.8 = {target_number:.2f}")

        # Check for duplicate guesses
        guessed_values = list(guesses.values())
        if len(guessed_values) != len(set(guessed_values)):
            print("\nDuplicate guesses detected! The round is disqualified.")
            for player in guesses:
                if player not in eliminated_players:
                    players[player] -= 1
            continue

        # Find the player closest to the target number
        closest_player = None
        closest_diff = float('inf')

        for player, guess in guesses.items():
            diff = abs(guess - target_number)
            if diff < closest_diff:
                closest_player = player
                closest_diff = diff

        print(f"\n{closest_player} guessed closest to the target {target_number:.2f}!")

        # Update points based on the result
        for player in players:
            if player == closest_player:
                players[player] += 1  # Winner gets 1 point
            elif player not in eliminated_players:
                players[player] -= 1  # Losers get -1 point

        # If someone guessed correctly, others lose 2 points
        if closest_diff == 0:
            print(f"{closest_player} guessed the correct answer! Everyone else loses 2 points.")
            for player in players:
                if player != closest_player and player not in eliminated_players:
                    players[player] -= 2

        # Check for players eliminated
        for player, score in players.items():
            if score <= -10 and player not in eliminated_players:
                eliminated_players.add(player)
                print(f"{player} has been eliminated!")
                del players[player]

        # Display current scores
        print("\nCurrent scores:")
        for player, score in players.items():
            print(f"{player}: {score} points")

    # Final results
    print("\nGame Over!")
    if len(players) == 1:
        winner = list(players.keys())[0]
        print(f"{winner} is the last player standing and wins!")
    else:
        winner = max(players, key=players.get)
        print(f"{winner} wins the game with the highest score!")

# Start the game
math_game()
