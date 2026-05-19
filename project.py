"""
Game: A Squires Tale - 
A text-based Adventure Game about a small Squire (You) on an adventure to knighthood, will you become a knight, or will you fail trying?
"""
allowed_races = ["human", "elf", "half-elf", "dwarf", "teifling", "halfling", "dragonborn", "half-orc"]

class MainCharacter:
    def __init__(self, name, race, starting_location):
        self.name = name
        self.race = race.lower()
        self.current_location = starting_location
        self.inventory = []
        # Creating placeholder stats
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.endurance = 0
        self.charismma = 0
        self.luck = 0
        self.mp = 0 
    

    def getStats(self):
        while self.race not in allowed_races:   #  <- Validation Loop
            self.race = input("That race does not exist! Please enter a valid race: ").lower()
            
        # Stat Assignment    
        race_stats = {
            "human": {"str": 10, "dex": 10, "int": 10, "end": 10, "cha": 12, "luck": 12, "mp": 10},
            "elf": {"str": 10, "dex": 10, "int": 12, "end": 10, "cha": 10, "luck": 10, "mp": 12},
            "half-elf": {"str": 10, "dex": 10, "int": 10, "end": 10, "cha": 12, "luck": 10, "mp": 12},
            "dwarf": {"str": 12, "dex": 10, "int": 10, "end": 12, "cha": 10, "luck": 10, "mp": 10},
            "teifling": {"str": 10, "dex": 12, "int": 12, "end": 10, "cha": 10, "luck": 10, "mp": 10},
            "halfling": {"str": 10, "dex": 12, "int": 11, "end": 10, "cha": 10, "luck": 11, "mp": 10},
            "dragonborn": {"str": 12, "dex": 10, "int": 10, "end": 10, "cha": 12, "luck": 10, "mp": 10},
            "half-orc": {"str": 12, "dex": 10, "int": 10, "end": 11, "cha": 10, "luck": 10, "mp": 11}
        }

        stats = race_stats[self.race]
        self.strength = stats["str"]
        self.dexterity = stats["dex"]
        self.intelligence = stats["int"]
        self.endurance = stats["end"]
        self.charisma = stats["cha"]
        self.luck = stats["luck"]
        self.mp = stats["mp"]

    def gather_item(self):
        current_loc = self.current_location
        if current_loc.items:
            print(f"\nYou found these items:")
            for idx, item in enumerate(current_loc.items):
                print(f"{idx + 1}. {item}")

            choice = input("What items do you want to pick up? (Type the item name or type 'cancel'): ").strip()
            if choice in current_loc.items:
                self.inventory.append(choice)
                current_loc.items.remove(choice)
                print(f"You picked up the {choice}.")
            elif choice.lower() == "cancel":
                print("You leave the items.")
            else:
                print("That item isn't here.")
        else:
            print("\nThere is nothing here")

    def talk_to_npc(self):
        current_loc = self.current_location
        if current_loc.npcs:
            print("There are these people here:")
            for npc in current_loc.npcs:
                print(f"- {npc}")

            choice = input("Who do you want to talk to? ").strip()
            if choice in current_loc.npcs:
                print(f"\n[{choice}]: '{current_loc.npcs[choice]}'")
            else:
                print("They are not here currently.")
        else:
            print("\nThere seems to be no one to talk to.")


    def move(self, direction):
        if direction in self.current_location.exits:
            self.current_location = self.current_location.exits[direction]
            print(f"You travel {direction} to {self.current_location.name}")
            print(f"{self.current_location.description}")
        else:
            print(f"You can't go {direction} from here!")

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.npcs = {}

    def __str__(self):
        return self.name
    
    def set_exit(self, direction, neighbor):
        self.exits[direction] = neighbor



name = input("Please enter your name: ")
race = input("What is your race? (Human, Elf, Half-Elf, Dwarf, Teifling, Halfling, Dragonborn, Half-Orc): ").lower()

# Setting up Locations, NPCs, and items

grantville = Location("Grantville", "A small and peaceful town with a calm atmosphere, also your hometown.")
grantville.items.append("healing potion")
grantville.npcs["Old Man Jenkins"] = "AAAAAAAHHHHHHHH!!!!"


forest_M1 = Location("Forest of Mist", "A dark forest filled with dead trees and no nearby life, the atmosphere is thick with fog, making it difficult to tell what direction you are heading in.")
forest_M1.items.append("wooden stick")

forest_M2 = Location("Forest of Mist", "You find yourself still in the forest unsure of where to continue.")
forest_M3E = Location("Forest of Mist", "You are still in the Forest of Mist, but in the mist you see a glimmer of light up north.")
forest_M3W = Location("Forest of Mist", "You are still in the forest of mist...")
cave = Location("Random Cave", "You head venture east for whatever reason, and you stumble across a cave.")

# Final Location
dark_mages_tower = Location("Dark Mage's Tower", "You enter the grimm tower, the walls made of obsidian going up to the clouds themselves, shelves filled up with books of dark magic and alchemy, and the smell of blood from the previous adventurers who dared to challenge the Evil Mage fills the air. ")

# Setting Exits (Moving between locations)

# Grantville
grantville.set_exit("north", forest_M1) # Section 1
grantville.set_exit("east", cave) # Section 1
# Forest of Mist
forest_M1.set_exit("south", grantville) # Section 1
forest_M1.set_exit("north", forest_M2)
forest_M2.set_exit("south", forest_M1)
forest_M2.set_exit("east", forest_M3E)
forest_M2.set_exit("west", forest_M3W)
forest_M3W.set_exit("east", forest_M2)
forest_M3E.set_exit("west", forest_M2)

# Mysterious cave
cave.set_exit("west", grantville) # Section 1


player = MainCharacter(name, race, grantville)
player.getStats()

# Story
print(f"I am {player.name} the {player.race}, and have {player.mp} mp.")
print(f"Location: {player.current_location}")

while player.current_location != dark_mages_tower:
    # Presenting Options
    print(f"\n-- Location: {player.current_location.name} --")
    action = input("What would you like to do? (move, look, gather, talk, inventory): ").lower().strip()

    if action == "move":
        direction = input("What direction would you like to head in? (North, South, East, or West), or type 'location' to look around.\n ").lower()
        player.move(direction)
    elif action == "look":
        print(f"\n{player.current_location.description}")
        if player.current_location.items:
            print(f"Items on ground: {', '.join(player.current_location.items)}")
        if player.current_location.npcs:
            print(f"People here: {', '.join(player.current_location.npcs.keys())}")
    elif action == "gather":
        player.gather_item()
    elif action == "talk":
        player.talk_to_npc()
    elif action == "inventory":
        print(f"\nYour Inventory: {player.inventory if player.inventory else 'Empty'}")

    else:
        print("Invalid command.")

    print(f"Location: {player.current_location}")