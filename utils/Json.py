import json

class Json:
    def __init__(self, jsonName):
        self.jsonName = jsonName

    def getJson(self):
        try:
            with open(self.jsonName, 'r') as jsonFile:
                return json.load(jsonFile)
        except:
            print("Erreur lors de la lecture du fichier " + self.jsonName)
            return []

    def setJson(self, data):
        try:
            with open(self.jsonName, 'w') as jsonFile:
                json.dump(data, jsonFile, indent=4)
        except:
            print("Erreur lors de l'écriture dans le fichier " + self.jsonName)