from binascii import a2b_base64

"""
Class Image permettant de gérer les images
"""
class Image:

    # Sauvegarde d'une image en base-uri dans le dossier images
    def saveImage(data, nom):
        try:
            data = data.split(",")[1]

            binary_data = a2b_base64(data)
            with open('images/' + str(nom) + '.png', 'wb') as fd:
                fd.write(binary_data)
        except:
            print("Erreur lors de la sauvegarde de l'image " + str(nom))