import random

# Define the player's deck of cards
player_deck = ["Attack", "Attack", "Attack", "Defend", "Defend", "Heal", "Heal", "Draw"]

# Define the opponent's deck of cards
opponent_deck = ["Attack", "Attack", "Defend", "Defend", "Heal", "Draw", "Draw", "Draw"]

# Initialize player and opponent health
player_health = 100
opponent_health = 100

# Main game loop
while True:
    # Display player and opponent health
    print(f"Your Health: {player_health}")
    print(f"Opponent's Health: {opponent_health}")
    print()

    # Player's turn
    print("Your Turn:")
    print("1. Play a card")
    print("2. End turn")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your Deck:", player_deck)
        card_to_play = input("Enter the card you want to play: ")
        if card_to_play in player_deck:
            print(f"You played {card_to_play}.")
            if card_to_play == "Attack":
                opponent_health -= 20
            elif card_to_play == "Defend":
                player_health += 10
            elif card_to_play == "Heal":
                player_health += 20
            elif card_to_play == "Draw":
                drawn_card = random.choice(player_deck)
                print(f"You drew {drawn_card}.")
                player_deck.append(drawn_card)
            player_deck.remove(card_to_play)
        else:
            print("You don't have that card in your hand.")

    elif choice == "2":
        print("End of turn.")

    # Check if the opponent has been defeated
    if opponent_health <= 0:
        print("Congratulations! You defeated your opponent.")
        break

    # Opponent's turn
    print("\nOpponent's Turn:")
    card_played = random.choice(opponent_deck)
    print(f"Opponent played {card_played}.")
    if card_played == "Attack":
        player_health -= 20
    elif card_played == "Defend":
        opponent_health += 10
    elif card_played == "Heal":
        opponent_health += 20
    elif card_played == "Draw":
        drawn_card = random.choice(opponent_deck)
        print(f"Opponent drew {drawn_card}.")
        opponent_deck.append(drawn_card)

    # Check if the player has been defeated
    if player_health <= 0:
        print("You have been defeated. Game over.")
        break

    print()  # Empty line for clarity
