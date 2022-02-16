figureColours = 'White'
square = {} #set of all squers from a1 to h8 as a clesses

class SquareClass():
    def __init__(self, name, posX=0, posY=0, squareColour=' ', figureColour=' ', figureType=' ', signed= 0):
        self.name = name
        self.posX = posX
        self.posY = posY
        self.squareColour = squareColour
        self.figureColour = figureColour
        self.figureType = figureType
        self.signed = signed

def squaresPosition():
    global figureColours
    i = 1
    if figureColours == 'White':
        figureColours = 'Black'
        squareColour = 'light yellow'
    else:
        squareColour = 'light blue'
        figureColours = 'White'

    while i <= 8:
        #square position in X axis
        fieldLetter = ' '
        offsetXPosValue = 66
        if i == 1:
            positionX = 100
            if figureColours == 'White':
                fieldLetter = 'a'
            else:
                fieldLetter = 'h'
        elif i == 2:
            positionX = positionX + offsetXPosValue
            if figureColours == 'White':
                fieldLetter = 'b'
            else:
                fieldLetter = 'g'
        elif i == 3:
            positionX = positionX + offsetXPosValue
            if figureColours == 'White':
                fieldLetter = 'c'
            else:
                fieldLetter = 'f'
        elif i == 4:
            positionX = positionX + offsetXPosValue
            if figureColours == 'White':
                fieldLetter = 'd'
            else:
                fieldLetter = 'e'
        elif i == 5:
            positionX = positionX + offsetXPosValue
            if figureColours == 'White':
                fieldLetter = 'e'
            else:
                fieldLetter = 'd'
        elif i == 6:
            positionX = positionX + offsetXPosValue
            if figureColours == 'White':
                fieldLetter = 'f'
            else:
                fieldLetter = 'c'
        elif i == 7:
            positionX = positionX + offsetXPosValue
            if figureColours == 'White':
                fieldLetter = 'g'
            else:
                fieldLetter = 'b'
        elif i == 8:
            positionX = positionX + offsetXPosValue
            if figureColours == 'White':
                fieldLetter = 'h'
            else:
                fieldLetter = 'a'

        for x in range(1,9):
            # square position in Y axis
            offsetYPosValue = 66
            if x == 1:
                positionY = 500
            elif x == 2:
                positionY = positionY - offsetYPosValue
            elif x == 3:
                positionY = positionY - offsetYPosValue
            elif x == 4:
                positionY = positionY - offsetYPosValue
            elif x == 5:
                positionY = positionY - offsetYPosValue
            elif x == 6:
                positionY = positionY - offsetYPosValue
            elif x == 7:
                positionY = positionY - offsetYPosValue
            elif x == 8:
                positionY = positionY - offsetYPosValue

            tempList = [9, 8, 7, 6, 5, 4, 3, 2, 1]
            if figureColours == 'White':
                k = f'{fieldLetter}{x}'
            else:
                k = f'{fieldLetter}{tempList[x]}'

            figtype = ' '
            if (int(k[-1:]) == 2) or (int(k[-1:]) == 7):
                figtype = 'pawn'
            if (k == 'a1') or (k == 'h1') or (k == 'a8') or (k == 'h8'):
                figtype = 'rook'
            if (k == 'b1') or (k == 'g1') or (k == 'b8') or (k == 'g8'):
                figtype = 'knight'
            if (k == 'c1') or (k == 'f1') or (k == 'c8') or (k == 'f8'):
                figtype = 'bishop'
            if (k == 'd1') or (k == 'd8'):
                figtype = 'queen'
            if (k == 'e1') or (k == 'e8'):
                figtype = 'king'
            figcol = ' '
            if (int(k[-1:]) == 1) or (int(k[-1:]) == 2):
                figcol = 'White'
            if (int(k[-1:]) == 7) or (int(k[-1:]) == 8):
                figcol = 'Black'

            square[f"{k}"] = SquareClass(name=f'{k}', posX=positionX, posY=positionY, squareColour=squareColour, figureColour=figcol, figureType=figtype)

            if squareColour == 'light blue' and x != 8:
                squareColour = 'light yellow'
            elif squareColour == 'light yellow' and x != 8:
                squareColour = 'light blue'

        i += 1

squaresPosition()

def squaredescrpt(figcol = '', item = '', text='', posx= 0, posy= 0, create= 0):
    text = '  '
    if figcol == 'White':
        if item in {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'}:
            text = f"{item[-1:]}"
            posx = square.get(f'{item}').posX - 30
            posy = square.get(f'{item}').posY + 25
            create = 1
        if item in {'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'}:
            text = f"{item[:-1]}"
            posx = square.get(f'{item}').posX + 25
            posy = square.get(f'{item}').posY + 80
            create = 1
    if figcol == 'Black':
        if item in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'}:
            text = f"{item[-1:]}"
            posx = square.get(f'{item}').posX - 30
            posy = square.get(f'{item}').posY + 25
            create = 1
        if item in {'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'}:
            text = f"{item[:-1]}"
            posx = square.get(f'{item}').posX + 25
            posy = square.get(f'{item}').posY + 80
            create = 1
    return text, posx, posy, create
