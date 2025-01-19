import unittest
from player import Player
from board import load_board
from rolls import load_rolls, DiceRolls
from game_logic import play_game

class TestGame(unittest.TestCase):
    
    # Load testing board, rolls and players
    def setUp(self):
        self.board = load_board("/Users/esmeralda/Downloads/new_coding_test/test_board.json")
        self.rolls = load_rolls("/Users/esmeralda/Downloads/new_coding_test/test_roll.json")
        self.players = [
            Player("Peter", self.board),
            Player("Billy", self.board),
            Player("Charlotte", self.board),
            Player("Sweedal", self.board)
        ]

    # Test whether players are correctly initialized
    def test_player_initialization(self):
        player = self.players[0]
        self.assertEqual(player.name, "Peter")
        self.assertEqual(player.balance, 16)
        self.assertEqual(player.position, self.board[0])

    # Test whther rolls are correctly loaded from JSON
    def test_rolls(self):
        roll = self.rolls.next_roll()
        self.assertEqual(roll, 7)
        roll = self.rolls.next_roll()
        self.assertEqual(roll, 7)

    # Test whether player move to the space based on the roll
    def test_player_move(self):
        player = self.players[0]
        player.move(4)
        self.assertEqual(player.position, self.board[4])

    # Test whether player can correctly purchase a property
    def test_buy_property(self):
        player = self.players[0]
        property_space = self.board[2]
        player.buy_property(property_space)
        self.assertEqual(property_space.owner, player)
    
    # Test whether game will end when a player is bankrupt
    def test_game_over(self):
        player = self.players[0]
        player.balance = 0
        property_space = self.board[2]
        rent = property_space.calc_rent(self.board)
        game_over = not player.pay_rent(rent, property_space)
        self.assertTrue(game_over)

    # Test whether the winners are correctly identified
    def test_find_winners(self):
        self.players[0].balance = 20
        self.players[1].balance = 15
        self.players[2].balance = 25
        self.players[3].balance = 25
        winners = Player.find_winners(self.players)
        self.assertEqual(len(winners), 2)
        self.assertEqual(winners[0].name, "Charlotte") 
        self.assertEqual(winners[1].name, "Sweedal") 
    
    # Test whether the play_game function executes
    def test_play_game(self):
        result = play_game(self.board, self.rolls, self.players)
        self.assertIsInstance(result, bool)

if __name__ == "__main__":
    unittest.main()