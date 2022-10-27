"""
Test de la classe Json
"""
from utils.Json import Json

# On initiliase la classe Json
json = Json('test.json')

# On récupère le contenu du fichier
print(json.getJson())

# On insert un contenu dans le fichier
json.setJson([{'test': 'test'}])

# On récupère le contenu du fichier
print(json.getJson())

# On supprime le contenu du fichier
json.cleanJson()

# On récupère le contenu du fichier
print(json.getJson())