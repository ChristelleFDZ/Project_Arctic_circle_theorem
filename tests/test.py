import unittest

class TestDomino(unittest.TestCase):
    def test_ifonction_is_instance_of_domino(self): # la fonction __init__
        d = Domino(angle_droit_h,np.array([-1, 0]) )
        self.assertIsInstance(d, Domino)


if __name__ == '__main__':
    unittest.main()     

