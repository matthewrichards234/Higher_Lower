# Higher-Lower Game

A simple, fun, interactive number-guessing game where players take turns to guess a randomly generated number within a specified range.

## How It Works

1. **Player Setup:**
   - The game supports between 1 and 5 players.
   - Players enter their names, ensuring each name is unique.

2. **Gameplay:**
   - A random number between `MIN_NUM` and `MAX_NUM` is generated at the start of the game.
   - Players take turns guessing the number.
   - If a guess is too low or too high, hints are provided to narrow the range.
   - The game continues until one player guesses the correct number.

3. **Winner:**
   - The first player to guess the number correctly is declared the winner!

---

## Features

- **Flexible Player Count:** Play solo or with friends (up to 5 players).
- **Hints:** Receive hints for higher or lower guesses to improve your chances.
- **Interactive Turns:** Each player gets their turn in rotation.
- **Validation:** Robust input handling to ensure a smooth gameplay experience.

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Running the Game
1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt in the game folder.
3. Run the script using the following command:
   ```bash
   python higher_lower.py
