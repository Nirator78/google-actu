# Import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# Import Json
import json
# Import sys
import sys
# Import Database
from utils.Database import Database
# Import Image
from utils.Image import Image

try :
    recherche = str(sys.argv[1])
except:
    recherche = 'actualite'
try :
    pages = int(sys.argv[2])
except:
    pages = 1

# Ouverture du navigateur Chrome avec le driver 
BASE_URL = f'https://www.google.com/search?q={recherche}&tbm=nws'
driver = webdriver.Firefox()
driver.get(BASE_URL)

# Récupération du bouton accepter les cookies
cookieBtn = driver.find_element(By.XPATH , '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span')
# Clic sur le bouton accepter les cookies
cookieBtn.click() 

# On initialise la base de données
db = Database()
db.connectDb()
db.createTable()
db.truncateTable()

# Boucle pour récupérer les actualités
def collect_google_actu(page):
    data=[]
    for page in range(1, page+1):
        # Verification de la présence du fichier json
        if(page > 1):
            driver.find_elements(By.CLASS_NAME, 'fl')[page-2].click()

        # Récupération des actualités
        articles = driver.find_elements(By.CLASS_NAME, 'SoaBEf')

        # Boucle pour récupérer les actualités
        for article in articles:
            try:
                nomSource = article.find_element(By.CLASS_NAME, 'CEMjEf.NUnG9d').text
            except:
                nomSource = None
            try:
                titre = article.find_element(By.CLASS_NAME, 'mCBkyc.y355M.ynAwRc.MBeuO.jBgGLd.OSrXXb').text
            except:
                titre = None
            try:
                decription = article.find_element(By.CLASS_NAME, 'GI74Re.jBgGLd.OSrXXb').text
            except:
                decription = None
            try:
                image = article.find_element(By.TAG_NAME, 'img').get_attribute('src')
            except:
                image = None
            try:
                date = article.find_element(By.CLASS_NAME, 'OSrXXb.ZE0LJd.YsWzw').text
            except:
                date = None
            try:
                lien = article.find_element(By.CLASS_NAME, 'WlydOe').get_attribute('href')
            except:
                lien = None

            # On ajoute l'image dans la base de données avec un lien temporaire
            db.addImage('inprogress')
            # On récupère l'id de l'image
            idImage = db.findImage('inprogress')
            # On télécharge l'image en la sauvegardant avec son id
            Image.saveImage(image, idImage[0])

            # On met à jour le lien de l'image dans la base de données
            db.updateImage(idImage[0], 'images/' + str(idImage[0]) + '.png')

            dataFormated = {
                'nomSource' : nomSource,
                'titre' : titre,
                'description' : decription,
                'image' : idImage[0],
                'date' : date,
                'lien' : lien,
            }

            # On ajoute l'image dans la base de données avec un lien temporaire
            db.addImage('inprogress')
            # On récupère l'id de l'image
            idImage = db.findImage('inprogress')['id']
            # On télécharge l'image en la sauvegardant avec son id
            Image.saveImage(image, idImage)

            # On met à jour le lien de l'image dans la base de données
            db.updateImage(idImage, 'images/' + str(idImage) + '.png')

            dataFormated = {
                'nomSource' : nomSource,
                'titre' : titre,
                'description' : decription,
                'image' : idImage,
                'date' : date,
                'lien' : lien,
            }

            # On ajoute l'article dans la base de données
            db.addArticle(dataFormated)

            # On ajoute l'article dans le fichier json
            data.append(dataFormated)

            # Ecriture dans le fichier json
            with open('google_actualite.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

    # Fermeture de la connexion à la base de données
    db.close()
    
    # Fermeture du navigateur
    driver.close()

collect_google_actu(pages)