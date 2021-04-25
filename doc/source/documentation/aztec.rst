Aztec Diamond 
==============

What's an aztec diamond  ?
-----------------------------

In combinatorial mathematics, Aztec diamond of order n, is the set of all squares of square network whose centers (x,y) satisfy  x + y < n .
We will work with the squares of colored diamond in chessboard.

Here is an example of Aztec diamond of order 1, 2, 3 and 6.

.. image:: http://images.math.cnrs.fr/IMG/png/vide.png
   :align: center





Random paving 
--------------------------------------

Now, we are interested in paving this figure.
We are going to tile our Aztec diamond using dominoes. The rules of the paving are as follows:


- firstly, our dominoes have to completely fill our figure,
- secondly, they must not overlap 
- and finally, don't come out of the figure.

There are a very large number of possible ways to place them. Indeed, for an Aztec Diamond of order n, there are 

.. image:: https://render.githubusercontent.com/render/math?math=2%5E%7Bn(n%2B1)/2%7D 
   
several tilings.

To represent different pavings, we will use a color convention that allows to distingue 4 possibilities of placement for a domino. 

- A horizontal domino with a white square on the right is represented by a clear blue domino.
- A horizontal domino with a white square on the left is represented by a green domino.
- A vertical domino with a white square at the bottom is represented by a yellow domino.
- A vertical domino with a black square at the bottom is represented by a red domino.

Below are 8 possibilities of paving an Aztec diamond of size 2:

.. image:: https://user-images.githubusercontent.com/78490299/112157958-00619200-8be8-11eb-8330-ca0a3d207fee.png
   :align: center

In this part, you'll see how to create the aztec diamond .


The class toset up the paving process with dominoes :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: src.domino.Domino
    :members: __init__ ,gen_rect , 



__Does it exist a typical arrangement of tilings on a large scale ?__


The arctic circle phenomenon 
----------------------------------


If we randomly choose one of the possible tilings of a large enough size of the Aztec diamond, we will see (with a probability close to 1 ) the formation of a circle in the center of the diamond. "This circle is called the **'arctic circle'**. Indeed, this circle is made up of dominoes of different colors which are positioned out of order.

On the other hand, outside the 'arctic circle', regularly tailed regions in the corners are called 'frozen regions'. In fact in each corner, the dominoes have same direction.

**This is the phenomenon of the arctic circle.**

This Theorem says that if we push all off it in infinity, we get a picture with a perfect circle in **a perfect diamond.**

The class toset up the shuffling dominoes to create the arctic circle :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: src.aztecdiamond.aztecdiamond
    :members: __init__ , generate_diamond_array , production_rect_grille, etape_pavage , augmentation_taille , suppression_oppose , move_tiles , remplissage_deuxdeux , draw , ecran_vide , dessin_grille , dessin_tuiles , dessin_commentaire


.. image:: https://user-images.githubusercontent.com/78490299/112158817-d3fa4580-8be8-11eb-9dc5-036e8558cc52.png
   :align: center



*Warning: The phenomenon of arctic circle is specific to diamond aztec; a typical tiling of the square does not contain any frozen areas, and the arrangement of dominoes is totally random.*

.. image:: https://user-images.githubusercontent.com/78490299/112158874-e1afcb00-8be8-11eb-8554-4396720d6afe.png
   :align: center
