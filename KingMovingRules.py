def king_move_enable(kingField, destField, chessBoardStatus):
    movePossible = 0
    xAxisBoard = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
    kingColour = chessBoardStatus.get(kingField).figureColour
    figureColourOnDestField = chessBoardStatus.get(destField).figureColour
    kingXIndexField = xAxisBoard.index(kingField[:-1])
    destXIndexField = xAxisBoard.index(destField[:-1])
    xMovingDirection = 0  # 1: right, -1: left (a-b-c...)
    yMovingDirection = 0  # 1: up, -1: down (1-2-3...)
    if int(destField[-1:]) < int(kingField[-1:]):
        yMovingDirection = -1
    if int(destField[-1:]) > int(kingField[-1:]):
        yMovingDirection = 1
    if xAxisBoard.index(destField[:-1]) < kingXIndexField:
        xMovingDirection = -1
    if xAxisBoard.index(destField[:-1]) > kingXIndexField:
        xMovingDirection = 1

    if kingColour != figureColourOnDestField: #check if figure on dest field is different colour or empty
        if (int(kingField[-1:]) + yMovingDirection) == int(destField[-1:]): #check if movement only one square in vertical
            if (kingXIndexField + xMovingDirection) == destXIndexField: #check if movement only one square in horizontal
                i = -1
                while i < 2:
                    k = -1
                    while k < 2:
                        try:
                            if chessBoardStatus.get(f'{xAxisBoard[destXIndexField + i]}{int(destField[-1:]) + k}').figureType == 'king' and\
                                    chessBoardStatus.get(f'{xAxisBoard[destXIndexField + i]}{int(destField[-1:]) + k}').figureColour != kingColour:
                                print('king is to close')
                                movePossible = 0
                                break
                            else:
                                movePossible = 1
                        except:
                            movePossible = 1
                            print('next to end board- ok')
                        k = k + 1
                    i = i + 1
                    if movePossible == 0:
                        break

    if chessBoardStatus.get(destField).figureType == 'king':
        movePossible = 0

    return movePossible