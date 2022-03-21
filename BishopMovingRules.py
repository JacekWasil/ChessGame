
def bishop_move_enable(bishopfield, destField, chessBoardStatus):
    movePossible = 0
    xAxisBoard = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
    bishopColour = chessBoardStatus.get(bishopfield).figureColour
    figureColourOnDestField = chessBoardStatus.get(destField).figureColour
    actuallSquareColour = chessBoardStatus.get(bishopfield).squareColour
    destFieldColour = chessBoardStatus.get(destField).squareColour
    bishopXIndexField = xAxisBoard.index(bishopfield[:-1])
    xMovingDirection = 1 # 1: right, -1: left (a-b-c...)
    yMovingDirection = 1  # 1: up, -1: down (1-2-3...)
    memoryForMovingField = bishopfield
    if actuallSquareColour == destFieldColour and bishopColour != figureColourOnDestField and bishopfield[:-1] != destField[:-1]: #check if destination square is the same colour and figure on dest field is different colour or empty
        if int(destField[-1:]) < int(bishopfield[-1:]):
            yMovingDirection = -1
        if int(destField[-1:]) > int(bishopfield[-1:]):
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

    if chessBoardStatus.get(destField).figureType == 'king':
        movePossible = 0

    return movePossible