import json

class Property:
    def __init__(self, name, type, price, colour):
        self.name = name
        self.type = type
        self.price = price
        self.colour = colour
        self.owner = None

# Load the monopoly board from a JSON file
def load_board(file_path):

    # Attempt to open and parse the board from the JSON file
    try:
        with open(file_path, 'r') as file:
            board_spaces = json.load(file)
    # Handle the case where the file does not exist
    except FileNotFoundError:
        print(f"Error: The file does not exist")
        return None 
    # Handle the case where the file is not valid JSON
    except json.JSONDecodeError:
        print(f"Error: The file is not in valid JSON format")
        return None
    # Catch any other exceptions
    except Exception as e:
        print(f"Error: Unexpected error {e}")
        return None

    # Initialize an empty list and to represents spaces in board
    board = []
    for space in board_spaces:
        if space['type'] == 'property':
            property = Property(space['name'], space['type'], space['price'], space['colour'])
            board.append(property)
        if space['type'] == 'go':
            go = Property(space['name'], space['type'], 0, "")
            board.append(go)
    return board