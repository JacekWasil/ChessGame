
def queen_move_enable(queenField, destField, chessBoardStatus):
    check = 0
    movePossible = 0
    xAxisBoard = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
    queenColour = chessBoardStatus.get(queenField).figureColour
    figureColourOnDestField = chessBoardStatus.get(destField).figureColour
    queenXIndexField = xAxisBoard.index(queenField[:-1])
    actuallSquareColour = chessBoardStatus.get(queenField).squareColour
    destFieldColour = chessBoardStatus.get(destField).squareColour
    bishopXIndexField = xAxisBoard.index(queenField[:-1])
    xMovingDirection = 0  # 1: right, -1: left (a-b-c...)
    yMovingDirection = 0  # 1: up, -1: down (1-2-3...)
    memoryForMovingField = queenField

    # movement like rook:
    if figureColourOnDestField != queenColour and  (queenField[:-1] == destField[:-1] or queenField[-1:] == destField[-1:]): #check if movement is only in horizontal or only vertical direction and dest figure colour is different than rook colour
        if int(destField[-1:]) < int(queenField[-1:]):
            yMovingDirection = -1
        if int(destField[-1:]) > int(queenField[-1:]):
            yMovingDirection = 1
        if xAxisBoard.index(destField[:-1]) < queenXIndexField:
            xMovingDirection = -1
        if xAxisBoard.index(destField[:-1]) > queenXIndexField:
            xMovingDirection = 1

        movePossible = 1
        while memoryForMovingField != destField:
            memoryForMovingField = f'{xAxisBoard[(xAxisBoard.index(memoryForMovingField[:-1]) + xMovingDirection)]}{int(memoryForMovingField[-1:]) + yMovingDirection}'
            if chessBoardStatus.get(memoryForMovingField).figureColour != ' ' and memoryForMovingField != destField:
                movePossible = 0
                break

    #movement like bishop:
    xMovingDirection = 0  # 1: right, -1: left (a-b-c...)
    yMovingDirection = 0  # 1: up, -1: down (1-2-3...)
    memoryForMovingField = queenField
    if actuallSquareColour == destFieldColour and queenColour != figureColourOnDestField and queenField[:-1] != destField[:-1]:  # check if destination square is the same colour and figure on dest field is different colour or empty
        if int(destField[-1:]) < int(queenField[-1:]):
            yMovingDirection = -1
        if int(destField[-1:]) > int(queenField[-1:]):
            yMovingDirection = 1
        if xAxisBoard.index(destField[:-1]) < bishopXIndexField:
            xMovingDirection = -1
        if xAxisBoard.index(destField[:-1]) > bishopXIndexField:
            xMovingDirection = 1

        movePossible = 1
        while memoryForMovingField != destField:
            memoryForMovingField = f'{xAxisBoard[(xAxisBoard.index(memoryForMovingField[:-1]) + xMovingDirection)]}{int(memoryForMovingField[-1:]) + yMovingDirection}'
            if chessBoardStatus.get(memoryForMovingField).figureColour != ' ' and memoryForMovingField != destField:
                movePossible = 0
                break

    if chessBoardStatus.get(destField).figureType == 'king' and movePossible:
        movePossible = 0
        check = 1

    return movePossible, check