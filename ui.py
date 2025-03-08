import tkinter as tk
from tkinter import ttk, font, messagebox, simpledialog
import pygame
from pet import VirtualPet
from game_logic import update_pet_stats, check_pet_health, check_achievements
from mini_games import guessing_game, memory_game
from shop import Shop

def create_gui(pet):
    # Initialize pygame for sound effects
    pygame.mixer.init()

    # Create the main window
    root = tk.Tk()
    root.title("Virtual Cat Simulator")
    root.geometry("400x500")  # Increased height for additional buttons
    root.configure(bg="#FFE4E1")  # Light pink background for kawaii aesthetic

    # Define custom fonts
    title_font = font.Font(family="Comic Sans MS", size=18, weight="bold")  # Kawaii font
    button_font = font.Font(family="Comic Sans MS", size=12)
    status_font = font.Font(family="Comic Sans MS", size=12)

    # Create a title label
    title_label = tk.Label(
        root,
        text=f"Welcome to {pet.name}'s World! 🐾",
        font=title_font,
        bg="#FFE4E1",  # Light pink background
        fg="#FF69B4"  # Hot pink text
    )
    title_label.pack(pady=10)

    # Create a frame for buttons
    button_frame = tk.Frame(root, bg="#FFE4E1")  # Light pink background
    button_frame.pack(pady=10)

    # Define button colors
    feed_button_bg = "#ADD8E6"  # Light Blue for Feed
    play_button_bg = "#F5F5DC"  # Beige for Play
    sleep_button_bg = "#D2B48C"  # Tan for Sleep
    mini_game_button_bg = "#FFD700"  # Gold for Mini-Games
    shop_button_bg = "#FFA07A"  # Light Salmon for Shop
    button_fg = "#000000"  # Black text

    # Create buttons
    feed_button = tk.Button(
        button_frame,
        text="Feed 🐟",
        font=button_font,
        bg=feed_button_bg,
        fg=button_fg,
        command=lambda: feed(pet, status_label, progress_bar, level_label, root)
    )
    feed_button.pack(side=tk.LEFT, padx=10)

    play_button = tk.Button(
        button_frame,
        text="Play 🎀",
        font=button_font,
        bg=play_button_bg,
        fg=button_fg,
        command=lambda: play(pet, status_label, progress_bar, level_label, root)
    )
    play_button.pack(side=tk.LEFT, padx=10)

    sleep_button = tk.Button(
        button_frame,
        text="Sleep 🌙",
        font=button_font,
        bg=sleep_button_bg,
        fg=button_fg,
        command=lambda: sleep(pet, status_label, progress_bar, level_label, root)
    )
    sleep_button.pack(side=tk.LEFT, padx=10)

    # Create a mini-games button
    mini_game_button = tk.Button(
        button_frame,
        text="Mini-Games 🎮",
        font=button_font,
        bg=mini_game_button_bg,
        fg=button_fg,
        command=lambda: open_mini_games(pet, status_label, root)
    )
    mini_game_button.pack(side=tk.LEFT, padx=10)

    # Create a shop button
    shop_button = tk.Button(
        button_frame,
        text="Shop 🛒",
        font=button_font,
        bg=shop_button_bg,
        fg=button_fg,
        command=lambda: open_shop(pet, status_label, root)
    )
    shop_button.pack(side=tk.LEFT, padx=10)

    # Create an aesthetic board (frame) for the status
    board_frame = tk.Frame(root, bg="#FFC0CB", bd=5, relief=tk.RAISED)  # Pink frame
    board_frame.pack(pady=10)

    # Create a status label inside the board
    status_label = tk.Label(
        board_frame,
        text="",
        font=status_font,
        bg="#FFC0CB",  # Pink background
        fg="#FFFFFF",  # White text
        justify=tk.LEFT
    )
    status_label.pack(pady=10, padx=10)

    # Create a level label
    level_label = tk.Label(
        root,
        text=f"Level: {pet.level} ⭐",
        font=status_font,
        bg="#FFE4E1",  # Light pink background
        fg="#FF69B4"  # Hot pink text
    )
    level_label.pack(pady=5)

    # Create a progress bar
    progress_bar = ttk.Progressbar(
        root,
        orient="horizontal",
        length=300,
        mode="determinate"
    )
    progress_bar.pack(pady=10)
    progress_bar["value"] = 0  # Initialize progress bar to 0

    # Style the progress bar to turn green when full
    style = ttk.Style()
    style.theme_use("default")
    style.configure("green.Horizontal.TProgressbar", background="#4CAF50")  # Green color

    # Initialize status
    update_status(pet, status_label)

    # Start the game loop
    def game_loop():
        update_pet_stats(pet)
        if check_pet_health(pet):
            root.quit()
        check_achievements(pet)
        update_status(pet, status_label)
        root.after(1000, game_loop)  # Update every 1 second

    root.after(1000, game_loop)
    root.mainloop()

