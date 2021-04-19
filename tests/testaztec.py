import unittest

class test_aztect_instance(unittest.TestCase):
    def test_aztec_array(self):
        gda = generate_diamond_array(self)
        self.assertIsInstance(gda.pavage,generate_diamond_array)

    def test_aztec_grille(self):
        gda = production_rect_grille(self)
        self.assertIsInstance(gda.grille_rects,production_rect_grille)    
##probleme au return : RAN O tests in O.000s
#je comprends pas l'erreur...

    if __name__ == '__main__':
        unittest.main()     
