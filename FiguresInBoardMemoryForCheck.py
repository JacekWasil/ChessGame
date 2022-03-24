def figures_position_in_memory_board(choosenField, destField, chessBoardStatus):
    figureColour = chessBoardStatus.get(choosenField).figureColour
    figureType = chessBoardStatus.get(choosenField).figureType
    newChessBoardStatus = chessBoardStatus
    x = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
    #y = ('1', '2', '3', '4', '5', '6', '7', '8')  # y axis fields
    xactuall = choosenField[:-1]

    # Check if double moved pawn was captured (if yes: deleted)
    if chessBoardStatus.get(choosenField).figureType == 'pawn':
        rightVriableOverTheBoard = 0
        leftVriableOverTheBoard = 0
        try:
            checkPawnSquareNameRight = (f'{(x[(x.index(xactuall) + 1)])}{choosenField[-1:]}')
        except:
            rightVriableOverTheBoard = 1
        try:
            checkPawnSquareNameLeft = (f'{(x[(x.index(xactuall) - 1)])}{choosenField[-1:]}')
        except:
            leftVriableOverTheBoard = 1
        # Check if next to pawn is standing another pawn with opposite colour
        if (rightVriableOverTheBoard == 0 and chessBoardStatus.get(checkPawnSquareNameRight).figureColour != figureColour) or \
                (leftVriableOverTheBoard == 0 and chessBoardStatus.get(checkPawnSquareNameLeft).figureColour != figureColour):
            # Check if next to pawn is standing another pawn after double move
            if (rightVriableOverTheBoard == 0 and chessBoardStatus.get(checkPawnSquareNameRight).pawnDoubleMove) or \
                    (leftVriableOverTheBoard == 0 and chessBoardStatus.get(checkPawnSquareNameLeft).pawnDoubleMove):
                # check if pass over an attacked square done
                if chessBoardStatus.get(f'{destField[:-1]}{choosenField[-1:]}').figureType == 'pawn':
                    #delete a beaten pawn
                    newChessBoardStatus.get(f'{destField[:-1]}{choosenField[-1:]}').figureType = ' '
                    newChessBoardStatus.get(f'{destField[:-1]}{choosenField[-1:]}').figureColour = ' '

    #move rook for castle
    if chessBoardStatus.get(choosenField).figureType == 'king' and choosenField[:-1] == 'e' and (destField[:-1] == 'c' or destField[:-1] == 'g'):
        if destField[:-1] == 'c':
            newChessBoardStatus.get(f'd{choosenField[-1:]}').figureType = 'rook'
            newChessBoardStatus.get(f'd{choosenField[-1:]}').figureColour = figureColour
            newChessBoardStatus.get(f'a{choosenField[-1:]}').figureType = ' '
            newChessBoardStatus.get(f'a{choosenField[-1:]}').figureColour = ' '
        if destField[:-1] == 'g':
            newChessBoardStatus.get(f'f{choosenField[-1:]}').figureType = 'rook'
            newChessBoardStatus.get(f'f{choosenField[-1:]}').figureColour = figureColour
            newChessBoardStatus.get(f'h{choosenField[-1:]}').figureType = ' '
            newChessBoardStatus.get(f'h{choosenField[-1:]}').figureColour = ' '

    #set new figure position on the board
    newChessBoardStatus.get(choosenField).figureType = ' '
    newChessBoardStatus.get(choosenField).figureColour = ' '
    newChessBoardStatus.get(destField).figureType = figureType
    newChessBoardStatus.get(destField).figureColour = figureColour

    return newChessBoardStatus


