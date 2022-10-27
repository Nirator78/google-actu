import mysql.connector as mc

class Database:
    def __init__(self):
        self.connection = mc.connect(
            host="localhost",
            user="root",
            password="",
            database='webscraping'
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def connectDb(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS webscraping")

    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `webscraping`.`article_google` (`id` INT NOT NULL AUTO_INCREMENT,`nomSource` VARCHAR(45) NULL, `titre` VARCHAR(255) NULL, `description` TEXT(1000) NULL, `image` INT NULL, `date` VARCHAR(45) NULL, `lien` VARCHAR(255) NULL, PRIMARY KEY (`id`));")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `webscraping`.`image_google` ( `id` INT NOT NULL AUTO_INCREMENT, `link` VARCHAR(255) NULL, PRIMARY KEY (`id`));")

    def addArticle(self, item):
        # On cherche si l'article existe dans la base de données
        sql = 'SELECT * FROM `webscraping`.`article_google` WHERE titre = "' + item['titre'] + '"'
        self.cursor.execute(sql)
        article = self.cursor.fetchone()
        # Si l'article n'existe pas, on l'ajoute
        if article == None:
            sql = "INSERT INTO `webscraping`.`article_google` (nomSource, titre, description, image, date, lien) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (item['nomSource'], item['titre'], item['description'], item['image'], item['date'], item['lien'])
            self.cursor.execute(sql, val)
            self.connection.commit()
        else:
            print('Article déjà existant')


    def addImage(self, link):
        sql = "INSERT INTO `webscraping`.`image_google` (link) VALUES ('" + link + "')"
        self.cursor.execute(sql)
        self.connection.commit()

    def updateImage(self, id, link):
        sql = "UPDATE `webscraping`.`image_google` SET link = '" + link + "' WHERE id = " + str(id)
        self.cursor.execute(sql)
        self.connection.commit()
    
    def findImage(self, link):
        sql = "SELECT * FROM `webscraping`.`image_google` WHERE link = '" + link + "' LIMIT 1"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def listArticleJoinImage(self):
        sql = "SELECT * FROM article_google LEFT JOIN `webscraping`.`image_google` ON article_google.image = image_google.id"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def truncateTable(self):
        self.cursor.execute("TRUNCATE TABLE `webscraping`.`article_google`")
        self.cursor.execute("TRUNCATE TABLE `webscraping`.`image_google`")

    def close(self):
        self.connection.close()