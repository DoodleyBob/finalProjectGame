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

    def move(self, direction):
        if direction in self.current_location.exits:
            self.current_location = self.current_location.exits[direction]
            print(f"You travel {direction} to {self.current_location.name}")
        else:
            print("You can't go {direction} from here!")

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def __str__(self):
        return self.name
    
    def set_exit(self, direction, neighbor):
        self.exits[direction] = neighbor



name = input("Please enter your name: ")
race = input("What is your race? (Human, Elf, Half-Elf, Dwarf, Teifling, Halfling, Dragonborn, Half-Orc): ").lower()

# Create Locations

grantville = Location("Grantville", "A small and peaceful town with a calm atmosphere, also your hometown.")
forest_M = Location("Forest of Mist", "A dark forest filled with dead trees and no nearby life, the atmosphere is thick with fog, making it difficult to tell what direction you are heading in.")
cave = Location("Random Cave", "You head venture east for whatever reason, and you stumble across a cave.")

# Final Location
dark_mages_castle = Location("Dark Mages Castle", "You enter the grimm castle where your objective lies, the Dark Mage, the most powerful being in the kingdom, will you defeat him and bring peace to the region?")
        
grantville.set_exit("north", forest_M) # Section 1
grantville.set_exit("east", cave) # Section 1
forest_M.set_exit("south", grantville) # Section 1
cave.set_exit("west", grantville) # Section 1


player = MainCharacter(name, race, grantville)
player.getStats()

# Story
print(f"I am {player.name} the {player.race}, and have {player.mp} mp.")
print(f"Location: {player.current_location}")

while player.current_location != dark_mages_castle:
    ui = input("What direction would you like to head in? (North, South, East, or West) ").lower()
    if ui == "north":
        player.move("north")
    elif ui == "south":
        player.move("south")
    elif ui == "east":
        player.move("east")
    elif ui == "west":
        player.move("west")
    print(f"Location: {player.current_location}")