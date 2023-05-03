# potions = {
#     "polyjuice": ['fluxweed', 'knotgrass', 'lacewing flies', 'leeches', 'horn of bicorn', 'boomslang skin', 'hair'],
#     "armadillo bile mixture": ['bat wings', 'armadillo bile', 'wormwood', 'amorentia', 'acromantula venom',
#                                'aconite', 'water'],
#     "animagus": ['mandrake leaf', 'hair', 'dew', 'death\'s-head hawk chrysalis']}
#
# ingredients = ['fluxweed', 'knotgrass', 'lacewing flies', 'leeches', 'horn of bicorn', 'boomslang skin',
#                'a piece of the person you are turning into', 'hair', 'nail', 'skin', 'bat wings', 'armadillo bile',
#                'wormwood', 'amorentia', 'acromantula venom', 'aconite', 'water', 'mandrake leaf', 'drinker\'s hair',
#                'dew', 'death\'s-head hawk chrysalis', 'newt spleens', 'bananas', 'an orange snake', 'a green leaf',
#                'angel\'s Trumpet', 'valerian sprigs', 'dittany', 'baneberry', 'cheese', 'death- cap', 'pumpkin juice',
#                'unicorn horn', 'caterpillars', 'orange juice', 'extract of gurdyroot', 'dragon dung',
#                'salamander blood', ' flobberworm mucus']
#
# pos_words = ['yes', 'course', 'sure', 'surely', 'do', 'always', 'yeah', 'believe', 'so', 'think']
# neg_words = ['no', 'not', 'neither', 'never', 'none', 'nobody', 'nothing', 'nowhere', 'n\'t']
from db.import_data_json import import_potions_json, import_ingredients_json, import_pos_neg_words

potions = import_potions_json()
ingredients = import_ingredients_json()

pos_words, neg_words = import_pos_neg_words()


