from memory_profiler import profile
import requests
import time
import numpy as np
import pygame




AFFICHAGE_Taille = 800
ARRIEREPLAN_Couleur = (20, ) * 3 # Choix noirs ??
BORDURE_Couleur = (0, ) * 3
BORDURE_Largeur = 2
ORIENTATIONS = N, S, E, O = range(4) #direction
PAVAGE_Couleur = {
    N: (0, 114, 189) ,  # bleu
    S: (119, 172, 48) ,  # vert
    E: (162, 20, 47) ,  # rouge
    O: (237, 177, 32) ,  # jaune
    None: (200, ) * 3
}
PAVAGE_Etapes = {
    N: np.array([-1, 0]), #Nord
    S: np.array([1, 0]), # Sud
    E: np.array([0, 1]), # Est
    O: np.array([0, -1]), #Ouest
}
PAVAGE_Etape_conflits = {
    N: S ,
    S: N ,
    E: O ,
    O: E ,
}

class Domino:
    
    @profile
    def __init__(self, angle_droit_h, orientation, order=None):
       
        
        assert orientation in ORIENTATIONS
        self.angle_droit_h = np.array(angle_droit_h)
        self.orientation = orientation
        self.rect = None
        
        if order is not None:
            self.gen_rect(order=order)
    @profile
    def gen_rect(self, order):
        
        TAILLE_Grille = AFFICHAGE_Taille / 2 / (order + 1) 
        if order < 30 :
            self.rect = pygame.Rect(
                round(TAILLE_Grille * (order + 1 + self.angle_droit_h[1])),  #  haut
                round(TAILLE_Grille * (order + 1 + self.angle_droit_h[0])),  # droite
                round(TAILLE_Grille * (2 if self.orientation in (N, S) else 1)),  # poids
                round(TAILLE_Grille * (1 if self.orientation in (N, S) else 2)),  # largeur
            )
    @profile
    def step(self):
        self.angle_droit_h += PAVAGE_Etapes[self.orientation]

if __name__ == "__main__":
    Domino([1,1,1,1], O ,None).Domino()