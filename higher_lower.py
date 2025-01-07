import random

MIN_NUM = 1
MAX_NUM = 1000
MIN_PLAYERS = 1
MAX_PLAYERS = 5

def higher_lower(player, target):
    while True:
        try:
            guess = int(input(f"{player}, guess a number between {MIN_NUM} and {MAX_NUM}: \n"))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        
        if guess < target:
            print(f"Your guess is too low! Try a higher number between {guess + 1} and {MAX_NUM}.")
        elif guess > target:
            print(f"Your guess is too high! Try a lower number between {MIN_NUM} and {guess - 1}.")
        else:
            print(f"Correct! {player}, you guessed the number!")
            return True

def enter_players():
    players = []
    while True:
        try:
            n = int(input("Enter number of players (1-5): \n"))
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

def main():
    print("Welcome to the Higher-Lower Game!")

    # Get player names
    players_list = enter_players()
    print("Here are the players:", players_list)

    # Generate a target number
    target = random.randint(MIN_NUM, MAX_NUM)

    # Game loop
    current_player_index = 0
    while True:
        current_player = players_list[current_player_index]
        print(f"It is {current_player}'s turn.")
        if higher_lower(current_player, target):
            return f"The winner is {current_player}!"
        current_player_index = (current_player_index + 1) % len(players_list)

# Uncomment to play!
print(main())
