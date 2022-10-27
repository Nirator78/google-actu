class Argument:
    def __init__(self, argv):
        self.argv = argv

    def recherche(self):
        try:
            return self.argv[1]
        except:
            return 'actualite'
    
    def nombrePage(self):
        try:
            return self.argv[2]
        except:
            return 1