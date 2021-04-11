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
    N: (0, 114, 189) ,  # bleu
    S: (119, 172, 48) ,  # vert
    E: (162, 20, 47) ,  # rouge
    O: (237, 177, 32) ,  # jaune
    None: (200, ) * 3
}
PAVAGE_Etape = {
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

class aztecdiamond:
    def __init__(self, order, fps=4):
        assert type(order) is int and order > 0
        self.order = order
        self.fps = fps
        self.tiles = []

        self.diamond = None
        self.pavage = None
        self.generate_diamond_array()

        pygame.init()
        self.screen = pygame.display.set_mode([AFFICHAGE_Taille, AFFICHAGE_Taille])
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.clock = pygame.time.Clock()

        self.grille_rects = None
        self.generate_grille_rects()

    def generate_diamond_array(self):
        tri = np.triu(np.ones([self.order] * 2))
        self.diamond = np.concatenate([
            np.concatenate([np.flipud(tri), np.transpose(tri)], axis=1),
            np.concatenate([tri, np.fliplr(tri)], axis=1)
        ], axis=0)
        self.pavage = np.zeros([2 * self.order] * 2, dtype='O')



# Cette fonction génère un rectangle en grille pour la production du diamant
    def production_rect_grille(self):
        self.grid_rects = [
            pygame.Rect(
                round(AFFICHAGE_Taille / 2 * (i + 1) / (self.order + 1)),  # gauche
                round(AFFICHAGE_Taille / 2 * (1 - (i + 1) / (self.order + 1))),  # en haut
                round(AFFICHAGE_Taille * (self.order - i) / (self.order + 1)),  # largeur
                round(AFFICHAGE_Taille * (i + 1) / (self.order + 1)),  # taille
            )
            for i in range(self.order)
        ]
# Description des étapes du pavage
    def etape_pavage(self, draw: bool = False):
        self.increase_order()
        if draw:
            self.draw()
        self.cancel_opposing_movers() # supprimer les carreaux 
                                        #orientés dans le même sens
        if draw:
            self.draw()
        self.move_tiles()
        if draw:
            self.draw()
        self.fill_two_by_twos() # remplir 2 par 2 (le diamant est symétrique)
        if draw:
            self.draw()
