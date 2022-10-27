# GOOGLE ACTUALITE
## Lien Github : https://github.com/Nirator78/google-actu/
## Framework
- Selenium
## Prérequis
- Avoir une base de données
- Avoir mysql connector
- Avoir Python
- Avoir Selenium avec le driver de Firefox ou Google Chrome

### Connexion a la base de données
- Modifier les informations de connexion dans le fichier Database.py
```
host="localhost",
user="root",
password=""
```
### Lancer le programme 
Executer si on veux les valeurs par defaut
Page 3 et actualité en recherche
```
py .\app.py
```
Avec des arguments
```
py .\app.py rechercheVoulu nombreDePages
```
Exemple
```
py .\app.py crypto 5
```
