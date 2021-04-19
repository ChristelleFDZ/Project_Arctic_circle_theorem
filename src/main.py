from aztecdiamond import aztecdiamond

def main():
    # Initialize an empty Aztecdiamond(1) diamond and draw it
    diamond = aztecdiamond(order=1)
    diamond.draw()

    # Fill the A(1) diamond with a randomly-oriented domino pair
    diamond.remplissage_deuxdeux()
    diamond.draw()

    # Then iterate the tiling generation and dessin as it grows
    while True:
        diamond.etape_pavage(draw=True)


if __name__ == '__main__':
    main()