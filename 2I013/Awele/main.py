import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_aleatoire
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_premiercoup
import joueur_derniercoup
import joueur_aleatoire

joueur1=joueur_premiercoup #Contient le module du joueur 1
joueur2=joueur_premiercoup #Contient le module du joueur 2

def joue ():
    """void -> nat
    retourne un gagnant"""
    jeu = game.initialiseJeu ()
 
    while not game.finJeu(jeu) : 
        #game.affiche(jeu)
        print "joueur : {}".format(game.getJoueur(jeu))
        coup = game.saisieCoup(jeu)
        print "coup joue : {}".format(coup)
        game.joueCoup(jeu, coup)
        print "score : {}".format(game.getScores(jeu))
        #game.affiche(jeu)
    return game.getGagnant (jeu)
    
victoires = []
for i in range (10) : 
    gagnant = joue()
    victoires[gagnant]+=1

print str(victoires)
game.affiche(jeu)

joueur = game.joueur2
game.joueur2 = game.joueur1
game.joueur1 = joueur

for i in range (10) : 
    g=joue()
    victoires[g%2+1]+=1

print str(victoires)




