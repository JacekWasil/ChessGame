def bishop_move_enable(bishoField, destField, chessBoardStatus):
    check = 0
    movePossible = 0
    xAxisBoard = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
    bishopColour = chessBoardStatus.get(bishoField).figureColour
    figureColourOnDestField = chessBoardStatus.get(destField).figureColour
    actuallSquareColour = chessBoardStatus.get(bishoField).squareColour
    destFieldColour = chessBoardStatus.get(destField).squareColour
    bishopXIndexField = xAxisBoard.index(bishoField[:-1])
    xMovingDirection = 1  # 1: right, -1: left (a-b-c...)
    yMovingDirection = 1  # 1: up, -1: down (1-2-3...)
    memoryForMovingField = bishoField
    if actuallSquareColour == destFieldColour and bishopColour != figureColourOnDestField and bishoField[:-1] != destField[:-1]: #check if destination square is the same colour and figure on dest field is different colour or empty
        if int(destField[-1:]) < int(bishoField[-1:]):
            yMovingDirection = -1
        if int(destField[-1:]) > int(bishoField[-1:]):
            yMovingDirection = 1
        if xAxisBoard.index(destField[:-1]) < bishopXIndexField:
            xMovingDirection = -1
        if xAxisBoard.index(destField[:-1]) > bishopXIndexField:
            xMovingDirection = 1

        movePossible = 1
        try:
            while memoryForMovingField != destField:
                memoryForMovingField = f'{xAxisBoard[(xAxisBoard.index(memoryForMovingField[:-1]) + xMovingDirection)]}{int(memoryForMovingField[-1:]) + yMovingDirection}'
                if chessBoardStatus.get(memoryForMovingField).figureColour != ' ' and memoryForMovingField != destField:
                    movePossible = 0
                    break
        except:
            movePossible = 0

    if chessBoardStatus.get(destField).figureType == 'king' and movePossible:
        movePossible = 0
        check = 1

    return movePossible, check