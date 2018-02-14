import sys
import othello 

sys.path.append("../..")

def saisieCoup(jeu):
    valides = othello.getCoupsValides(jeu)
    return valides [-1]
