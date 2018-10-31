"""
file for parsing a json file of all the spells and storing them into a Spell object
"""
import json

class Spells():
    def __init__(self, name, casting_time, componets, description, duration, level, spell_range, school):
        self.name=name
        self.casting_time=casting_time
        self.componets=componets
        self.description=description
        self.duration=duration
        self.level=level
        self.spell_range=spell_range
        self.school=school



def getSpells(file, slist):
    with open(file, 'r') as f:
        spell_dict=json.load(f)