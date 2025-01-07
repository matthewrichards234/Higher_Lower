import random

def higher_lower():
    r = random.randint(1, 100)
    guess = int(input("Guess a number between 1 - 100: \n"))
    while guess != r:
        if guess < r:
            print("You guessed a number LOWER than the answer.")
        elif guess > r:
            print("You guessed a number HIGHER than the answer.")
        guess = int(input("Guess again: \n"))
    print("Correct! You guessed the number.")
    return True

def enter_players():
    # Store player names
    players = []

    while True:
        # Number of players playing
        try:
            n = int(input("Enter number of players (1-5): \n"))
            
            # Limiting total players
            if n < 1 or n > 5:
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
players_list = enter_players()
print("Here are the players:", players_list)

def track_turn(players):
    while higher_lower():
        turn = 0
        for player in players:
            print(f"It is {player[turn]}'s turn: \n")
            higher_lower(player[turn])
            turn += 1

            # Reset player turns when length of players is exceeded
            if turn > len(players):
                turn = 0

def main():
    print("Welcome to the Higher-Lower Game!")
    enter_players()
    players = enter_players()
    track_turn(players)

#track_turn(players)
#print(track_turn)

