from aztecdiamond import AztecDiamond

def main():
    # Initialize an empty AztecDiamond(1) diamond and draw it
    diamond = AztecDiamond(order=1)
    diamond.draw()

    # Fill the AztecDiamond(1) with a randomly-oriented domino pair
    diamond.remplissage_deuxdeux()
    diamond.draw()

    # Then iterate the tiling generation and dessin as it grows
    while True:
        diamond.etape_pavage(draw=True)


if __name__ == '__main__':
    main()