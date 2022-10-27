
from selenium.webdriver.common.by import By

class Scraper :
    def getData(self, article):
        item = {}
        try:
            item["nomSource"] = article.find_element(By.CLASS_NAME, 'CEMjEf.NUnG9d').text
        except:
            item["nomSource"] = None
        try:
            item["titre"] = article.find_element(By.CLASS_NAME, 'mCBkyc.y355M.ynAwRc.MBeuO.jBgGLd.OSrXXb').text.replace('"', '')
        except:
            item["titre"] = None
        try:
            item["description"] = article.find_element(By.CLASS_NAME, 'GI74Re.jBgGLd.OSrXXb').text
        except:
            item["description"] = None
        try:
            item["image"] = article.find_element(By.TAG_NAME, 'img').get_attribute('src')
        except:
            item["image"] = None
        try:
            item["date"] = article.find_element(By.CLASS_NAME, 'OSrXXb.ZE0LJd.YsWzw').text
        except:
            item["date"] = None
        try:
            item["lien"] = article.find_element(By.CLASS_NAME, 'WlydOe').get_attribute('href')
        except:
            item["lien"] = None

        return item