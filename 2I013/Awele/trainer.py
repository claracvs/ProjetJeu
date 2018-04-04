# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:08:58 2018

@author: 3671207
"""
from copy import deepcopy
import random
import main
import sys
sys.path.append("..")
import game
sys.path.append("./Joueurs")
import ab
import ab_train
import joueur_aleatoire

game.joueur1 = ab_train
game.joueur2 = ab

    
def train (epsilon=0.5, decay = 1) : 
    e = epsilon    
    pars = [i for i in ab_train.params]
    print(str(pars))
    for i in range (20) : 
        for j in range (6):
            v1 = main.joue100parties()
            ab_train.params [j]+=epsilon
            v2 = main.joue100parties ()
            if (v1 [0]> v2[0]) : 
                ab_train.params [j]-=epsilon
                print("ab_train : " + str(ab_train.params)+"; train : "+ str(ab.params))
                print("victoire 1 :" + str(v1) + "; victoire 2 : " + str(v2))
            #pars [j]=ab_train.params[j]
        e*=decay
        ab.params = deepcopy(pars)
        train(e, decay)
            
train ()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            