from player import Player
from board import load_board
from rolls import load_rolls

def play_game(board, rolls, players):

    game_over = False   # Flag to indicate game has ended
    turn = 0            # Turn count
    
    while not game_over:

        current_player = players[turn % len(players)]   # Determine the current player
        current_roll = rolls.next_roll()                # The roll for current player

        # Check if there are rolls left
        if current_roll is None:
            print(f"GAME OVER: OUT OF ROLLS")
            game_over = True
            break

        # Move the player if not bankrupt and update their current space.
        current_player.move(current_roll)
        current_space = current_player.position

        # Handle property space
        if current_space.type == "property":
            # The property is unowned, purchase
            if current_space.owner == None:
                if not current_player.buy_property(current_space):
                        game_over = True
                        break
            # The property is owned by others, pay rent
            elif current_space.owner != current_player:
                rent = current_space.calc_rent(board)
                if not current_player.pay_rent(rent, current_space):
                    game_over = True
                    break
        
        print(current_player)
        # Next turn
        turn += 1

    # Bankrupt player has occurred, determine winners based on each player's status
    if game_over:
        winners = Player.find_winners(players)
        if winners:
            print("Winner(s): " + ", ".join(f"{winner.name}" for winner in winners))
        else:
            print(f"No Winner found")
        for player in players:
            print(player)

    return True