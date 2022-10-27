import mysql.connector as mc

class Database:
    def __init__(self):
        self.connection = mc.connect(
            host="localhost",
            user="root",
            password="Azerty94",
            database='webscraping'
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def connectDb(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS webscraping")

    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `webscraping`.`article_google` (`id` INT NOT NULL AUTO_INCREMENT,`nomSource` VARCHAR(45) NULL, `titre` VARCHAR(255) NULL, `description` TEXT(1000) NULL, `image` INT NULL, `date` VARCHAR(45) NULL, `lien` VARCHAR(255) NULL, PRIMARY KEY (`id`));")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `webscraping`.`image_google` ( `id` INT NOT NULL AUTO_INCREMENT, `link` VARCHAR(255) NULL, PRIMARY KEY (`id`));")

    def addArticle(self, item):
        sql = "INSERT INTO article_google (nomSource, titre, description, image, date, lien) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (item['nomSource'], item['titre'], item['description'], item['image'], item['date'], item['lien'])
        self.cursor.execute(sql, val)
        self.connection.commit()

    def addImage(self, link):
        sql = "INSERT INTO image_google (link) VALUES ('" + link + "')"
        self.cursor.execute(sql)
        self.connection.commit()

    def updateImage(self, id, link):
        sql = "UPDATE image_google SET link = '" + link + "' WHERE id = " + str(id)
        self.cursor.execute(sql)
        self.connection.commit()
    
    def findImage(self, link):
        sql = "SELECT * FROM image_google WHERE link = '" + link + "' LIMIT 1"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def listArticleJoinImage(self):
        sql = "SELECT * FROM article_google LEFT JOIN image_google ON article_google.image = image_google.id"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()