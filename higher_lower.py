import random

def higher_lower():
    r = random.randint(1, 100)
    print("Welcome to the Higher-Lower Game!")
    guess = int(input("Guess a number between 1 - 100: \n"))
    while guess != r:
        if guess < r:
            print("You guessed a number LOWER than the answer.")
        elif guess > r:
            print("You guessed a number HIGHER than the answer.")
        guess = int(input("Guess again: \n"))
    print("Correct! You guessed the number.")
    return True

#print(higher_lower())

def enter_players():
    # Store player names
    players = []

    # Number of players playing
    n = int(input("Enter number of players (1-5): \n"))

    # Base case limiting total players
    if (n < 1) or (n > 5):
        print("Please enter player number betwee 1-5.\n")

    for p in range(n):
        while len(players) < n:
            p = input("Enter player name: \n").title()
            if p in players:
                print("Please enter unique names per player.\n")
            else:
                players.append(p)
        print("All players added! Good luck!")

    return players

def track_turn():
    while higher_lower():
        pass


#print(enter_players())
