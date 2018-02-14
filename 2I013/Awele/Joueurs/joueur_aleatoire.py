import sys
import random
import awele 

sys.path.append("../..")

def saisieCoup(jeu):
    
    valides = awele.getCoupsValides(jeu)
    l=len(valides)
    
    return valides[random.randint(0,l-1)]
