import sys
sys.path.append("..")
import game

def initPlateau() : 
    plateau=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    plateau[3][3]=1
    plateau[4][4]=1
    plateau[3][4]=2
    plateau[4][3]=2
    return plateau


def listeCoupsValides(jeu):
    liste_coups = coups(jeu)
    return [i for i in liste_coups if len(encadrement(jeu, i, False))>0]
     
def coups(jeu) : 
    joueur=game.getJoueur(jeu)
    joueur=(j%2)+1
    s={str(x) for l in range(0,8) for c in range(0,8) for x in entourageVide(jeu, [l,c]) if game.getCaseVal(jeu, l, c)==j}
    return [eval(x) for x in s]

def finJeu(jeu) :
    return False
    
    
    
def entourageVide(jeu, case) : 
    ret = []
    l=case[0]
    c=case[1]
    if l>0 : 
        if (game.getCaseVal(jeu, l-1, c)==0) : 
            ret.append([l-1, c])
        if (c>0) : 
            if (game.getCaseVal(jeu, l-1, c-1)==0):
                ret.append([l-1, c-1])
        if c<7 : 
            if (game.getCaseVal(jeu, l-1, c+1)==0) : 
                ret.append([l-1, c+1])
    if l<7 : 
        if (game.getCaseVal(jeu, l+1, c)==0) : 
            ret.append([l+1, c])
        if (c>0) : 
            if (game.getCaseVal(jeu, l+1, c-1)==0):
                ret.append([l+1, c-1])
        if c<7 : 
            if (game.getCaseVal(jeu, l+1, c+1)==0) : 
                ret.append([l+1, c+1])
    if c>0 : 
        if (game.getCaseVal(jeu, l, c-1)==0) : 
            ret.append([l, c-1]) 
    if c<7 : 
        if (game.getCaseVal(jeu, l, c+1)==0) : 
            ret.append([l, c+1]) 
    return ret
    
def encadrement(jeu, case, tous=True) : 
    ret = []
    for l in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if (not ((l==0) and (c==0))) :
                if encadre(jeu, case[0], case[1], l, c) :
                    ret.append([l, c])
                    if (not tous) : 
                        return ret
    return ret
    
    
def encadre(jeu, l, c, ml, mc) : 
    i=0
    j=game.getJoueur(jeu)
    while (True) :
        l+=ml
        c+=mc
        if ((l>7) or (l<0) or (c>7) or (c<0)) : 
            return False
        v=game.getCaseVal(jeu, l, c)
        if (v==j) : 
            if(i==0) : 
                return False
            else : 
                return True
        if (v==0) : 
            return False
        i+=1
    return False
    
    
def joueCoup(jeu, coup) : 
    game.getCoupsJoues(jeu).append(coup)
    j=jeu[1]
    s=game.getScores(jeu)
    e=encadrement(jeu, coup, True) 
    adv=j%2+1
    game.setCaseVal(jeu, coup[0], coup[1], j)
    s[j-1]+=1
    for d in e: 
        l=coup[0]
        c=coup[1]
        while (True) : 
            l+=d[0]
            c+=d[1]
            if (game.getCaseVal(jeu, l, c)==j) :
                break
            game.setCaseVal(jeu, l, c, j)
            s[j-1]+=1 
            s[adv-1]-=1
    game.changeJoueur(jeu)
        
        
        
def initScores():
    parties = [2,2]
    return parties
    
