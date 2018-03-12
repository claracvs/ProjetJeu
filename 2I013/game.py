# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup: Pair[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:N-UPLET[plateau nat List[coup] List[coup] Pair[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

import sys

#sys.path.append ("..")

#import awele
#sys.path.append ("./Joueurs")
#import joueurMiniMax
#import joueur_derniercoup
#import joueur_aleatoire

game=None #awele #Contient le module du jeu specifique: awele ou othello
joueur1=None #joueurMiniMax #Contient le module du joueur 1
joueur2=None #joueur_aleatoire #Contient le module du joueur 2


#Fonctions minimales 

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    jeu[2] = getCoupsValides (jeu)
    [score1, score2] =[jeu[4][0], jeu [4][1]]
    plateau=[[j for j in i] for i in jeu[0]]
    coupsPossibles=[i for i in jeu[2]]
    coupsJoues=[i for i in jeu[3]]
    
    nouveau_jeu= [plateau, getJoueur(jeu), coupsPossibles, coupsJoues, [score1, score2]]
    return nouveau_jeu
    

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    if game.finPartie(jeu) : 
        return True 
    if len(getCoupsValides(jeu)) == 0:
        return True 
    return False

def saisieCoup(jeu):

    if jeu[1] == 1:
        joueur = joueur1
    else :
        joueur = joueur2
    
    jeu[2] = getCoupsValides(jeu)

    coupJoue = joueur.saisieCoup(jeu)
    #print(str(coupJoue))
    #print(str(getCoupsValides(jeu)))
    
    while coupJoue not in getCoupsValides(jeu) :
    #while (not game.coupValide(jeu,coupJoue)):
        print "Votre coup n'est pas valide, recommencez la saisie"
        coupJoue = joueur.saisieCoup(jeu)

    return coupJoue
    
def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu a jour (sauf coups valides qui est fixee a None)
    """
    game.joueCoup(jeu, coup)

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    plateau=game.initPlateau()
    coupsPossibles=None
    coupsJoues=[]
    score= game.initScore()
    joueur=1
    
    return [plateau, joueur, coupsPossibles, coupsJoues, score]
    

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    if finJeu(jeu) : 
        return game.gagnant(jeu)
    return 0

def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    
    print("Coups joues : "+str(jeu[3]))
   
    print "Joueur : {}".format(jeu[1])
    print "Scores = {}, {}".format(jeu [4][0],jeu[4][1])
    print "Plateau  : "
    print"       |  ",
    lc=len(jeu[0][0])
    for i in range(lc):
        print i, "  |  ",
    print 
    print"------------------------------------------------------------------------"
    i=0
    while(i<len(jeu[0])) :
        print"  ", i, "  |",
        j=0
        while (j<(len(jeu[0][1]))) :
            print" ", jeu[0][i][j], "  |",
            j=j+1
        i+=1
        print
        print"------------------------------------------------------------------------"
    
# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    return jeu[0]

def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    return jeu[3]

def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met a jour la liste des coups valides
    """
    if jeu[2] is None : 
        jeu [2] = game.getCoupsValides(jeu)
    return jeu[2]
    

def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    return jeu[4]

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    return jeu[1]

def getAdversaire (jeu) :
    """ jeu  -> nat
        Retourne l'adversaire du joueur qui joue dans le jeu passe en parametre
    """
    return jeu[1]%2+1

def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
    if jeu[1]==1 :
        jeu[1] = 2
    else :
        jeu[1] = 1

def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    return jeu[4][joueur-1]

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    return jeu[0][ligne][colonne]

def setCaseVal(jeu, ligne, colonne, valeur) : 
    """ jeu*nat*nat*nat -> void
        Modifie le contenu de la case ligne,colonne du jeu en lui affectant le contenu valeur
    """
    jeu[0][ligne][colonne] = valeur
    
    




