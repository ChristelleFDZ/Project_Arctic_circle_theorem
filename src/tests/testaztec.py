import unittest
import sys 
sys.path.append("..") # for getting out of tests directory
from src import aztecdiamond
# l'importation de aztecdiamond failed

class test_aztecdiamond(unittest.TestCase):
    def test_aztec_array(self):
        gda = generate_diamond_array(self)
        self.assertIsInstance(gda.pavage,generate_diamond_array)

    def test_aztec_grille(self):
        gda = production_rect_grille(self)
        self.assertIsInstance(gda.grille_rects,production_rect_grille)  

    def test_order_is_positive(self):
        self.assertGreater(aztecdiamond.order,0)  

    def test_order_is_int(self):
        self.assertTrue(aztecdiamond.order is int )

if __name__ == '__main__':
    unittest.main()   
      
#Ran 4 tests in 0.001s
#FAILED (errors=4)
#Error : No module named 'src'