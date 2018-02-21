#awele
import sys
sys.path.append("..")
import game

def initPlateau () :
    """void->plateau
    initialise le plateau : 4 graines dans chaque case"""
    plateau = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    return plateau

def initScore():
    """void->List[score]
    initialise les scores a 0"""
    score = [0,0]
    return score
    
    
def finPartie (jeu) : 
    if len(jeu[3]) > 100 : 
        return True
    if jeu[4][0]>24 or jeu[4][1]>24 : 
        return True
    return False 


def gagnant (jeu) : 
    """jeu-> nat
    renvoie le numero du joueur gagant, 0 si match nul"""
    score = jeu[4]
    if score[0]>score[1] : 
        #print "le joueur 1 a gagne"
        return 1
    if score[1]>score[0] : 
        #print "le joueur 2 a gagne"
        return 2
    print "match nul"
    return 0
    
    
def joueCoup(jeu, coup) : 
    """jeu*coup->jeu
    re-initialise le jeu en fonction du coup joue    
    """
    nb_graines = game.getCaseVal(jeu, coup[0], coup[1])
    game.setCaseVal(jeu, coup[0], coup[1], 0)
    distribueJeu(jeu, coup, nb_graines)
    jeu[3].append(coup)
    jeu[2]=None
    game.changeJoueur(jeu)

def coupValide (jeu, coup, affame = False) : 
    """jeu*coup*bool -> bool
    permet de savoir si un coup est valide"""
    nb_graines = game.getCaseVal(jeu, coup[0], coup[1])
    if nb_graines == 0 : 
        return False
    if affame : #permet de savoir s'il est possible de nourrir l'adversaire et donc si on doit le faire
        if coup[0]==0 : 
            return nb_graines > coup[1]
        else : 
            return nb_graines > 5-coup[1]
    return True
 
    
def getCoupsValides (jeu) :
    """jeu->list(coups)
    renvoie la liste des coups valides
    """ 
    joueur = game.getJoueur(jeu)
    a = estAffame(jeu,game.getAdversaire(jeu))
    return [[joueur-1, coup] for coup in range(6) if coupValide(jeu, [joueur-1, coup], a)]
    
   
def estAffame (jeu, adversaire) :
    """jeu*joueur -> bool
    """
    
    ligne = game.getAdversaire(jeu)-1
    somme = 0
    
    for i in range(6) :
        somme = somme + jeu[0][ligne][i]
    if (somme==0) : 
        return True
    return False
        
def nextCase (jeu, coup) : 
    """retourne les coordonnees de la prochaine case a parcourir selon le sens dans lequel on tourne"""
    
    if coup[0]==0 : #le sens inverse est le sens de parcours de la ligne 0 car pas le sens de lecture normal
        if coup[1] > 0 : 
            return [coup[0],coup[1]-1]
        else : 
            coup[0]=1
            return [coup[0], coup[1]]
    else    :
        if coup[1] < 5 :
            return [coup[0], coup[1]+1]
        else :
            coup[0]=0
            return [coup[0],coup[1]]

def distribueJeu (jeu, coup, nb_graines) :
    """jeu*coup*nat-> jeu
    distribue les graines""" 
    
    case = coup

    while (nb_graines > 0) : 
        case = nextCase(jeu, case)
        if (case == coup) :
            continue
        jeu[0][case[0]][case[1]]+=1
        nb_graines -=1
    
    manger(jeu,case)

def manger (jeu,coup):
    """
    jeu*coup->jeu
    mange les graines de l'adversaire si c'est possible et renvoie le jeu modifie
    """
    
    jeu_bis=game.getCopieJeu(jeu)
    case_val = game.getCaseVal(jeu,coup[0],coup[1])

    while (case_val== 2) or (case_val== 3) and jeu[0][1]==game.getAdversaire(jeu)-1 :
    	#print "valeur de la case a manger  : {}, coordonnees {}".format(case_val, coup)
        jeu[4][jeu[1]-1] += case_val #mise a jour du score
        #print "score : {}".format (jeu[4][jeu[1]-1])
        #game.setCaseVal(jeu_bis, coup_bis[0], coup_bis[1],0)
        jeu[0][coup[0]][coup[1]] = 0
        #print "case mangee?  : {}, coordonnees {}".format(jeu[0][coup[0]][coup[1]], coup)
        if coup[0]==0 : #cas ou le joueur 2 mange
            if coup[1]<5:
                coup[1]+=1
        else : #cas ou le joueur 1 mange
            if coup [1]>0:
                coup[1]-=1
        case_val = game.getCaseVal(jeu,coup[0],coup[1])
        #print "valeur de la nouvelle case a manger  : {}, coordonnees {}".format(case_val, coup) 
    
    if estAffame(jeu, game.getAdversaire(jeu)) :
        #print "on n'a pas pu manger"
        for i in range(5):
            jeu[i]=jeu_bis[i]
        
   




























        
        
        
        
 
    
    





















