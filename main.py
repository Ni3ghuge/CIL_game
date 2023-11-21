from animal import Animal
from gun import Gun
from player import Player
import time
import random
class Game:
    def __init__(self):
        self.guns = [Gun("Pistol", 30), Gun("Shotgun", 40), Gun("Sniper", 50),Gun("Rifel",100)]
        self.animals = [
            Animal("Rabbit", 5),
            Animal("Deer", 10),
            Animal("Bear", 20),
            Animal("Wolf", 15),
            Animal("Fox", 8)
        ]
        self.player = None

    def print_options(self, options, category):
        print(f"\nChoose a {category}:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option.name} - Power: {option.power}")

    def shoot_animal(self, gun, animal):
        print(f"\nAiming at the {animal.name} with {gun.name} (Power: {gun.power})...")
        time.sleep(2)
        shot_power = random.randint(1, 10)
        if shot_power <= gun.power:
            print(f"You shot the {animal.name} successfully!")
            self.player.points += animal.points
        else:
            print(f"You missed the {animal.name}!")

    def display_player_info(self):
        print(f"\nPlayer: {self.player.name}")
        print(f"Total Points: {self.player.points}\n")

    def play_game(self):
        player_name = input("Enter your name: ")
        self.player = Player(player_name)

        print("Welcome to the Animal Shooting Game!")

        while True:
            self.print_options(self.guns, "gun")
            selected_gun = input("Enter the number of the gun of your choice: ")
            
            if selected_gun.isdigit() and 1 <= int(selected_gun) <= len(self.guns):
                break
            else:
                print("Invalid input. Please enter a valid number.")

        selected_gun = self.guns[int(selected_gun) - 1]

        rounds = 5
        print("\nGet ready!")
        time.sleep(1)
        print("Game starts now!\n")

        try:
            for _ in range(rounds):
                animal = random.choice(self.animals)
                self.shoot_animal(selected_gun, animal)
                self.display_player_info()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            self.display_player_info()

        print(f"\nGame over, {self.player.name}! Your total points: {self.player.points}")

if __name__ == "__main__":
    game = Game()
    game.play_game()