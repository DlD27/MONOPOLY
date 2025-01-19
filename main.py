# main.py

from game_logic import play_game
from rolls import load_rolls
from board import load_board
from player import Player

def main():

    # Load the board and dice rolls
    board = load_board("/Users/esmeralda/Downloads/new_coding_test/board.json")
    rolls = load_rolls("/Users/esmeralda/Downloads/new_coding_test/rolls_2.json")

    # Initialise players
    players = [
        Player("Peter", board), 
        Player("Billy", board), 
        Player("Charlotte", board), 
        Player("Sweedal", board)
    ]

    if board and rolls:
        play_game(board, rolls, players)

if __name__ == "__main__":
    main()
