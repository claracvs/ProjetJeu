# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:26:54 2018

@author: 3671207
"""

import game 


moi = None
PMAX = 2
params=[10,3,3]

def saisieCoup(jeu) :
    global moi
    moi=game.getJoueur(jeu)
    coup=decision(jeu,game.getCoupsValides(jeu))
    return coup
    
def decision (jeu, listeCoups) : 
    """ jeu*[coup]-> pair[coup, score]
    choisit le coup à jouer dans une liste de coup possibles
    """
    coupAjouer = None
    scoremax = -10000000000
    for coup in listeCoups :
        score_estime = estimation (jeu, coup, 1, -10000000,10000000)
        if score_estime > scoremax : 
            coupAjouer = coup
            scoremax=score_estime
    return coupAjouer
    
    
def estimation (jeu, coup, profondeur, alpha, beta) : 
    copie = game.getCopieJeu(jeu)
    game.joueCoup (copie, coup)    
    if game.finJeu(copie) : 
        gagnant = game.getGagnant(copie)
        if gagnant == moi :
            return 10000
        elif gagnant == 0 : 
            return -100
        else :
            return -10000
            
    if profondeur == PMAX :
        return evaluation (copie)
        
    listeCoups = game.getCoupsValides (copie)  
   
    if profondeur%2 ==0:  #noeud max
        scoremax=-10000000
        for c in listeCoups : 
            score_estime = estimation(copie, c, profondeur+1, max(alpha, scoremax), beta)
            if  score_estime >= beta :
                return 10000000  
            if score_estime>scoremax : 
                scoremax=score_estime
        return scoremax

    if profondeur%2==1: #noeud min
        scoremin=10000000
        for c in listeCoups : 
            score_estime = estimation(copie, c, profondeur+1, alpha, min(beta, scoremin))
            if  score_estime <= alpha :
                return -10000000
            if score_estime<scoremin:
                scoremin=score_estime
        return scoremin

            
def evaluation (jeu) : 
    """ jeu -> int 
    """
    def dot (param, evals):#produit scalaire poids*sous fonctions d'eval
        res=0
        for i in range(len(evals)):
            res+=params[i]*evals[i]    
        return res
    evals = [f1(jeu), f2(jeu), f3(jeu)]
    #print ("evaluation "+ str (dot (params,evals)))
    return dot (params, evals)
        
    
def f1 (jeu) :    
    #print ("difference de score " + str (game.getScore(jeu,moi)-game.getScore(jeu, moi%2+1)))
    return game.getScore(jeu,moi)-game.getScore(jeu, moi%2+1)

def f2 (jeu) : #début de partie : alterner case vide et case pleine
    res = 0    
    if len (jeu[3])<20 :
        for i in range (5) : 
            if (jeu[0][moi-1][i]==0 and jeu[0][moi-1][i+1]!=0) or (jeu[0][moi-1][i]!=0 and jeu[0][moi-1][i+1]==0)  :
                res +=1
    return res
    
def f3 (jeu) : #milieu de partie : peu de graines à gauche, beaucoup de graines à droite    
    if len (jeu[3])>=20 : 
        if moi == 1 : 
            grenier = jeu[0][moi-1][3] + jeu[0][moi-1][4] + jeu[0][moi-1][5]
            defense = jeu[0][moi-1][0] + jeu[0][moi-1][1] + jeu[0][moi-1][2]
        else : 
            defense = jeu[0][moi-1][3] + jeu[0][moi-1][4] + jeu[0][moi-1][5]
            grenier = jeu[0][moi-1][0] + jeu[0][moi-1][1] + jeu[0][moi-1][2]
        #print("reserves "+str(grenier-defense))
        return grenier - defense            
    return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        