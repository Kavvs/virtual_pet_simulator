class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100
        self.species = "Cat"  # Changed to Cat
        self.color = "Gray"   # Default cat color
        self.times_fed = 0
        self.times_played = 0
        self.times_slept = 0
        self.level = 1

    def feed(self):
        self.hunger -= 10
        self.health += 5
        self.times_fed += 1
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} has been fed!")

    def play(self):
        self.happiness += 10
        self.energy -= 5
        self.times_played += 1
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name} is happy playing with you!")

    def sleep(self):
        self.energy += 20
        self.hunger += 5
        self.times_slept += 1
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} is sleeping. Zzz...")

    def check_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")
        print(f"Health: {self.health}")
        print(f"Species: {self.species}")
        print(f"Color: {self.color}")
        print(f"Level: {self.level}\n")

    def update_health(self):
        if self.hunger > 80 or self.happiness < 20 or self.energy < 20:
            self.health -= 5  # Reduced from 10 to 5
        else:
            self.health += 1  # Slowly recover health if stats are good

        # Ensure health stays within bounds
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")