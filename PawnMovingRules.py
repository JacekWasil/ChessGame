print('PawnMovingRules:')

def pawn_move_enable(pawnfield, destField, chessBoardStatus):
    x = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') # x axis fields
    #y = ('1', '2', '3', '4', '5', '6', '7', '8') # y axis fields

    movepossible = 0
    pawncolour = chessBoardStatus.get(pawnfield).figureColour
    if pawncolour == 'White':
        i = 1
    elif pawncolour == 'Black':
        i = -1

    # Move forward x1
    if chessBoardStatus.get(destField).figureType == ' ' and destField == f'{pawnfield[:-1]}{int(pawnfield[-1:]) + i}':
        movepossible = 1

    # Move forward x2
    if chessBoardStatus.get(destField).figureType == ' ' and destField == f'{pawnfield[:-1]}{int(pawnfield[-1:]) + 2 * i}':
        if (pawncolour == 'White' and pawnfield[-1:] == '2') or (pawncolour == 'Black' and pawnfield[-1:] == '7'):
            movepossible = 1

    # Classic Capturing
    xactuall = pawnfield[:-1]
    xdestiny = destField[:-1]
    if ((x.index(xactuall) + 1) == x.index(xdestiny)) or ((x.index(xactuall) - 1) == x.index(xdestiny)): #check if destination in x axis is +/- 1
        if int(pawnfield[-1:]) + i == int(destField[-1:]): #check if destination in y axis is +1
            if pawncolour == 'White' and chessBoardStatus.get(destField).figureColour == 'Black':
                movepossible = 1
            elif pawncolour == 'Black' and chessBoardStatus.get(destField).figureColour == 'White':
                movepossible = 1

    # Pass over an attacked square
    if ((x.index(xactuall) + 1) == x.index(xdestiny)) or ((x.index(xactuall) - 1) == x.index(xdestiny)): #check if destination in x axis is +/- 1
        if int(pawnfield[-1:]) + i == int(destField[-1:]): #check if destination in y axis is +1
            if chessBoardStatus.get(destField).figureColour == ' ': #check if destination field is empty
                # Check if next to white pawn is black (double moved)pawn and other way
                checkPawnSquareNameRight = (f'{(x[(x.index(xactuall) + 1)])}{pawnfield[-1:]}')
                checkPawnSquareNameLeft = (f'{(x[(x.index(xactuall) - 1)])}{pawnfield[-1:]}')
                if pawncolour == 'White':
                    # Check if next to pawn is standing another pawn with opposit colour
                    if chessBoardStatus.get(
                            checkPawnSquareNameRight).figureColour == 'Black' or chessBoardStatus.get(
                            checkPawnSquareNameLeft).figureColour == 'Black':
                        # Check if next to pawn is standing another pawn after double move
                        if chessBoardStatus.get(checkPawnSquareNameRight).pawnDoubleMove or chessBoardStatus.get(checkPawnSquareNameLeft).pawnDoubleMove:
                            movepossible = 1
                if pawncolour == 'Black':
                    # Check if next to pawn is standing another pawn with opposite colour
                    if chessBoardStatus.get(
                            checkPawnSquareNameRight).figureColour == 'White' or chessBoardStatus.get(
                            checkPawnSquareNameLeft).figureColour == 'White':
                        # Check if next to pawn is standing another pawn after double move
                        if chessBoardStatus.get(
                                checkPawnSquareNameRight).pawnDoubleMove or chessBoardStatus.get(
                                checkPawnSquareNameLeft).pawnDoubleMove:
                            movepossible = 1

    if chessBoardStatus.get(destField).figureType == 'king':
        movePossible = 0

    return movepossible

