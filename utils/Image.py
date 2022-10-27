from binascii import a2b_base64

class Image:

    def saveImage(data, nom):
        try:
            data = data.split(",")[1]

            binary_data = a2b_base64(data)
            with open('images/' + str(nom) + '.png', 'wb') as fd:
                fd.write(binary_data)
        except:
            print("Erreur lors de la sauvegarde de l'image " + str(nom))