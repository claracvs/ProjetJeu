import sys
sys.path.append("../..")

def saisieCoup(jeu):
    
    coordonnees = []
    coordonnees.append(jeu[1]-1)
    coordonnees.append(input("Priere d'entrer un numero de colonne :"))
    return coordonnees
    
