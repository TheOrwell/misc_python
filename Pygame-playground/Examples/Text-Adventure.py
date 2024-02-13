import random

# Define dialogue options for characters
dialogues = {
    "guard": [
        "Halt! Who goes there?",
        "What's the password?",
        "You're not authorized to enter!",
        "State your business!"
    ],
    "merchant": [
        "Welcome, traveler! Interested in my wares?",
        "Looking for something special?",
        "I have the finest goods in all the land!",
        "Buy something or move along!"
    ],
    "innkeeper": [
        "Welcome to our inn! Would you like a room?",
        "We have a warm bed waiting for you!",
        "Rest and recover, weary traveler.",
        "Make yourself at home!"
    ]
}

# Define rooms and characters in each room
rooms = {
    "forest": ["guard", "merchant"],
    "town": ["innkeeper", "merchant"],
    "castle": ["guard", "innkeeper"]
}

# Define player's starting location
current_room = "forest"

# Main game loop
while True:
    # Print current location
    print(f"You are in the {current_room.capitalize()}.")

    # Choose a random character in the current room
    current_character = random.choice(rooms[current_room])

    # Display character's dialogue
    print(f"{current_character.capitalize()}: {random.choice(dialogues[current_character])}")

    # Ask the player for input
    user_input = input("What do you want to do? ")

    # Check if the player wants to move to another room
    if user_input.lower() == "move":
        next_room = input("Where do you want to go? (forest, town, castle): ").lower()
        if next_room in rooms.keys():
            current_room = next_room
        else:
            print("You can't go there!")

    # Check if the player wants to quit the game
    elif user_input.lower() == "quit":
        print("Thanks for playing!")
        break

    # Otherwise, continue the conversation
    else:
        print("You continue the conversation...")

    print()  # Empty line for clarity
