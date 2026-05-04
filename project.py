"""
Game: A Squires Tale - 
A text-based Adventure Game about a small Squire (You) on an adventure to knighthood, will you become a knight, or will you fail trying?
"""
allowed_species = ["Human", "human", "Elf", "elf", "Half-Elf", "Half-elf", "half-elf", "Dwarf", "dwarf", "Teifling", "teifling", "Halfling", "halfling", "Dragonborn", "dragonborn", "Half-Orc", "Half-orc", "half-orc"]

class MainCharacter:
    def __init__(self):
        self.name = name
        self.age = age
        self.species = species
    def getStats(self):
        while self.species not in allowed_species:
            self.species = input("Enter your race - (Human, Elf, Half-Elf, Dwarf, Teifling, Halfling, Dragonborn, Half-Orc): ")
            if self.species == "Human" or self.species == "human":
                strength = 10
                dexterity = 10
                intelligence = 10
                endurance = 10
                charisma = 12
                luck = 12
                mp = 10
            elif self.species == "Elf" or self.species == "elf":
                strength = 10
                dexterity = 10
                intelligence = 12
                endurance = 10
                charisma = 10
                luck = 10
                mp = 12
            elif self.species == "Half-Elf" or self.species == "Half-elf" or self.species == "half-elf":
                strength = 10
                dexterity = 10
                intelligence = 10
                endurance = 10
                charisma = 12
                luck = 10
                mp = 12
            elif self.species == "Dwarf" or self.species == "dwarf":
                strength = 12
                dexterity = 10
                intelligence = 10
                endurance = 12
                charisma = 10
                luck = 10
                mp = 10
            elif self.species == "Teifling" or self.species == "teifling":
                strength = 10
                dexterity = 12
                intelligence = 12
                endurance = 10
                charisma = 10
                luck = 10
                mp = 10
            elif self.species == "Halfling" or self.species == "halfling":
                strength = 10    
                dexterity = 12
                intelligence = 11
                endurance = 10
                charisma = 10
                luck = 11
                mp = 10
            elif self.species == "Dragonborn" or self.species == "dragonborn":
                strength = 12
                dexterity = 10
                intelligence = 10
                endurance = 10
                charisma = 12
                luck = 10
                mp = 10
            elif self.species == "Half-Orc" or self.species == "Half-orc" or self.species == "half-orc":
                strength = 12
                dexterity = 10
                intelligence = 10
                endurance = 11
                charisma = 10
                luck = 10
                mp = 11
            else:
                self.species = input("That race does not exist, please re-input a race out of the races provided - (Human, Elf, Half-Elf, Dwarf, Teifling, Halfling, Dragonborn, Half-Orc): ")


