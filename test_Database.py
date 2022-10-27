"""
Test de la classe Database
"""
from utils.Database import Database

# On initialise la classe Database
db = Database()

# On se connecte à la base de données
db.connectDb()
# On crée la table si elle n'existe pas
db.createTable()

# On ajoute une image
db.addImage('link')

# On ajoute un article
db.addArticle({
    'nomSource' : 'nomSource',
    'titre' : 'titre',
    'description' : 'description',
    'image' : 1,
    'date' : 'date',
    'lien' : 'lien',
})


print(db.findImage('link'))

# On met à jour l'image de l'article
db.updateImage(1, 'link2')

# On recupère l'image
print(db.findImage('link2'))

# On recupère les articles avec les images associées
print(db.listArticleJoinImage())

# On ferme la connexion à la base de données
db.close()