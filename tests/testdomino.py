import unittest



class testdomino(unittest.TestCase):
    def test_ifonction_is_instance_of_domino(self): # la fonction __init__
        d = Domino(angle_droit_h,np.array([-1, 0]) )
        self.assertIsInstance(d, Domino)

    def test_domino_rectangle(self):
        d = gen_rect(self, order)
        self.assertIsInstance(d,gen_rect)
#Méthode test : "construction de l'objet" 

if __name__ == '__main__':
    unittest.main()     
# OK