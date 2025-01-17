import json

# Load predefined dice rolls from a JSON file
def load_rolls(file_path):

    # Attempt to open and load the rolls from the JSON file
    try:
        with open(file_path, 'r') as file:
            rolls_data = json.load(file)
            return rolls_data
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