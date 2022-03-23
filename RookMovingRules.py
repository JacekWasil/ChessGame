
def rook_move_enable(rookField, destField, chessBoardStatus):
    check = 0
    movePossible = 0
    xAxisBoard = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
    rookColour = chessBoardStatus.get(rookField).figureColour
    figureColourOnDestField = chessBoardStatus.get(destField).figureColour
    rookXIndexField = xAxisBoard.index(rookField[:-1])
    xMovingDirection = 0  # 1: right, -1: left (a-b-c...)
    yMovingDirection = 0  # 1: up, -1: down (1-2-3...)
    memoryForMovingField = rookField
    if figureColourOnDestField != rookColour and  (rookField[:-1] == destField[:-1] or rookField[-1:] == destField[-1:]): #check if movement is only in horizontal or only vertical direction and dest figure colour is different than rook colour
        if int(destField[-1:]) < int(rookField[-1:]):
            yMovingDirection = -1
        if int(destField[-1:]) > int(rookField[-1:]):
            yMovingDirection = 1
        if xAxisBoard.index(destField[:-1]) < rookXIndexField:
            xMovingDirection = -1
        if xAxisBoard.index(destField[:-1]) > rookXIndexField:
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
