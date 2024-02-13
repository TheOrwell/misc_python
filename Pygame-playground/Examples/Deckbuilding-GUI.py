import random
import tkinter as tk
from tkinter import messagebox

class DeckBuilderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Deck Builder Game")

        # Define the player's deck of cards
        self.player_deck = ["Attack", "Attack", "Attack", "Defend", "Defend", "Heal", "Heal", "Draw"]

        # Define the opponent's deck of cards
        self.opponent_deck = ["Attack", "Attack", "Defend", "Defend", "Heal", "Draw", "Draw", "Draw"]

        # Initialize player and opponent health
        self.player_health = 100
        self.opponent_health = 100

        # Create GUI elements
        self.player_health_label = tk.Label(master, text=f"Your Health: {self.player_health}")
        self.player_health_label.grid(row=0, column=0)
        self.opponent_health_label = tk.Label(master, text=f"Opponent's Health: {self.opponent_health}")
        self.opponent_health_label.grid(row=1, column=0)

        self.play_card_button = tk.Button(master, text="Play Card", command=self.play_card)
        self.play_card_button.grid(row=2, column=0)

        self.end_turn_button = tk.Button(master, text="End Turn", command=self.end_turn)
        self.end_turn_button.grid(row=3, column=0)

        self.info_text = tk.Text(master, height=5, width=50)
        self.info_text.grid(row=4, column=0, columnspan=2)

        # Create a label to display the player's hand
        self.player_hand_label = tk.Label(master, text="Your Hand:")
        self.player_hand_label.grid(row=5, column=0)

        self.player_hand = tk.Label(master, text=", ".join(self.player_deck))
        self.player_hand.grid(row=5, column=1)

    def play_card(self):
        card_to_play = random.choice(self.player_deck)
        if card_to_play == "Attack":
            self.opponent_health -= 20
            self.info_text.insert(tk.END, f"You played {card_to_play}. You dealt 20 damage to the opponent.\n")
        elif card_to_play == "Defend":
            self.player_health += 10
            self.info_text.insert(tk.END, f"You played {card_to_play}. You gained 10 health.\n")
        elif card_to_play == "Heal":
            self.player_health += 20
            self.info_text.insert(tk.END, f"You played {card_to_play}. You healed 20 health.\n")
        elif card_to_play == "Draw":
            drawn_card = random.choice(self.player_deck)
            self.info_text.insert(tk.END, f"You played {card_to_play}. You drew {drawn_card}.\n")
            self.player_deck.append(drawn_card)
        self.player_deck.remove(card_to_play)
        self.update_health_labels()
        self.update_hand_labels()

        self.check_game_over()

        self.opponent_turn()

    def end_turn(self):
        self.opponent_turn()

    def opponent_turn(self):
        card_played = random.choice(self.opponent_deck)
        if card_played == "Attack":
            self.player_health -= 20
            self.info_text.insert(tk.END, f"Opponent played {card_played}. You took 20 damage.\n")
        elif card_played == "Defend":
            self.opponent_health += 10
            self.info_text.insert(tk.END, f"Opponent played {card_played}. Opponent gained 10 health.\n")
        elif card_played == "Heal":
            self.opponent_health += 20
            self.info_text.insert(tk.END, f"Opponent played {card_played}. Opponent healed 20 health.\n")
        elif card_played == "Draw":
            drawn_card = random.choice(self.opponent_deck)
            self.info_text.insert(tk.END, f"Opponent played {card_played}. Opponent drew {drawn_card}.\n")
            self.opponent_deck.append(drawn_card)
        self.update_health_labels()

        self.check_game_over()

    def update_health_labels(self):
        self.player_health_label.config(text=f"Your Health: {self.player_health}")
        self.opponent_health_label.config(text=f"Opponent's Health: {self.opponent_health}")

    def update_hand_labels(self):
        self.player_hand.config(text=", ".join(self.player_deck))

    def check_game_over(self):
        if self.opponent_health <= 0:
            messagebox.showinfo("Game Over", "Congratulations! You defeated your opponent.")
            self.master.quit()
        elif self.player_health <= 0:
            messagebox.showinfo("Game Over", "You have been defeated. Game over.")
            self.master.quit()

def main():
    root = tk.Tk()
    game = DeckBuilderGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
