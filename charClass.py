import random
import json

"""
program to generate a class for 5e dnd character
"""

class Fighter():
    def __init__(self, style, archetype, hp, armor, weapons, saving_throws, skills):
        self.style=style
        self.archetype=archetype
        self.hp=hp
        self.armor=armor
        self.weapons=weapons,
        self.saving_throws=saving_throws
        self.skills=[]

    def genStyle(self):
        styleList=["archery", "defense", "dueling", "great weapon fighting", "protection", "two-weapon fighting"]
        self.style=random.choice(styleList)
        return self
        
    def getArch(self):
        typeList=["champion", "battle master", "eldritch knight"]
        self.archetype=random.choice(typeList)
        return self
        
    def getSkills(self):
        sList=["acrobatics", "animal handling", "athletics", "history", "insight", "intimidation", "perception", "survival"]
        self.skills.append(random.choice(sList))
        sList.remove(self.skills[0])
        self.skills.append(random.choice(sList))
        return self

class Barbarian():
    def __init__(self,path, hp, armor, weapons,saving_throws, skills):
        self.path=path
        self.hp=hp
        self.armor=armor
        self.weapons=weapons
        self.saving_throws=saving_throws
        self.skills=[]
    
    def genPath(self):
        pathList=["beserker", "totem warrior"]
        self.path=random.choice(pathList)
        return self
    
    def getSkills(self):
        sList=["animal handling", "athletics", "intimidation", "nature", "perception", "survival"]
        self.skills.append(random.choice(sList))
        sList.remove(self.skills[0])
        self.skills.append(random.choice(sList))
        return self


class Wizard():
    def __init__(self, college, hp, armor, weapons, cantrips, spells, spell_slots, saving_throws, skills):
        self.college=college
        self.hp=hp
        self.armor=armor
        self.weapons=weapons
        self.cantrips=[]
        self.spells=[]
        self.spell_slots=spell_slots
        self.saving_throws=saving_throws
        self.skills=[]



class Bard():
    def __init__(self, college, hp, armor, weapons, instraments, saving_throws, inspiration, spells, spell_slots):
        self.college=college
        self.hp=hp
        self.armor=armor
        self.weapons=weapons
        self.instraments=[]
        self.saving_throws=saving_throws
        self.inspiration=inspiration
        self.spells=[]
        self.spell_slots=spell_slots
    
    def getCollege(self):
        clist=["lore", "glamour", "satire", "swords", "valor", "whispers"]
        self.college=random.choice(clist)
        return self
    
    def getInstraments(self):
        ilist=["bagpipes", "drum", "dulcimer", "flute", "lute", "lyre", "horn", "pan flute", "shawm", "viol"]
        self.instraments=random.choice(ilist)
        return self

    def getSpells(self):
        with open('spells.json', 'r') as f:
            spell_dict=json.load(f)
        
        for spell in spell_dict:
            print(spell_dict[spell])
        



def makeFighter(f):
    f.genStyle()
    f.getArch()
    f.getSkills()
    return f

def makeBarb(b):
    b.genPath()
    b.getSkills()
    return b


fighter=Fighter('', '', '1d10', 'all,shields', 's,m', 'str,con',"")

made=makeFighter(fighter)

barb=Barbarian('','1d12','l,m,sheilds','s,m','str,con','')
made2=makeBarb(barb)

print("fighter:",made.__dict__)
print("barbarian",made2.__dict__)

bard=Bard('','1d8','','','','','','','')
bard.getSpells()