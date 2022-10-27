from binascii import a2b_base64

class Image:

    def saveImage(data, nom):
        data = data.split(",")[1]

        binary_data = a2b_base64(data)
        with open('images/' + str(nom) + '.png', 'wb') as fd:
            fd.write(binary_data)