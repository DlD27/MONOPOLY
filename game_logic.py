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
    roll_index = 0      # Index in the rolls listg
    
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
        
        # Next turn
        turn += 1
        roll_index += 1

    if game_over:
        winners = Player.find_winners(players)
        if winners:
            print(f"Winner(s):")
            for winner in winners:
                print(f" {winner.name}")
        else:
            print(f"No Winner found")
        for player in players:
            print(player)

    return True