import random
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueurMiniMax
import joueurMiniMaxElag
#import joueur_aleatoire
import joueurDefaillant
#import joueur_humain
import time

game.joueur1 = joueurDefaillant
game.joueur2=  joueurMiniMaxElag


debut=time.time()
def joue ():
    """void -> nat
    retourne un gagnant"""
    jeu = game.initialiseJeu ()
    
    for i in range (4):
        random.seed()
        coup = joueur_aleatoire.saisieCoup(jeu)
        game.joueCoup(jeu, coup)
    
    while not game.finJeu(jeu) :
        #game.affiche(jeu)
        coup = game.saisieCoup(jeu)
        game.joueCoup(jeu, coup)
    return game.getGagnant (jeu)
    
victoires = [0,0]

for i in range (50) : 
    gagnant = joue()
    if gagnant!=0 :
        victoires[gagnant-1]+=1

print str(victoires)
moitie = time.time()
print (moitie-debut)

joueur = game.joueur2
game.joueur2 = game.joueur1
game.joueur1 = joueur

for i in range (50) : 
    gagnant=joue()
    if gagnant!=0 :
        victoires[gagnant%2]+=1

print str(victoires)

fin = time.time ()
print ("temps de jeu : " + str(fin-debut))



