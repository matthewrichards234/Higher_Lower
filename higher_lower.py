import random

def higher_lower():
    r = random.randint(1, 100)
    guess = int(input("Guess a number between 1 - 100 \n"))
    while guess != r:
        if guess < r:
            print("You guessed a number LOWER that the answer.")
            guess = guess = int(input("Guess a number between 1 - 100 \n"))
        elif guess > r:
            print("You guessed a number HIGHER that the answer.")
            guess = guess = int(input("Guess a number between 1 - 100 \n"))
        else:
            print("Correct!")
            return True

print(higher_lower())

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

print(higher_lower())
