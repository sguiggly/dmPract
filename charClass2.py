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

class Barbarian(Classes):
    def __init__(self, subclass, hp, armor, weapons, saving_throws, skills):
        Classes.__init__(self, subclass, hp, armor, weapons, saving_throws, skills)

def makeFighter(f,sList,subList):
    f.genStyle()
    f.getSkills(sList)
    f.getSub(subList)
    return f

def makeBarb(b,sList,subList):
    b.getSkills(sList)
    b.getSub(subList)
    return b

fighter=Fighter('', '1d10', 'all,shields', 's,m', 'str,con',"",'')
fSkills=["acrobatics", "animal handling", "athletics", "history", "insight", "intimidation", "perception", "survival"]
archList=["champion", "battle master", "eldritch knight"]
madeFighter=makeFighter(fighter, fSkills, archList)

barbarian=Barbarian('','1d12','l,m,sheilds','s,m','str,con','')
barbSkills=["animal handling","athletics","intimidation","nature","perception","survival"]
pathList=["path of the beserker", "path of the totem warrior"]
madeBarb=makeBarb(barbarian,barbSkills,pathList)

print("fighter:",madeFighter.__dict__)
print("barbarian:",madeBarb.__dict__)