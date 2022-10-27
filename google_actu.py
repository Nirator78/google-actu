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

from utils.Scraper import Scraper

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

# On initialise scraper
scraper = Scraper()

# Boucle pour récupérer les actualités
def collect_google_actu(page):
    data=[]
    for page in range(1, page+1):
        # Verification de la présence du fichier json
        try:
            with open('google_actualite.json') as f:
                data = json.load(f)
        except:
            pass

        if(page > 1):
            driver.find_elements(By.CLASS_NAME, 'fl')[page-2].click()

        # Récupération des actualités
        articles = driver.find_elements(By.CLASS_NAME, 'SoaBEf')

        # Boucle pour récupérer les actualités
        for article in articles:
            dataFormated  = scraper.getData(article)
            # On ajoute l'image dans la base de données avec un lien temporaire
            db.addImage('inprogress')
            # On récupère l'id de l'image
            idImage = db.findImage('inprogress')['id']
            # On télécharge l'image en la sauvegardant avec son id
            Image.saveImage(dataFormated["image"], idImage)

            # On met à jour le lien de l'image dans la base de données
            db.updateImage(idImage, 'images/' + str(idImage) + '.png')

            dataFormated["image"] = idImage

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