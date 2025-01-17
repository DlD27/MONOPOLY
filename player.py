class Player:
    def __init__(self, name, board):
        self.name = name            
        self.balance = 16           # Starting balance for the player
        self.position = board[0]    # Starting position on the board
        self.properties = []        # List of properties owned the by player
        self.board = board          # Board the player is playing on

    # Updates player's position based on the roll
    def move(self, roll):
        if self.balance >= 0:
            current_index = self.board.index(self.position)
            new_index = (current_index + roll) % len(self.board)
            self.position = self.board[new_index]
            print(f"{self.name} moved to {self.position.name}")
            return True
        else:
            print(f"{self.name} is bankrupt.")
            return False
    
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
            print(f"{self.name} is bankrupt.")
            return False

    # Allow the player to pay rent to the owner of a property when having enough balance
    def pay_rent(self, property):
        rent = property.price
        if (rent <= self.balance):
            self.balance -= rent
            property.owner.balance += rent
            print(f"{self.name} pays rent ${rent} to {property.name}'s onwer {property.owner.name}")
            return True
        else:
            self.balance -= property.price
            print(f"{self.name} is bankrupt.")
            return False
    
    # Player's status
    def __str__(self):
        return f"Player: {self.name} has ${self.balance} and is at {self.position.name}" 


