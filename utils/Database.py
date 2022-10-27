from dataclasses import dataclass
import mysql.connector as mc

class Database:
    def __init__(self):
        self.connection = mc.connect(
            host="localhost",
            user="root",
            password="Azerty94",
            database='webscraping'
        )
        self.cursor = self.connection.cursor()

    def connectDb(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS webscraping")

    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `webscraping`.`article_google` (`id` INT NOT NULL AUTO_INCREMENT,`nomSource` VARCHAR(45) NULL, `titre` VARCHAR(255) NULL, `description` TEXT(1000) NULL, `image` INT NULL, `date` VARCHAR(45) NULL, `lien` VARCHAR(255) NULL, PRIMARY KEY (`id`));")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `webscraping`.`image_google` ( `id` INT NOT NULL AUTO_INCREMENT, `link` VARCHAR(255) NULL, PRIMARY KEY (`id`));")

    def addRow(self, item):
        sql = "INSERT INTO movie (title, img, author, time, genre, score, description, releaseDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (item['title'], item['img'], item['author'], item['time'], item['genre'], item['score'], item['desc'], item['release'])
        self.cursor.execute(sql, val)
        self.connection.commit()

    def addRowBoursorama(self, item):
        sql = "INSERT INTO boursorama (indexStockExchange, stockAction, variation, vMax, vMin, vOpen, dateCollect) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (item['indexStockExchange'], item['stockAction'], item['variation'], item['vMax'], item['vMin'], item['vOpen'], item['dateCollect'])
        self.cursor.execute(sql, val)
        self.connection.commit()