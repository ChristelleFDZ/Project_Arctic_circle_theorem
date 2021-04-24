import pytest
import numpy as np
import pygame
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import aztecdiamond
from aztecdiamond import AztecDiamond
from numpy.testing import assert_array_equal
""" 
This test is for the class AztecDiamond. They are valids when the display resolution is unchanged here 800.
"""
class TestAztecDiamond:

    def test_generate_diamond_array(self):
        """ 
        This function test if the diamond of the aztec diamond in order 5 equals with what we expected.
        """
        d= AztecDiamond(5)
        d.generate_diamond_array()
        assert_array_equal(d.diamond, np.array([[0.,0.,0.,0.,1.,1.,0.,0.,0.,0.]
                                                ,[0.,0.,0.,1.,1.,1.,1.,0.,0.,0.]
                                                ,[0.,0.,1.,1.,1.,1.,1.,1.,0.,0.]
                                                ,[0.,1.,1.,1.,1.,1.,1.,1.,1.,0.]
                                                ,[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]
                                                ,[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]
                                                ,[0.,1.,1.,1.,1.,1.,1.,1.,1.,0.]
                                                ,[0.,0.,1.,1.,1.,1.,1.,1.,0.,0.]
                                                ,[0.,0.,0.,1.,1.,1.,1.,0.,0.,0.]
                                                ,[0.,0.,0.,0.,1.,1.,0.,0.,0.,0.]]))
    
    def test_production_rect_grille(self): 
        """
        The same here.
        """
        d= AztecDiamond(5)
        d.production_rect_grille()
        expected_rects= [pygame.Rect(67, 333, 667, 133), pygame.Rect(133, 267, 533, 267), pygame.Rect(200, 200, 400, 400), pygame.Rect(267, 133, 267, 533), pygame.Rect(333, 67, 133, 667)]
        assert d.grille_rects == expected_rects 

        
    def test_augmentation_taille(self):
        """
        Here, we test if the order has indeed increased by 1.
        """
        d= AztecDiamond(5)
        d.augmentation_taille()
        assert d.order == 6
    
    def test_remplissage_deuxdeux(self):
        """
        We look here to see if there is the same size we want during the initial step, then filling two by two, then steps (ie: the increase in size, the removal of opposites and the movement of the tiles)
        and finally again the filling two by two.
        """
        d= AztecDiamond(1)
        assert (int(len(d.tiles)),int(len(d.pavage))) == (0,2)
        d.remplissage_deuxdeux()
        assert (len(d.tiles),len(d.pavage))== (2,2)
        d.augmentation_taille() 
        d.suppression_oppose()
        d.move_tiles()
        assert (len(d.tiles),len(d.pavage))== (2,4)
        d.remplissage_deuxdeux()
        assert (len(d.tiles),len(d.pavage))== (6,4)
