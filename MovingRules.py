print('#########################')


def pawnmoveenable(pawnfield, destfield, chessboardstatus):
    x = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') # x axis fields
    y = ('1', '2', '3', '4', '5', '6', '7', '8') # y axis fields
    #print (chessboardstatus.get('b3').squareColour)
    movepossible = 0
    pawncolour = chessboardstatus.get(pawnfield).figureColour
    if pawncolour == 'White':
        i = 1
    elif pawncolour == 'Black':
        i = -1

    # Move forward x1
    if chessboardstatus.get(destfield).figureType == ' ' and destfield == f'{pawnfield[:-1]}{int(pawnfield[-1:])+i}':
        movepossible = 1

    # Move forward x2
    if chessboardstatus.get(destfield).figureType == ' ' and destfield == f'{pawnfield[:-1]}{int(pawnfield[-1:]) + 2*i}':
        if (pawncolour == 'White' and pawnfield[-1:] == '2') or (pawncolour == 'Black' and pawnfield[-1:] == '7'):
            movepossible = 1

    #TODO this "Classic Capturing is not working properly (check board status after Capturing)
    # Classic Capturing
    xactuall = pawnfield[:-1]
    xdestiny = destfield[:-1]
    if ((x.index(xactuall) + 1) or (x.index(xactuall) - 1)) == x.index(xdestiny): #check if destination in x axis is +/- 1
        print ('a')
        if int(pawnfield[-1:]) + i == int(destfield[-1:]): #check if destination in y axis is +1
            print('b')
            if pawncolour == 'White' and chessboardstatus.get(destfield).figureColour == 'Black':
                movepossible = 1
            elif pawncolour == 'Black' and chessboardstatus.get(destfield).figureColour == 'White':
                movepossible = 1


    return movepossible

