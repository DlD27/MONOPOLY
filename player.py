STARTING_BALANCE = 16
GO_AWARD = 1

class Player:
    def __init__(self, name, board):
        self.name = name            
        self.balance = STARTING_BALANCE # Starting balance for the player
        self.position = board[0]        # Starting position on the board
        self.properties = []            # List of properties owned the by player
        self.board = board              # Board the player is playing on

    # Updates player's position based on the roll
    def move(self, roll):
        current_index = self.board.index(self.position)
        new_index = (current_index + roll) % len(self.board)

        # The player has completed one round of the board and passed GO
        if new_index < current_index:
            self.balance += GO_AWARD
            print(f"{self.name} passed GO, balance increase by $1")
         
        self.position = self.board[new_index]
        print(f"{self.name} moved to {self.position.name}")
        return True
    
    # Allow the player to buy a property when having enough balance
    def buy_property(self, property):
        if property.price <= self.balance:
            self.balance -= property.price
            self.properties.append(property)
            property.owner = self
            print(f"{self.name} bought {property.name} at ${property.price}")
            return True
        else:
            self.balance -= property.price
            print(f"{self.name} is bankrupt, unable to purchase a property.")
            return False

    # Allow the player to pay rent to the owner of a property when having enough balance
    def pay_rent(self, rent, property):
        if rent <= self.balance:
            self.balance -= rent
            property.owner.balance += rent
            print(f"{self.name} pays rent ${rent} to {property.name}'s owner {property.owner.name}")
            return True
        else:
            self.balance -= rent
            print(f"{self.name} is bankrupt, unable to pay rent.")
            return False
    
    # Identify the winner, which is the player with the most money on hand
    @staticmethod
    def find_winners(players):
        winners = []
        max_balance = max(player.balance for player in players)
        for player in players:
            if player.balance == max_balance:
                winners.append(player)
        return winners

    # Player's status
    def __str__(self):
        return f"Player: {self.name} has ${self.balance} and is at {self.position.name}" 