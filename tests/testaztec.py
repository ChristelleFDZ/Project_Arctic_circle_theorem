import unittest

class test_aztect_instance(unittest.TestCase):
    def test_aztec_array(self):
        gda = generate_diamond_array(self)
        self.assertIsInstance(gda.pavage,generate_diamond_array)

    def test_aztec_grille(self):
        gda = production_rect_grille(self)
        self.assertIsInstance(gda.grille_rects,production_rect_grille)    

if __name__ == '__main__':
    unittest.main()   
      
#Ran 2 tests in 0.001s
#FAILED (errors=2)