from pet import VirtualPet
from ui import create_gui

def main():
    pet_name = input("What would you like to name your pet? ")
    pet = VirtualPet(pet_name)
    create_gui(pet)

if __name__ == "__main__":
    main()