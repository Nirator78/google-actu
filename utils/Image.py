from binascii import a2b_base64
import os

"""
Class Image permettant de gérer les images
"""
class Image:
    # On créer un dossier images s'il n'existe pas
    def __init__(self):
        if not os.path.exists('images'):
            os.makedirs('images')

    # Sauvegarde d'une image en base-uri dans le dossier images
    def saveImage(self, data, nom):
        try:
            data = data.split(",")[1]

            binary_data = a2b_base64(data)
            with open('images/' + str(nom) + '.png', 'wb') as fd:
                fd.write(binary_data)
        except:
            print("Erreur lors de la sauvegarde de l'image " + str(nom))