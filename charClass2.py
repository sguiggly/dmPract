import random
import json
import os

class Classes():
    def __init__(self, subclass, hp, armor, weapons, saving_throws, skills):
        self.subclass=subclass
        self.hp=hp
        self.armor=armor
        self.weapons=weapons
        self.saving_throws=saving_throws
        self.skills=[]

    def getSub(self, subList):
        self.subclass=random.choice(subList)
        return self
    
    def getSkills(self, sList):
        self.skills.append(random.choice(sList))
        sList.remove(self.skills[0])
        self.skills.append(random.choice(sList))
        return self

class Fighter(Classes):
    def __init__(self, subclass, hp, armor, weapons, saving_throws, skills, style):
        Classes.__init__(self, subclass, hp, armor, weapons, saving_throws, skills)
        self.style=style

    def genStyle(self):
        styleList=["archery", "defense", "dueling", "great weapon fighting", "protection", "two-weapon fighting"]
        self.style=random.choice(styleList)
        return self

def makeFighter(f,sList,subList):
    f.genStyle()
    f.getSkills(sList)
    f.getSub(subList)
    return f

fighter=Fighter('', '1d10', 'all,shields', 's,m', 'str,con',"",'')
fSkills=["acrobatics", "animal handling", "athletics", "history", "insight", "intimidation", "perception", "survival"]
archList=["champion", "battle master", "eldritch knight"]
madeFighter=makeFighter(fighter, fSkills, archList)

print("fighter:",madeFighter.__dict__)