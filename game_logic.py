def update_pet_stats(pet):
    # Gradually decrease stats over time
    pet.hunger += 1  # Reduced from 2 to 1
    pet.happiness -= 1
    pet.energy -= 1

    # Update health based on stats
    if pet.hunger > 80 or pet.happiness < 20 or pet.energy < 20:
        pet.health -= 5  # Reduced from 10 to 5
    else:
        pet.health += 1  # Slowly recover health if stats are good

    # Ensure health stays within bounds
    if pet.health > 100:
        pet.health = 100
    elif pet.health < 0:
        pet.health = 0

def check_pet_health(pet):
    if pet.health <= 0:
        print(f"Oh no! {pet.name} is not feeling well. Take better care of your pet!")
        return True
    return False

def check_achievements(pet):
    achievements = {
        "Fed 10 times": pet.times_fed >= 10,
        "Played 10 times": pet.times_played >= 10,
        "Evolved Pet": pet.level > 1
    }
    for achievement, unlocked in achievements.items():
        if unlocked:
            print(f"Achievement unlocked: {achievement}!")