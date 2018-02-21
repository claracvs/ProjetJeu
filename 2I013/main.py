import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueurMiniMax
import joueur_aleatoire
import joueur_derniercoup
game.joueur1=joueurMiniMax
game.joueur2=joueur_aleatoire

def joue ():
    """void -> nat
    retourne un gagnant"""
    jeu = game.initialiseJeu ()
 
    while not game.finJeu(jeu) : 
        coup = game.saisieCoup(jeu)
        game.joueCoup(jeu, coup)
    return game.getGagnant (jeu)
    
victoires = [0,0]
for i in range (50) : 
    gagnant = joue()
    if gagnant :
        victoires[gagnant-1]+=1

print str(victoires)

joueur = game.joueur2
game.joueur2 = game.joueur1
game.joueur1 = joueur

for i in range (50) : 
    g=joue()
    if g :
        victoires[g%2]+=1

print str(victoires)




