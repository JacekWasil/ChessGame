
def knight_move_enable(knightfield, destField, chessBoardStatus):
    xAxisBoard = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
    knightXIndexField = xAxisBoard.index(knightfield[:-1])
    destXIndexField = xAxisBoard.index(destField[:-1])
    check = 0
    movePossible = 0
    knightColour = chessBoardStatus.get(knightfield).figureColour
    figureColourOnDestField = chessBoardStatus.get(destField).figureColour
    actuallSquareColour = chessBoardStatus.get(knightfield).squareColour
    destFieldColour = chessBoardStatus.get(destField).squareColour



    if actuallSquareColour != destFieldColour and knightfield[:-1] != destField[:-1]: #check if destination square is a different colour and column has different name
        if (int(knightfield[-1:]) == int(destField[-1:]) + 1) or (int(knightfield[-1:]) == int(destField[-1:]) + 2) or\
                (int(knightfield[-1:]) == int(destField[-1:]) - 1) or (int(knightfield[-1:]) == int(destField[-1:]) - 2): #check if dest field is in range in Y axis
                if (knightXIndexField + 1 == destXIndexField) or (knightXIndexField - 1 == destXIndexField) or\
                    (knightXIndexField + 2 == destXIndexField) or (knightXIndexField - 2 == destXIndexField):
                    if chessBoardStatus.get(destField).figureType == ' ': #if dest field empty then move possible
                        movePossible = 1
                    if knightColour != figureColourOnDestField: #if figure colour on dest field is different than knight colour
                        movePossible = 1

    if chessBoardStatus.get(destField).figureType == 'king' and movePossible:
        movePossible = 0
        check = 1

    return movePossible, check