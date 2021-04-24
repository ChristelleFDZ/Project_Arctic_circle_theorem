"""
This program will create different dominoes. In fact there are 4 type of dominoes.

"""
import numpy as np
import pygame

#definition des couleurs et orientation 
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
    """
    This class will contain the steps to create different dominoes according to their orientations: East(E),West(O),North(N),South(S)
    It will be used in the aztecdiamond program (Class aztecdiamond). 
    """
    #version ='0.1'
    def __init__(self, angle_droit_h, orientation, order=None):
        """
        Creates the variables associated with the class Domino
        :type angle_droit_h: array
        :param angle_droit_h: an instance of the class passed to __init__

        :type orientation: array # for example: North(N): np.array([-1, 0])
        :param orientation: The direction of the domino, it can be East(E),West(O),North(N),South(S)

        :type order: int 
        :param order: an instance of the class passed to __init__ ; The default value of order is None ;
                        As its name shows, this instance represents the order of our Aztec Diamond.In our 
                        program,the order goes from 1 to 70.
        
                        
        """
        
        
        self.angle_droit_h = np.array(angle_droit_h)
        self.orientation = orientation
        self.rect = None
        
        if order is not None:
            self.gen_rect(order=order)

    def gen_rect(self, order):
        """
        Generates rectangles for the tiling
        In fact, dominoes have rectangular shape

        """
        TAILLE_Grille = AFFICHAGE_Taille / 2 / (order + 1) 
        if order < 70 :
            self.rect = pygame.Rect(
                round(TAILLE_Grille * (order + 1 + self.angle_droit_h[1])),  #  haut
                round(TAILLE_Grille * (order + 1 + self.angle_droit_h[0])),  # gauche
                round(TAILLE_Grille * (2 if self.orientation in (N, S) else 1)),  # largeur
                round(TAILLE_Grille * (1 if self.orientation in (N, S) else 2)),  # hauteur
            )
        
    def step(self):
        self.angle_droit_h += PAVAGE_Etapes[self.orientation]
