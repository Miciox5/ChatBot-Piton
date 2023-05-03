import json
import os


def to_lowercase(data):
    if isinstance(data, dict):
        return {to_lowercase(k): to_lowercase(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [to_lowercase(i) for i in data]
    elif isinstance(data, str):
        return data.lower()
    else:
        return data


def import_potions_json():
    # ottieni il percorso assoluto della directory corrente
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # costruisci il percorso relativo del file "potions.json"
    potions_file = os.path.join(current_dir, ".", "potions.json")

    # carica i dati dal file "potions.json"
    with open(potions_file) as f_p:
        ps = json.load(f_p)

    ps = to_lowercase(ps)

    return ps


def import_ingredients_json():
    # ottieni il percorso assoluto della directory corrente
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # costruisci il percorso relativo del file "ingredients.json"
    potions_file = os.path.join(current_dir, ".", "ingredients.json")

    # carica i dati dal file "ingredients.json"
    with open(potions_file) as f_i:
        ings = json.load(f_i)

    ings = to_lowercase(ings['ingredients'])
    # print(ings)
    return ings


def import_pos_neg_words():
    # ottieni il percorso assoluto della directory corrente
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # costruisci il percorso relativo del file "pos_neg_words.json"
    all_w_file = os.path.join(current_dir, ".", "pos_neg_words.json")

    # carica i dati dal file "ingredients.json"
    with open(all_w_file) as f_a:
        all_words = json.load(f_a)

    all_words = to_lowercase(all_words)

    pos_w, neg_w = all_words['positive_words'], all_words['negative_words']

    return pos_w, neg_w


def get_ingredients_potion_json(name_potion):
    potions = json.load(open("potions.json"))
    potion = potions[name_potion]
    return potion


def get_all_potions():
    potions_list = list(json.load(open("potions.json")).keys())
    return potions_list

# print(get_ingredients_potion_json('Amortentia'))

## Risposte corrette pozioni:
# Oblivious: drops of lete river water,mistletoe berries,valerian roots,scoops of basic ingredient
# Ageing: newt spleens, bananas, an orange snake, a green leaf
# amortentia: moon water, ashwinder's egg, rose petal, hot pepper powder
#