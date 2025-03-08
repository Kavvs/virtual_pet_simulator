class Shop:
    def __init__(self):
        self.items = {
            "Fish": 10,  # Restores hunger
            "Toy": 20,   # Increases happiness
            "Bed": 50    # Increases energy
        }

    def display_items(self):
        print("Welcome to the shop!")
        for item, price in self.items.items():
            print(f"{item}: {price} coins")

    def buy_item(self, item, pet):
        if item in self.items:
            print(f"You bought {item} for {self.items[item]} coins!")
            if item == "Fish":
                pet.hunger -= 20
            elif item == "Toy":
                pet.happiness += 20
            elif item == "Bed":
                pet.energy += 20
        else:
            print("Item not found!")