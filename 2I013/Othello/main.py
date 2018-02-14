import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
import joueur_premiercoup
import joueur_derniercoup
import joueur_aleatoire

joueur1=joueur_premiercoup #Contient le module du joueur 1
joueur2=joueur_premiercoup #Contient le module du joueur 2
jeu=game.initialiseJeu()

while(not game.finJeu(jeu)) :
    game.affiche(jeu)
    print"Joueur ", jeu[1], ", a votre tour de jouer"
    coup = game.saisieCoup(jeu)
    game.joueCoup(jeu, coup)
gagnant=game.getGagnant(jeu)
game.affiche(jeu)
print "Le gagnant est le joueur",gagnant+1

