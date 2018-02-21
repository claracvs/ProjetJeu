# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:59:54 2018

@author: 3671207
"""

#ne sait pas jouer en joueur 2
import game

moi = None
PMAX = 1

def saisieCoup(jeu) :
    global moi
    moi=game.getJoueur(jeu)
    coup=decision(jeu,game.getCoupsValides(jeu))
    return coup[0]
    
def decision (jeu, listeCoups) : 
    """ jeu*[coup]-> pair[coup, score]
    choisit le coup à jouer dans une liste de coup possibles
    """
    coupAjouer = None
    scoremax = -10000000000
    for coup in listeCoups :
        estime = estimation (jeu, coup, 1)
        if estime > scoremax : 
            coupAjouer = coup
            scoremax=estime
    return [coupAjouer, scoremax]
    
    
def estimation (jeu, coup, profondeur) : 
    copie = game.getCopieJeu(jeu)
    game.joueCoup (copie, coup)    
    if game.finJeu(copie) : 
        gagnant = game.getGagnant(copie)
        if gagnant == moi :
            return 1000
        elif gagnant == 0 : 
            return -100
        else :
            return -100000
            
    if profondeur == PMAX :
        return evaluation (copie)
        
    if profondeur%2 ==1:
        listeCoups = game.getCoupsValides (copie)
        scoremax=-10000
        for c in listeCoups : 
            score_estime = estimation(copie, c, profondeur+1)
            if  score_estime > scoremax :
                scoremax=score_estime
        return scoremax

    if profondeur%2==0:
        listeCoups = game.getCoupsValides (copie)
        scoremin=10000
        for c in listeCoups : 
            score_estime = estimation(copie, c, profondeur+1)
            if  score_estime < scoremin :
                scoremin=score_estime
        return scoremin
        
def evaluation (jeu) : 
    """ jeu -> int 
    """
    return game.getScore(jeu,moi)-game.getScore(jeu, moi%2+1)

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
