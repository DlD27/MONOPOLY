from player import Player
from board import load_board
from rolls import load_rolls

def play_game(board, rolls):

    # Initialise players
    players = [
        Player("Peter", board), 
        Player("Billy", board), 
        Player("Charlotte", board), 
        Player("Sweedal", board)
    ]
    for player in players:
        print(player)

    game_over = False   # Flag to indicate game has ended
    turn = 0            # Turn count
    roll_index = 0      # Index in the rolls list
    GO_REWARD = 1       # Amount given when land on GO
    
    while not game_over:
        current_player = players[turn % len(players)] # Determine the current player

        # Check if there are rolls left
        if roll_index >= len(rolls):
            print(f"GAME OVER: OUT OF ROLLS")
            game_over = True
            break
        current_roll = rolls[roll_index] # The roll for current player

        # Move the player if not bankrupt
        if not current_player.move(current_roll):
            game_over = True
            break

        # Find current space after the move
        current_space = current_player.position

        # Handle property space
        if current_space.type == "property":
            # The property is unowned by others, the player buys it
            if current_space.owner == None:
                if not current_player.buy_property(current_space):
                        game_over = True
                        break
        # Handle GO space
        elif current_space.type == "go":
            current_player.balance += GO_REWARD
            print(f"The player lands on GO balance increase by $1")
        
        # Next turn
        turn += 1
        roll_index += 1
    
    return True