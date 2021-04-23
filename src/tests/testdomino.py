import unittest
import numpy as np
import sys 
from domino import Domino
sys.path.append("..") # for getting out of tests directory
#from src.domino import Domino
#  l'importation de Domino failed
class testdomino(unittest.TestCase):
    def test_ifonction_is_instance_of_domino(self): # la fonction __init__
        d = Domino(angle_droit_h[1],np.array([-1, 0]),1 )
        self.assertIsInstance(d, Domino)

    def test_domino_rectangle(self):
        d = gen_rect(1)  # order=1
        self.assertIsInstance(d,gen_rect)

    def test_orientation_is_in_ORIENTATIONS(self):
        self.assertIn(Domino.orientation, ORIENTATIONS)

#Méthode test : "construction de l'objet" 

if __name__ == '__main__':
    unittest.main()     
#Ran 3 tests in 0.001s
#FAILED (errors=3)
#Error : No module named 'src'