import json

"""
Function to load the monopoly board from a JSON file
Reusable for adapting differents board configuration
"""
def load_board(file_path):
    # Attempt to open and load the board from the JSON file
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    # Handle the case where the file does not exist
    except FileNotFoundError:
        print(f"Error: The file does not exist")
        return None 
    # Handle the case where the file is not valid JSON
    except json.JSONDecodeError:
        print(f"Error: The file is not in valid JSON form")
        return None
    # Catch any other exceptions
    except Exception as e:
        print(f"Error: Unexpected error {e}")

# Print to ensure the board is loaded correctly
board = load_board('/Users/esmeralda/Downloads/new_coding_test/board.json')
print(board if board else "Unable to load board data")