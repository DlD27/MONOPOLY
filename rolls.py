import json

class DiceRolls:
    def __init__(self, rolls):
        self.rolls = rolls  # List of dice rolls
        self.index = 0      # Tracks the current roll index

    # Retrieve the next roll from the list, if available
    def next_roll(self):
        if self.index < len(self.rolls):
            roll = self.rolls[self.index]
            self.index += 1
            return roll
        else:
            print("Reached the end of the rolls.")
            return None

# Load predefined dice rolls from a JSON file
def load_rolls(file_path):
    # Attempt to open and load the rolls from the JSON file
    try:
        with open(file_path, 'r') as file:
            rolls_data = json.load(file)
            return DiceRolls(rolls_data)
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