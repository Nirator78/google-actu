# Import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Import Json
import json
# Import sys
import sys

# Verification numero de page

def verif_page(page):
    # si page 1 on met 0
    if page == 1:
        return str(page-1)
    # si page 1 on met 0
    else:
        return str(page-1)+'0'
    
page = verif_page(int(sys.argv[2]))

# Ouverture du navigateur Chrome avec le driver 
BASE_URL = f'https://www.google.com/search?q={str(sys.argv[1])}&tbm=nws&start={page}'
driver = webdriver.Firefox()
driver.get(BASE_URL)

# Récupération du bouton accepter les cookies
cookieBtn = driver.find_element(By.XPATH , '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span')
# Clic sur le bouton accepter les cookies
cookieBtn.click()

# Boucle pour récupérer les actualités
def collect_google_actu():
    data=[]
    # Verification de la présence du fichier json
    try:
        with open('google_actualite.json') as f:
            data = json.load(f)
    except:
        pass
    # Récupération des actualités
    articles = driver.find_elements(By.CLASS_NAME, 'vJOb1e.aIfcHf.Hw13jc')

    # Boucle pour récupérer les actualités
    for i in range(len(articles)):
        try:
            nomSource = articles[i].find_element(By.CLASS_NAME, 'CEMjEf.NUnG9d').text
        except:
            nomSource = None
        try:
            titre = articles[i].find_element(By.CLASS_NAME, 'mCBkyc.y355M.ynAwRc.MBeuO.nDgy9d').text
        except:
            titre = None
        try:
            decription = articles[i].find_element(By.CLASS_NAME, 'GI74Re.nDgy9d').text
        except:
            decription = None
        try:
            image = articles[i].find_element(By.TAG_NAME, 'img').get_attribute('src')
        except:
            image = None
        try:
            date = articles[i].find_element(By.CLASS_NAME, 'OSrXXb.ZE0LJd.YsWzw').text
        except:
            date = None
        try:
            lien = articles[i].find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/a').get_attribute('href')
        except:
            lien = None
        data.append({
            'nomSource': nomSource, 
            'titre': titre, 
            'decription': decription, 
            'image': image,
            'date': date,
            'lien': lien
        })

    # Ecriture dans le fichier json
    with open('google_actualite.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    driver.close()

collect_google_actu()