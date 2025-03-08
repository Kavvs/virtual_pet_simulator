import json
import pygame

def save_pet(pet, filename):
    with open(filename, "w") as file:
        json.dump(pet.__dict__, file)

def load_pet(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        pet = VirtualPet(data["name"])
        pet.__dict__.update(data)
        return pet

def play_sound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def update_leaderboard(name, score):
    with open("data/leaderboard.txt", "a") as file:
        file.write(f"{name}: {score}\n")