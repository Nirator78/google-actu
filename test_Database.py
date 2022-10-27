from utils.Database import Database

db = Database()
db.connectDb()
db.createTable()

db.addImage('link')

db.addArticle({
    'nomSource' : 'nomSource',
    'titre' : 'titre',
    'description' : 'description',
    'image' : 1,
    'date' : 'date',
    'lien' : 'lien',
})

print(db.findImage('link'))

db.updateImage(1, 'link2')

print(db.findImage('link2'))

print(db.listArticleJoinImage())

db.close()