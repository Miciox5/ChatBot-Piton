import json

from db.import_data_json import import_potions_json, import_ingredients_json


# Caricamento strutture necessarie per l'esecuzione
potions = import_potions_json()
ingredients = import_ingredients_json()

pos_words = ['yes', 'course', 'sure', 'surely', 'do', 'always', 'yeah', 'believe', 'so', 'think']
neg_words = ['no', 'not', 'neither', 'never', 'none', 'nobody', 'nothing', 'nowhere', 'n\'t']
