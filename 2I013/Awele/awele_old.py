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
    #plateau = jeu[0]
    for i in range(2) :
        for j in range(6) : 
            if jeu[0][i][j]!=0 : 
                return False
    if len(jeu[3]) > 100 : 
        return False
    if jeu[4][0]>24 or jeu[4][1]>24 : 
        retun False
    return True 


def gagnant (jeu) : 
    """jeu-> nat
    renvoie le numero du joueur gagant, 0 si match nul"""
    score = jeu[4]
    if score[0]>score[1] : 
        return 1
    if score[1]>score[2] : 
        return 2
    return 0
    
    
def joueCoup(jeu, coup) : 
    """jeu*coup->jeu
    re-initialise le jeu en fonction du coup joue"""
    jeu[3].append(coup) #ajout du coup a la liste des coups joues
    plateau = jeu[0]
    l = coup[0]
    c = coup [1]
    nb_graines = plateau[l][c]
    plateau[l][c] = 0
    for i in range(nb_graines):
        case_suivant = nextCase(jeu, 
        plateau[coup[0]][coup[1]]+=1
        coup[1]+=1
        if coup[1]>5 : 
            coup[1]=0
            coup[0]=(coup[0]+1)%2
    
    if estAffame == False : 
        while (plateau[coup[0]][coup[1]]==2 or plateau[coup[0]][coup[1]] == 3 ) and coup[1]>=0: 
            #jeu[4] : score
            jeu[4][jeu[1]-1]= plateau[coup[0]][coup[1]]
            plateau[coup[0]][coup[1]]=0
            coup[1]-=1


    
def getCoupsValides (jeu) :
    """jeu->list(coups)
    renvoie la liste des coups valides"
    """

    
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
        
    joueur = game.getJoueur(jeu)
    a = estAffame(jeu, joueur%2+1)
    return [[joueur-1, coup] for coup in range(6) if coupValide(jeu, [joueur-1, coup], a)]
    

def estAffame (jeu, joueur) :
    """jeu*joueur -> bool
    joueur = joueur%2+1
    #case=jeu[0]
    for i in range(6) : 
        if game.getCaseVal(jeu, jeu[0][joueur-1], jeu[0][i])!=0 : 
            return False
    return True"""
    
    ligne = game.getJoueur(jeu)%2
    somme = 0
    
    for i in range(6) :
        somme = somme + jeu[0][ligne][i]
    if (somme==0) : 
        return True
    return False
        
def nextCase (jeu, coup, inverse=True) : 
    """retourne les coordonnees de la prochaine case a parcourir selon le sens dans lequel on tourne"""
    
    if inverse : #le sens inverse est le sens de parcours de la ligne 0 car pas le sens de lecture normal
        if coup[1] > 0 : 
            return [coup[0],coup[1]-1]
        else : 
            return [coup[0]+1, coup[1]]
    else    :
        if coup[1] < 5 :
            return [coup[0], coup[1]+1]
        else :
            return [coup[0]-1, coup[1]]

def distribueJeu (jeu, coup, nb_graines) :
    """jeu*coup*nat-> jeu
    distribue les graines en fonction de la possibilite de manger ou pas, 
    et mange en consequence les graines de l'adversaire"""
    
    case = coup
    jeu[0][coup[0]][coup[1]]=0
    
    while (nb_graines > 0) : 
        coup = nextCase(jeu, coup,coup[0]==0)
        
        if (coup == case) :
            continue
        
        jeu[0][coup[0]][coup[1]]+=1
        nb_graines -=1
        
    jeu_bis=game.getCopie(jeu)
    
    case_val = game.getCaseVal(jeu_bis,coup[0],coup[1])
    while case_val== 2 or case_val== 3:
        jeu_bis[4][jeu[1]-1] += case_val
        jeu_bis[0][coup[0]][coup[1]]=0
        
        coup= nextCase(jeu_bis,coup,coup[0]==0)
        case_val = game.getCaseVal(jeu_bis,coup[0],coup[1])
        
    if estAffame(jeu_bis, jeu_bis[1]%2+1) :
        print "on n'a pas pu manger, miskina"
        return jeu 
    return jeu_bis
    




























        
        
        
        
 
    
    





