def feed(pet, status_label, progress_bar, level_label, root):
    pet.feed()
    update_status(pet, status_label)
    update_progress(pet, progress_bar, level_label, root)

def play(pet, status_label, progress_bar, level_label, root):
    pet.play()
    update_status(pet, status_label)
    update_progress(pet, progress_bar, level_label, root)

def sleep(pet, status_label, progress_bar, level_label, root):
    pet.sleep()
    update_status(pet, status_label)
    update_progress(pet, progress_bar, level_label, root)

def open_mini_games(pet, status_label, root):
    while True:
        choice = simpledialog.askinteger("Mini-Games", "Choose a mini-game:\n1. Guessing Game\n2. Memory Game", parent=root)
        if choice is None:  # User clicked Cancel
            return
        if choice == 1:
            coins_earned = guessing_game(pet, root)
            break
        elif choice == 2:
            coins_earned = memory_game(pet, root)
            break
        else:
            messagebox.showinfo("Mini-Games", "Invalid choice! Please enter 1 or 2.")

    messagebox.showinfo("Mini-Games", f"You earned {coins_earned} coins!")
    update_status(pet, status_label)

def open_shop(pet, status_label, root):
    shop = Shop()
    shop.display_items()
    item = simpledialog.askstring("Shop", "Enter the item you want to buy:", parent=root)
    if item:
        shop.buy_item(item, pet)
        update_status(pet, status_label)

def update_status(pet, status_label):
    status_label.config(text=f"{pet.name}'s Status:\n"
                          f"Hunger: {pet.hunger}\n"
                          f"Happiness: {pet.happiness}\n"
                          f"Energy: {pet.energy}\n"
                          f"Health: {pet.health}\n"
                          f"Level: {pet.level} ⭐")

def update_progress(pet, progress_bar, level_label, root):
    # Calculate total actions (feed + play + sleep)
    total_actions = pet.times_fed + pet.times_played + pet.times_slept

    # Update progress bar
    if total_actions % 3 == 0 and total_actions > 0:
        progress_bar["value"] = 100  # Fill the progress bar
        progress_bar.configure(style="green.Horizontal.TProgressbar")  # Turn green
        pet.level_up()  # Level up the pet
        level_label.config(text=f"Level: {pet.level} ⭐")  # Update level display
        play_sound("sounds/meow.mp3")  # Play "meow" sound effect
        show_kawaii_face(root)  # Show kawaii happy face
        update_leaderboard(pet.name, pet.level)  # Update leaderboard
        progress_bar.after(2000, lambda: reset_progress_bar(progress_bar))  # Reset after 2 seconds
    else:
        progress_bar["value"] = (total_actions % 3) * 33.33  # Increment progress bar

def reset_progress_bar(progress_bar):
    progress_bar["value"] = 0  # Reset progress bar
    progress_bar.configure(style="TProgressbar")  # Revert to default style

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def show_kawaii_face(root):
    kawaii_face = tk.Label(
        root,
        text="(=^･ω･^=)",  # Kawaii cat face
        font=font.Font(family="Comic Sans MS", size=24),
        bg="#FFE4E1",  # Light pink background
        fg="#FF69B4"  # Hot pink text
    )
    kawaii_face.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    kawaii_face.after(2000, kawaii_face.destroy)  # Remove after 2 seconds

def update_leaderboard(name, level):
    with open("data/leaderboard.txt", "a") as file:
        file.write(f"{name}: Level {level}\n")