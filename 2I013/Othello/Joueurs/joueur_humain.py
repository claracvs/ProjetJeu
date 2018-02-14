import sys
sys.path.append("../..")


def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    coup = []
    coup.append(input("Priere d'entrer le numero de la ligne :"))
    coup.append(input("Priere d'entrer le numero de la colonne :"))
    return coup
    


