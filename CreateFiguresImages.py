def figure_image_generation(colour='', figtype='', squarecolour ='', figimg=''):
    if colour == 'White':
        if figtype == 'pawn':
            figimg = 'wpawn_img'
        elif figtype == 'rook':
            figimg = 'wrook_img'
        elif figtype == 'knight':
            figimg = 'wknight_img'
        elif figtype == 'bishop':
            figimg = 'wbishop_img'
        elif figtype == 'queen':
            figimg = 'wqueen_img'
        elif figtype == 'king':
            figimg = 'wking_img'
    elif colour == 'Black':
        if figtype == 'pawn':
            figimg = 'bpawn_img'
        elif figtype == 'rook':
            figimg = 'brook_img'
        elif figtype == 'knight':
            figimg = 'bknight_img'
        elif figtype == 'bishop':
            figimg = 'bbishop_img'
        elif figtype == 'queen':
            figimg = 'bqueen_img'
        elif figtype == 'king':
            figimg = 'bking_img'
    else:
        if squarecolour == 'light yellow':
            figimg = 'wsquare_img'
        else:
            figimg = 'bsquare_img'

    return figimg
