from utils.Argument import Argument
import sys

# py .\test_Argument.py 1 2

arg = Argument(sys.argv)

print(arg.recherche())
print(arg.nombrePage())

argEmpty = Argument([])

print(argEmpty.recherche())
print(argEmpty.nombrePage())