import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def guessing_game(pet, root):
    number = random.randint(1, 10)
    while True:
        guess = simpledialog.askinteger("Guessing Game", "Guess a number between 1 and 10:", parent=root)
        if guess is None:  # User clicked Cancel
            return 0
        if 1 <= guess <= 10:
            break
        messagebox.showinfo("Guessing Game", "Invalid input! Please enter a number between 1 and 10.")

    if guess == number:
        messagebox.showinfo("Guessing Game", "You won! Your cat is happy!")
        pet.happiness += 20  # Increase happiness
        return 10  # Earn 10 coins
    else:
        messagebox.showinfo("Guessing Game", f"Wrong guess. The number was {number}. Try again!")
        return 0  # No coins earned

def memory_game(pet, root):
    # Initialize the game
    pairs = ["A", "A", "B", "B", "C", "C"]
    random.shuffle(pairs)
    revealed = [False] * 6  # Track which cards are revealed
    matched = [False] * 6   # Track which cards are matched
    attempts = 0
    coins_earned = 0

    while not all(matched):
        # Display the current state of the board
        board = " ".join(
            pairs[i] if revealed[i] or matched[i] else "?"
            for i in range(6)
        )
        messagebox.showinfo("Memory Game", f"Current Board:\n{board}")

        # Ask the user to select two cards
        try:
            card1 = simpledialog.askinteger("Memory Game", "Enter the position of the first card (1-6):", parent=root, minvalue=1, maxvalue=6)
            if card1 is None:  # User clicked Cancel
                return 0
            card2 = simpledialog.askinteger("Memory Game", "Enter the position of the second card (1-6):", parent=root, minvalue=1, maxvalue=6)
            if card2 is None:  # User clicked Cancel
                return 0
        except ValueError:
            messagebox.showinfo("Memory Game", "Invalid input! Please enter numbers between 1 and 6.")
            continue

        # Check if the selected cards match
        if card1 == card2:
            messagebox.showinfo("Memory Game", "You selected the same card twice. Try again!")
            continue

        if pairs[card1 - 1] == pairs[card2 - 1]:
            messagebox.showinfo("Memory Game", "Match found!")
            matched[card1 - 1] = True
            matched[card2 - 1] = True
        else:
            messagebox.showinfo("Memory Game", "No match. Try again!")

        attempts += 1

    # Game over
    messagebox.showinfo("Memory Game", f"Congratulations! You matched all pairs in {attempts} attempts!")
    pet.happiness += 30  # Increase happiness
    return 20  # Earn 20 coins