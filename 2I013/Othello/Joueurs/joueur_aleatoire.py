import sys
import random
import othello 

sys.path.append("../..")

def saisieCoup(jeu):
    
    valides = othello.getCoupsValides(jeu)
    l=len(valides)
    
    return valides[random.randint(0,l-1)]
