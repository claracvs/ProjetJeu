import sys
sys.path.append("..")
import game

def initPlateau() : 
    plateau=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    plateau[3][3]=1
    plateau[4][4]=1
    plateau[3][4]=2
    plateau[4][3]=2
    """
    plateau[2][2]=1
    plateau[2][3]=2
    plateau[1][4]=2
    plateau[1][3]=2
    plateau[0][4]=1
    plateau[0][2]=1
    """
    return plateau
            
def initScores():
	"""void -> [int,int]
	retourne les scores initiaux"""
	score = [2,2]
	return score	
 
 
def getCoupsValides (jeu) : 
    """jeu -> list
	retourne une liste de coups valides"""
    coups = toucheAdversaire(jeu)
    
    return [unCoup for unCoup in coups if (len(encadrements(jeu,unCoup,False))>0)]
	

def toucheAdversaire (jeu) :
	"""jeu -> list
	retourne la liste des coups touchant l'adversaire
 FONCTIONNE
 """
	return[[i,j] for i in range(8) for j in range(8) for k in [-1,0,1] for l in [-1,0,1] if ((jeu[0][i][j] == 0) and (i+k) >= 0 and (i+k)<8 and (j+l)>=0 and (j+l)<8 and jeu[0][i+k][j+l]==(jeu[1]%2+1))]
	
def getCaseAutour (jeu,case) :
	"""jeu*[int,int] -> list
	prend une case d'un jeu et retourne les 8 cases autour de celle-ci"""
	return [[case[0]+i, case[1]+j] for i in [-1,0,1] for j in [-1,0,1] if case[0]+i < 8 and case[0] + i >= 0 and case[0]+j < 8 and case[0]+j >= 0 and (case[i]!=0 or case[j]!=0) ]
	

def encadrements(jeu,coup,tous=True) : 
    """jeu, list, bool -> list
    si tous= False, on s'arrete des que l'on a un coup valide
    retourne une liste de directions [i,j]"""
    liste_retour = []
    for i in [-1,0,1] :
         for j in [-1,0,1] :
             if (i==0) and (j==0) :
                 continue
             if checkDirection(jeu,coup,[i,j]) :
                 liste_retour.append([i,j])
                 if not tous :
                     return liste_retour    
    return liste_retour
					
def checkDirection(jeu,coup,direction) : #direction [i,j]
	"""jeu* list* [int,int] -> bool
	retourne vrai si on va dans la bonne direction, ie si on se deplace sur un adversaire, false sinon"""
	joueur = jeu[1]
	i = 0
	while True : 
		i+=1
		coup = [coup[0]+direction[0], coup[1]+direction[1]]
		if coup[0]<0 or coup[0] >7 or coup[1] < 0 or coup[1]>7 :
			return False
		if jeu[0][coup[0]][coup[1]] == 0 :
			return False
		if jeu[0][coup[0]][coup[1]] == joueur :
			return i>1


def joueCoup(jeu, coup) : 
    """jeu*coordonnees -> void
	met a jour le jeu avec le coup joue"""
    joueur=game.getJoueur(jeu)
    print "coup joue : {}".format(coup)
    jeu[3].append(coup)
    case = [coup[0],coup[1]]
    
    adversaire=joueur%2+1
    game.setCaseVal(jeu, coup[0], coup[1], joueur)
    jeu[4][joueur-1]+=1
    #print "encadrement :{}".format(encadrements(jeu, coup, True))
    for d in encadrements(jeu, coup, True) : 
        #print "direction  :{}".format(d)
        case = [coup[0],coup[1]]
        case[0]+=d[0]
        case[1]+=d[1]
        while game.getCaseVal(jeu, case[0], case[1])==adversaire : 
            game.setCaseVal(jeu, case[0], case[1], joueur)
            #print "case retournee :{}".format(jeu[0][case[0]][case[1]])
            #print "case : {}".format (case)
            jeu[4][joueur-1] +=1
            jeu[4][adversaire-1]-=1
    game.changeJoueur(jeu)
    jeu[2]=None
        

def finPartie(jeu) :
    """jeu->bool
    retourne vrai si la fin du jeu est atteinte, false sinon"""
    if game.getCoupsValides == []:
        return True
        
    fin_atteinte = True
    
    for i in range(8) :
        for j in range(8) :
            if jeu[0][i][j]==0 :
                fin_atteinte= False
    if len(jeu[3])>100 :
        fin_atteinte = True
    return fin_atteinte

def gagnant(jeu) :
    """jeu-> nat
    renvoie le numero du joueur gagant, 0 si match nul"""
    score = jeu[4]
    if score[0]>score[1] : 
        return 1
    if score[1]>score[0] : 
        return 2
    return 0
	
	
