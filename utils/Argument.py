"""
 Class permettant de gérer les arguments passés au script
"""
class Argument:
    # Récupération des arguments
    def __init__(self, argv):
        self.argv = argv
 
    # Renvoie de la recherche, si aucun argument n'est passé, on renvoie une recherche par défaut
    def recherche(self):
        try:
            return self.argv[1]
        except:
            return 'actualite'
    
    # Renvoie du nombre de page a scrapper, si aucun argument n'est passé, on renvoie 1 page
    def nombrePage(self):
        try:
            return self.argv[2]
        except:
            return 3