import pytest
import numpy as np
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import domino
from domino import Domino

class TestDomino:
    
    def test_gen_rect(self):
        """
        Test the domino with the order 5, the localisation (3,2) and the position west O 
        """
        d= Domino((3,2), domino.O, 5)
        #test genrect
        assert (d.rect.height,d.rect.left,d.rect.width,d.rect.top) == (133,533,67,600)
 

"""if __name__ == '__main__':
    t= TestDomino()
    t.test_gen_rect()
    #pytest.main()     """
