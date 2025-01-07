import random

MIN_NUM = 1
MAX_NUM = 3
MIN_PLAYERS = 1
MAX_PLAYERS = 5

def higher_lower():
    r = random.randint(MIN_NUM, MAX_NUM)
    while True:
        try:
            guess = int(input(f"Guess a number between {MIN_NUM} - {MAX_NUM}: \n"))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        
        if guess < r:
            print(f"Your guess is too low! Try a higher number between {guess + 1} and {MAX_NUM}.")
        elif guess > r:
            print(f"Your guess is too high! Try a lower number between {MIN_NUM} and {guess - 1}.")
        else:
            print("Correct! You guessed the number!")
            return True

def enter_players():
    # Store player names
    players = []

    while True:
        # Number of players playing
        try:
            n = int(input("Enter number of players (1-5): \n"))
            
            # Limiting total players
            if n < MIN_PLAYERS or n > MAX_PLAYERS:
                print("Please enter a number between 1 and 5.\n")
                continue
                
            while len(players) < n:
                p = input("Enter player name: \n").strip().title()
                if p in players:
                    print("Please enter unique names per player.\n")
                else:
                    players.append(p)
            print("All players added! Good luck!")

            return players

        except ValueError:
            print("Invalid input. Please enter an integer.")

def track_turn(players):
    num_players = len(players)
    current_player_index = 0  # Index turn
    for player in players:
        print(f"It is {player[current_player_index]}'s turn: \n")
        current_player_index = (current_player_index + 1) % num_players
    
def main():
    print("Welcome to the Higher-Lower Game!")

    # Get player names
    players_list = enter_players()
    print("Here are the players:", players_list)
    
    while higher_lower() != True:
        game = track_turn(players_list)

# Uncomment when ready to play!
#print(main)