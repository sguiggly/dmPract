"""
file for parsing a json file of all the spells and storing them into a Spell object
"""
import json
import os
dirname=os.path.dirname(__file__)
filename=os.path.join(dirname, 'spells.json')

def getSpells(file):
    with open(file, encoding="utf8") as f:
            spell_dict=json.load(f)
        
    return spell_dict

shittoprint=getSpells(filename)
for spell in shittoprint:
    print(shittoprint[spell])