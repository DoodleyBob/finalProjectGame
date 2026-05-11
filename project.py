"""
Game: A Squires Tale - 
A text-based Adventure Game about a small Squire (You) on an adventure to knighthood, will you become a knight, or will you fail trying?
"""
allowed_races = ["Human", "human", "Elf", "elf", "Half-Elf", "Half-elf", "half-elf", "Dwarf", "dwarf", "Teifling", "teifling", "halfling", "dragonborn", "half-orc"]

class MainCharacter:
    def __init__(self, name, race):
        self.name = name
        self.race = race
    def getStats(self):
        while self.race not in allowed_races:
            self.race = input("Please Enter your race - (Human, Elf, Half-Elf, Dwarf, Teifling, Halfling, Dragonborn, Half-Orc): ").lower()
        if self.race == "human":
            self.strength = 10
            self.dexterity = 10
            self.intelligence = 10
            self.endurance = 10
            self.charisma = 12
            self.luck = 12
            self.mp = 10
        elif self.race == "elf":
            self.strength = 10
            self.dexterity = 10
            self.intelligence = 12
            self.endurance = 10
            self.charisma = 10
            self.luck = 10
            self.mp = 12
        elif self.race == "half-elf":
            self.strength = 10
            self.dexterity = 10
            self.intelligence = 10
            self.endurance = 10
            self.charisma = 12
            self.luck = 10
            self.mp = 12
        elif self.race == "dwarf":
            self.strength = 12
            self.dexterity = 10
            self.intelligence = 10
            self.endurance = 12
            self.charisma = 10
            self.luck = 10
            self.mp = 10
        elif self.race == "teifling":
            self.strength = 10
            self.dexterity = 12
            self.intelligence = 12
            self.endurance = 10
            self.charisma = 10
            self.luck = 10
            self.mp = 10
        elif self.race == "halfling":
            self.strength = 10    
            self.dexterity = 12
            self.intelligence = 11
            self.endurance = 10
            self.charisma = 10
            self.luck = 11
            self.mp = 10
        elif self.race == "dragonborn":
            self.strength = 12
            self.dexterity = 10
            self.intelligence = 10
            self.endurance = 10
            self.charisma = 12
            self.luck = 10
            self.mp = 10
        elif self.race == "half-orc":
            self.strength = 12
            self.dexterity = 10
            self.intelligence = 10
            self.endurance = 11
            self.charisma = 10
            self.luck = 10
            self.mp = 11

name = input("Please enter your name: ")
race = input("What is your race? (Human, Elf, Half-Elf, Dwarf, Teifling, Halfling, Dragonborn, Half-Orc): ")
player = MainCharacter(name, race)
player.getStats()
print(f"I am {player.name} the {player.race}, and have {player.mp} mp.")