from aztecdiamond import AztecDiamond

def main():
    """ 
    Firstly we initialize an empty AztecDiamond(1) diamond and draw it, then we fill the AztecDiamond(1) with a randomly-oriented domino pair
    and finally we iterate the tiling generation and dessin as it grows.

    """
    # First step
    diamond = AztecDiamond(order=1)
    diamond.draw()

    # Second step
    diamond.remplissage_deuxdeux()
    diamond.draw()

    #Third step
    while True:
        diamond.etape_pavage(draw=True)


if __name__ == '__main__':
    main()