# Import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# Import sys
import sys
# Import Database
from utils.Database import Database
# Import Image
from utils.Image import Image
# Import Argument
from utils.Argument import Argument
# Import Json
from utils.Json import Json
# Import Scraper
from utils.Scraper import Scraper

# On initialise la gestion d'argument
argument = Argument(sys.argv)
# On défini notre argument recherche
recherche = argument.recherche()
# On défini notre argument page
pages = argument.nombrePage()


# Ouverture du navigateur Chrome avec le driver 
BASE_URL = f'https://www.google.com/search?q={recherche}&tbm=nws'
try: 
    driver = webdriver.Firefox()
except:
    driver = webdriver.Chrome()
    
driver.get(BASE_URL)

# Récupération du bouton accepter les cookies
cookieBtn = driver.find_element(By.XPATH , '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span')
# Clic sur le bouton accepter les cookies
cookieBtn.click() 

# On initialise la base de données
db = Database()
db.connectDb()
db.createTable()
# On supprime les données de la base de données
# db.truncateTable()

# On initialise scraper
scraper = Scraper()

# On initialise le fichier json
json = Json('google_actualite.json')
# On vide le fichier json
# json.cleanJson()

# Boucle pour récupérer les actualités
def collect_google_actu(page):
    data=[]
    for page in range(1, page+1):
        # Verification de la présence du fichier json
        data = json.getJson()

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
        json.setJson(data)

    # Fermeture de la connexion à la base de données
    db.close()
    
    # Fermeture du navigateur
    driver.close()

collect_google_actu(pages)

# Liste compréhension pour voir sion a compris la compréhension
print([f'{i}' for i in range(10)])