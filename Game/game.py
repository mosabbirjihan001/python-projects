# Initialize players and their scores
players = {}
rounds = 1

# Function to start the game
def start_game():
    print("Welcome to the Number Guessing Game!")
    num_players = int(input("Enter number of players: "))
    
    # Initialize players' names and scores
    for i in range(1, num_players + 1):
        player_name = input(f"Enter name of Player {i}: ")
        players[player_name] = 0
    
    # Start rounds
    while True:
        play_round()

def play_round():
    global rounds
    print(f"\n-- Round {rounds} --")
    
    # Numbers for calculation (can be changed as needed)
    numbers = [10, 2, 38, 90, 66, 22]
    average = sum(numbers) / len(numbers)
    target = average * 0.8
    print(f"Target number (calculated as average * 0.8) is {target:.2f}")

    guesses = {}
    
    # Collect guesses from players
    for player in players:
        guess = float(input(f"{player}, enter your guess: "))
        guesses[player] = guess
    
    # Check if two or more players chose the same number
    if len(set(guesses.values())) < len(guesses):
        print("Round disqualified: Two or more players chose the same number.")
        for player in guesses:
            players[player] -= 1
    else:
        # Find the player with the closest guess to the target
        closest_player = min(guesses, key=lambda player: abs(guesses[player] - target))
        print(f"The closest guess is by {closest_player} with a guess of {guesses[closest_player]}")

        if guesses[closest_player] == target:
            print(f"{closest_player} guessed the correct number!")
            players[closest_player] += 1
            for player in guesses:
                if player != closest_player:
                    players[player] -= 2
        else:
            print(f"No one guessed the correct number. Players closest to the target will get points.")
            for player in guesses:
                if guesses[player] == target:
                    players[player] += 1
                else:
                    players[player] -= 1

    # Check for elimination
    eliminated_players = [player for player, score in players.items() if score <= -10]
    
    # Display scores
    print("\nScores:")
    for player, score in players.items():
        print(f"{player}: {score}")
    
    if eliminated_players:
        print(f"\nEliminated players: {', '.join(eliminated_players)}")
        for player in eliminated_players:
            del players[player]
    
    # End game if no players left
    if len(players) == 0:
        print("\nGame Over. All players are eliminated!")
        exit()

    rounds += 1

# Start the game
start_game()
