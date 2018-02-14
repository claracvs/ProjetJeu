import sys
import awele 

sys.path.append("../..")

def saisieCoup(jeu):
    valides = awele.getCoupsValides(jeu)
    return valides[0]
