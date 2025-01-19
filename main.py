import sys
from game_logic import play_game
from rolls import load_rolls
from board import load_board
from player import Player

def main(board_file, rolls_file):

    # Load the board and dice rolls
    board = load_board(board_file)
    rolls = load_rolls(rolls_file)

    # Initialise players
    players = [
        Player("Peter", board), 
        Player("Billy", board), 
        Player("Charlotte", board), 
        Player("Sweedal", board)
    ]

    # Simulate the game
    if board and rolls:
        play_game(board, rolls, players)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Expecting: python main.py <board_file> <rolls_file>")
    else:
        main(sys.argv[1], sys.argv[2])
