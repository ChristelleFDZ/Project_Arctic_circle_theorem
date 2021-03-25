# Project_Arctic_circle_theorem-
Project for HMMA238.

Made by :
* Djouahra Sonia : sonia.djouahra@etu.umontpellier.fr
* Es-Sbai Omar : omar.es-sbai@etu.umontpellier.fr
* Sow Oumouratou Anna : oumouratou-anna.sow@etu.umontpellier.fr
* Fernandez Christelle: christelle.fernandez@etu.umontpellier.fr

-------------------------------

## <font color="purple">Aztec Diamond </font>
------------------------------------

In combinatorial mathematics, Aztec diamond of order $n$, is the set of all squares of square network whose centers $(x,y)$ satisfy $| x | + | y | ≤ n.$ 

We will work with the squares of colored diamond in chessboard.

*Here is an example of Aztec diamond of order $1$, $2$, $3$ and $6$.*

<p align="center">
  <img src="https://user-images.githubusercontent.com/78490299/112157586-a5c83600-8be7-11eb-888d-f195621129ff.png" alt="Sublime's custom image"/>
</p>


>http://images.math.cnrs.fr/Pavages-aleatoires-par-touillage.html


-----------------------------------
## <font color="purple">Random paving </font>
--------------------------------------

Now, we are interested in paving this figure.
We are going to tile our Aztec diamond using dominoes. The rules of the paving are as follows:
- firstly, our dominoes have to completely fill our figure,
- secondly, they must not overlap 
- and finally, don't come out of the figure.
There are a very large number of possible ways to place them. Indeed, for an Aztec Diamond of order $n$, there are  $2^{n(n+1)/2}$ several tilings.

To represent different pavings, we will use a color convention that allows to distingue 4 possibilities of placement for a domino. 
- A horizontal domino with a white square on the right is represented by a clear blue domino.
- A horizontal domino with a white square on the left is represented by a green domino.
- A vertical domino with a white square at the bottom is represented by a yellow domino.
- A vertical domino with a black square at the bottom is represented by a red domino.

*Below are $8$ possibilities of paving an Aztec diamond of size $2$:*
<p align="center">
  <img src="https://user-images.githubusercontent.com/78490299/112157958-00619200-8be8-11eb-8330-ca0a3d207fee.png" alt="Sublime's custom image"/>
</p>


>http://images.math.cnrs.fr/Pavages-aleatoires-par-touillage.html

__Does it exist a typical arrangement of tilings on a large scale ?__


-------------------

## <font color="purple"> The arctic circle phenomenon </font>
----------------------------------


If we randomly choose one of the possible tilings of a large enough size of the Aztec diamond, we will see (with a probability close to $1$ ) the formation of a circle in the center of the diamond. "This circle is called the **'arctic circle'**. Indeed, this circle is made up of dominoes of different colors which are positioned out of order.

On the other hand, outside the 'arctic circle', regularly tailed regions in the corners are called 'frozen regions'. In fact in each corner, the dominoes have same direction.

**This is the phenomenon of the arctic circle.**

This Theorem says that if we push all off it in infinity, we get a picture with a perfect circle in **a perfect diamond.**


<p align="center">
  <img src="https://user-images.githubusercontent.com/78490299/112158817-d3fa4580-8be8-11eb-9dc5-036e8558cc52.png" alt="Sublime's custom image"/>
</p>


*Warning: The phenomenon of arctic circle is specific to diamond aztec; a typical tiling of the square does not contain any frozen areas, and the arrangement of dominoes is totally random.*

<p align="center">
  <img src="https://user-images.githubusercontent.com/78490299/112158874-e1afcb00-8be8-11eb-8554-4396720d6afe.png" alt="crré"/>
</p>



>https://math.univ-angers.fr/fete-de-la-science/

-------------------
## <font color="purple">Goals and Work Organization</font>
----------------

For our project, we want to represent arctic phenomenon in form of animation(widget or gif).
The goal is to relate the previous information in a simple and fun way accessible to all.

For this we will have in :

### Part 1 : Coding
* **Figure:** creation of the figure in function of the size $n$ and colors in function of the paving.
* **Visualization** (widget or gif of the figure with playful animation)

### Part 2 : Documentation
* In-depth research of functions used and mathematical explanation
* Examples


### Part 3 : Last point 
* Finalization of the page *Githup*

It was difficult to find an equivalent distribution of tasks because different parts are closely linked, we have chosen to work as follows:


| Omar | Anna | Christelle | Sonia |
|--:|---------|:--:|:----|
|Visualization|   Figure      | Visualization |    Figure      |


*For now, each person's work refers to the coding part and each person will take care of their documentation part. Of course, the distribution of work is purely objective.*



