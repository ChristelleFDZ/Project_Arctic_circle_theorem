import random
import numpy as np
import pygame

#option d'affichage (on pourra changer les parametres si trop petit a voir ensemble.. )
#definition des couleurs et orientation 
AFFICHAGE_Taille = 1000
ARRIEREPLAN_Couleur = (20, ) * 3 # Choix noirs ??
BORDURE_Couleur = (0, ) * 3
BORDURE_Largeur = 2
ORIENTATIONS = N, S, E, O = range(4) #direction
PAVAGE_Couleur = {
    N: (0, 114, 189) ;  # bleu
    S: (119, 172, 48) ;  # vert
    E: (162, 20, 47) ;  # rouge
    O: (237, 177, 32) ;  # jaune
    None: (200, ) * 3
}
PAVAGE_Etape = {
    N: np.array([-1, 0]), #Nord
    S: np.array([1, 0]), # Sud
    E: np.array([0, 1]), # Est
    O: np.array([0, -1]), #Ouest
}
PAVAGE_Etape_conflits = {
    N: S ;
    S: N ;
    E: O ;
    O: E ; 

}


class Domino:
    def __init__(self, angle_droit_h, orientation, order=None):
        assert orientation in ORIENTATIONS
        self.angle_droit_h = np.array(angle_droit_h)
        self.orientation = orientation
        self.rect = None
        