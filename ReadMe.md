# WOVEN MONOPOLY

## OVERVIEW

Woven monopoly is a deterministic monopoly game.
Players start with a balance of $16. The game proceed as: 
1. Must purchase the property if they land on a space is unowned.
2. Must pay rent if they land on a space is owned by another. Rent is doubled if all properties of the same colour are owned by same player.
3. Earn 1$ when passing GO.
4. Ends when a player become bankrupt (Unable to pay for rent or buy property), player with the most money wins.

## DESIGN DECISIONS

To ensure functionality with extensibility and maintainability:
- Using seperate modules for **Rolls**, **Board**, **Players** and **Game logic** to isolate individual functionalities. Enhancing code readability and extensibility.
- Functions are designed to handle specific game actions, ensuring clear logic and smooth gameplay. Also helps for debugging.
- The **main.py** is responsible for setting up game components and simulating gameplay. Makes it easier to adapt to different files and players.
- Rolls and board files are provided via file paths passed as argument instead of hard-coded. Allows for easy customization and efficient setup.

## ADDITIONAL INFORMATION

- Rent is equal to the price of the property.
- Bankrupt indicates a player cannot afford the price or rent.
- Players take turns in the order they appear in the list.
- GO is assumed to be at the 0 index of the board.

## HOW TO EXECUTE

1. Clone the repository to local machine:
```bash
git clone https://github.com/DlD27/MONOPOLY.git
```
2. Make sure Python is installed:
```bash
python --version
```
3. Run the game using the following command (Pass board and rolls file paths):
```bash
python main.py "board_file_path" "rolls_file_path"
```

## HOW TO TEST

### 1. Unit test with Python
Run unit tests to ensure every function runs and returns expected value:
``` bash
python -m unittest
```

### 2. Additional test with custom rolls and board
Provide custom board and rolls files (test_board and test_roll) for a quick check to ensure the game performs as expected:
```bash
python main.py "test_board_file_path" "test_roll_file_path"
```
