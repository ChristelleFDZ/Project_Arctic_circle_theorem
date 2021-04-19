import unittest

class testdomino(unittest.TestCase):
    def test_domino_rectangle(self):
        d = gen_rect(self, order)
        self.assertIsInstance(d,gen_rect)
#Méthode test : "construction de l'objet" 

    if __name__ == '__main__':
        unittest.main()     
# OK