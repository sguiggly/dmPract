"""
A simple D&d 5e characters generation for generating stats, race, and class for a 5e character.
"""
import random

class Race:
    def __init__(self, name, size, speed, darkvision, subrace):
        self.name=name
        self.size=size
        self.speed=speed
        self.darkvision=darkvision
        self.subrace=subrace

    def raceInfo(self):
        return self

def genRace(race):
    return random.choice(race)

def genSubRace(race):
    if race.name == "dragonborn":
        subrace=["black","red","blue","green","white","copper","bronze","copper","silver","gold"]
        race.subrace=random.choice(subrace)
        return race
    elif race.name == "elf":
        subrace=["highelf", "woodelf"]
        race.subrace=random.choice(subrace)
        return race
    elif race.name == "dwarf":
        subrace=["hill","mountain"]
        race.subrace=random.choice(subrace)
        return race
    elif race.name == "halfling":
        subrace=["lightfoot","stout"]
        race.subrace=random.choice(subrace)
        return race
    elif race.name == "gnome":
        subrace=["forest","rock"]
        race.subrace=random.choice(subrace)
        return race
    else:
        return race

races = []

races.append(Race("human", "m", 30, 0, ""))
races.append(Race("tiefling", "m", 30, 1, ""))
races.append(Race("halfling", 's', 25, 0, ""))
races.append(Race("dwarf", 'm', 25, 1, ""))
races.append(Race("elf", 'm', 30, 1, ""))
races.append(Race("halforc", 'm', 30, 1, ""))
races.append(Race("halfelf", 'm', 30, 1, ""))
races.append(Race("gnome", 's', 25, 1, ""))
races.append(Race("dragonborn", 'm', 30, 0, ""))

mainRace=genRace(races)
raceSelection=genSubRace(mainRace)
print(raceSelection.__dict__)