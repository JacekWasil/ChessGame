print('#########################')


def pawnmoveenable(pawnfield, destfield, chessboardstatus):
    x = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') # x axis fields
    y = ('1', '2', '3', '4', '5', '6', '7', '8') # y axis fields
    movepossible = 0
    pawncolour = chessboardstatus.get(pawnfield).figureColour
    if pawncolour == 'White':
        i = 1
    elif pawncolour == 'Black':
        i = -1

    #Move forward x1
    if chessboardstatus.get(destfield).figureType == ' ' and destfield == f'{pawnfield[:-1]}{pawnfield[-1:]+i}':
        movepossible = 1

    return movepossible

