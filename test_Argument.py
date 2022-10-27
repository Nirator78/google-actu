"""
Test de la classe Argument
"""
from utils.Argument import Argument
import sys

# py .\test_Argument.py 1 2

# On initialise la classe Argument avec les arguments de la ligne de commande
arg = Argument(sys.argv)

# On récupère les arguments
print(arg.recherche())
print(arg.nombrePage())

# On initiliase la classe Argument sans arguments pour voir les valeurs par défaut
argEmpty = Argument([])

print(argEmpty.recherche())
print(argEmpty.nombrePage())