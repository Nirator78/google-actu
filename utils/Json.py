import json

"""
Class json permettant de gérer les fichiers json
"""
class Json:
    # On défini un nom de pour la gestion du fichier json
    def __init__(self, jsonName):
        self.jsonName = jsonName

    # On récupère le contenu du fichier json, si le fichier n'existe pas, on renvoie un tableau vide
    def getJson(self):
        try:
            with open(self.jsonName, 'r') as jsonFile:
                return json.load(jsonFile)
        except:
            print("Erreur lors de la lecture du fichier " + self.jsonName)
            return []

    # On sauvegarde un tableau dans le fichier json
    def setJson(self, data):
        try:
            with open(self.jsonName, 'w') as jsonFile:
                json.dump(data, jsonFile, indent=4)
        except:
            print("Erreur lors de l'écriture dans le fichier " + self.jsonName)

    # On vide le fichier json
    def cleanJson(self):
        self.setJson([])
