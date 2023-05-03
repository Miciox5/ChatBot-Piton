import json

from db.import_data_json import import_potions_json, import_ingredients_json, import_pos_neg_words

# Caricamento strutture necessarie per l'esecuzione
potions = import_potions_json()
ingredients = import_ingredients_json()
pos_words, neg_words = import_pos_neg_words()
