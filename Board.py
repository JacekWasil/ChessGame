import tkinter as tk
from tkinter import *
from Squares import *  # every square is a class-> example: square.get('b3').squareColour
from CreateFigures import figgeneration
from SquareClick import signebutton, figuremove, movedest
from PopUpFigures import createbuttonspawnatendboard, deletebuttonandpawnchangefig

gameisstarting = 1
turn = ' '#who is moving now (White or Black)
root = tk.Tk()
root.geometry('1200x900')
root.configure(bg="light green")
squarebutton = {} #collected all squares buttons

#Generate figures images
wpawn_img = PhotoImage(file=f'Figure/w_pawn.png')
wrook_img = PhotoImage(file=f'Figure/w_rook.png')
wknight_img = PhotoImage(file=f'Figure/w_knight.png')
wbishop_img = PhotoImage(file=f'Figure/w_bishop.png')
wqueen_img = PhotoImage(file=f'Figure/w_queen.png')
wking_img = PhotoImage(file=f'Figure/w_king.png')
bpawn_img = PhotoImage(file=f'Figure/b_pawn.png')
brook_img = PhotoImage(file=f'Figure/b_rook.png')
bknight_img = PhotoImage(file=f'Figure/b_knight.png')
bbishop_img = PhotoImage(file=f'Figure/b_bishop.png')
bqueen_img = PhotoImage(file=f'Figure/b_queen.png')
bking_img = PhotoImage(file=f'Figure/b_king.png')
wsquare_img = PhotoImage(file=f'Figure/w_square.png')
bsquare_img = PhotoImage(file=f'Figure/b_square.png')

img_collection = {'wpawn_img' : wpawn_img, 'wrook_img' : wrook_img, 'wknight_img' : wknight_img, 'wbishop_img' : wbishop_img, 'wqueen_img' : wqueen_img,
                  'wking_img' : wking_img, 'bpawn_img' : bpawn_img, 'brook_img' : brook_img, 'bknight_img' : bknight_img, 'bbishop_img' : bbishop_img,
                  'bqueen_img' : bqueen_img, 'bking_img' : bking_img, 'wsquare_img' : wsquare_img, 'bsquare_img' : bsquare_img}


###############################################   TEST    BOARD    ##############################################
labellist = {}
###############################################   END TEST BOARD   ##############################################

#print (square.get('a1').squareColour)
def changeFiguresColour():
    global figureColours, turn

    turn = 'White'
    if figureColours == 'White':
        figureColours = 'Black'
        ChooseColourBtn['text'] = 'Black'

    else:
        figureColours = 'White'
        ChooseColourBtn['text'] = 'White'

    # Display information who's turn
    turdiplay = Label(text=f" It is {turn} turn", bg='light green')
    turdiplay.place(x=0, y=0)

    squaresPosition()

    # place squares with right names on the board position (example: a1 is a button set as a square)
    iterator = iter(square)
    item = next(iterator, None)

    #Set figures on the board
    for x in range(64):
        #Write field names on left and on bottom side of chessboard
        (txt, posx, posy, create) = squaredescrpt(figureColours, item)
        if create == 1:
            text = Label(text=f"{txt}", bg='light green')
            text.place(x=posx, y=posy)
            if item in {'a1', 'h8'}:
                text = Label(text=f"{item[-1:]}", bg='light green')
                text.place(x=posx - 55, y=posy - 50)

        ###############################################   TEST    BOARD    ##############################################
        labellist[f'{item}'] = item
        ###############################################   END TEST BOARD   ##############################################

        fig = globals()[figgeneration(square.get(item).figureColour, square.get(item).figureType, square.get(item).squareColour)]

        squarebutton[item] = Button(root, text=f'{item}', bg=square.get(f'{item}').squareColour, image = fig, command= lambda x= item, y= squarebutton: signebutton(str(x), y) and figmove())
        squarebutton[item].place(x=square.get(f'{item}').posX, y=square.get(f'{item}').posY)
        item = next(iterator, None)



    ###############################################   TEST    BOARD    ##############################################
    testboard()
    ###############################################   END TEST BOARD   ##############################################


ChooseColourBtn = Button(root, text='Start', bg = 'yellow', padx=14, pady=16, command=changeFiguresColour)
ChooseColourBtn.place(x=0, y=50)


#TODO finish it - try with root2
###################################################################################################################################################################

endbuttonknight = Button(root, text='B1', bg='blue', image = wknight_img, padx=14, pady=16, command= lambda: deletebuttonandpawnchangefig('knight', endbuttonknight, endbuttonbishop, endbuttonrook, endbuttonqueen))
endbuttonbishop = Button(root, text='B1', bg='blue',image = wbishop_img,padx=14, pady=16, command= lambda: deletebuttonandpawnchangefig('bishop',endbuttonknight, endbuttonbishop, endbuttonrook, endbuttonqueen))
endbuttonrook = Button(root, text='B1', bg='blue', image = wrook_img,padx=14, pady=16, command= lambda: deletebuttonandpawnchangefig('rook', endbuttonknight, endbuttonbishop, endbuttonrook, endbuttonqueen))
endbuttonqueen = Button(root, text='B1', bg='blue', image = wqueen_img,padx=14, pady=16, command= lambda: deletebuttonandpawnchangefig('queen', endbuttonknight, endbuttonbishop, endbuttonrook, endbuttonqueen))

temporarybutton = Button(root, text='Temporary \n Button', bg = 'red', padx=14, pady=16, command= lambda: createbuttonspawnatendboard(endbuttonknight, endbuttonbishop, endbuttonrook, endbuttonqueen))
temporarybutton.place(x=800, y=50)


###################################################################################################################################################################

###############################################   TEST    BOARD    ##############################################
def testboard():
    for i in labellist:
        tempclear = '          '
        tempfigcolour = square.get(f'{i}').figureColour
        tempfigtype = square.get(f'{i}').figureType
        if square.get(f'{i}').figureColour == ' ' and square.get(f'{i}').figureType == ' ':
            tempfigcolour = tempclear
            tempfigtype = tempclear
        labellist[i] = Label(text= f'{tempfigcolour} \n{tempfigtype} \n{square.get(i).pawnDoubleMove}', bg='light green')
        labellist[i].place(x=square.get(f'{i}').posX + 550, y=square.get(f'{i}').posY + 18)
###############################################   END TEST BOARD   ##############################################



#display figure move
lastDoubleMove = 'a1'
def figmove():
    global figuremove, turn, lastDoubleMove

    if figuremove[0] == 1:

        if square.get(movedest[1]).squareColour == 'light yellow':
            squarebutton[movedest[1]].config(image=wsquare_img, bg= 'light yellow')
        else:
            squarebutton[movedest[1]].config(image=bsquare_img, bg= 'light blue')
        squarebutton[movedest[2]].config(image = img_collection[f'{movedest[0]}'])

        #TODO This function has to be fixed
        #Delete beating pawn after beating in fly
        if square.get(lastDoubleMove).pawnDoubleMove:
            if (movedest[2][:-1]) == (lastDoubleMove[:-1]) and ((turn == 'White' and (int(movedest[2][-1:]) - 1 == int(lastDoubleMove[-1:]))) or (turn == 'Black' and (int(movedest[2][-1:]) + 1 == int(lastDoubleMove[-1:])))):
                if square.get(lastDoubleMove).squareColour == 'light yellow':
                    squarebutton[lastDoubleMove].config(image=wsquare_img, bg='light yellow')
                else:
                    squarebutton[lastDoubleMove].config(image=bsquare_img, bg='light blue')
                square.get(lastDoubleMove).figureType = ' '
                square.get(lastDoubleMove).figureColour = ' '









        #Change figures position in chessboard memory
        square.get(movedest[1]).figureType = ' '
        square.get(movedest[1]).figureColour = ' '
        square.get(movedest[2]).figureType = movedest[0][1:-4]
        if turn == 'White':
            square.get(movedest[2]).figureColour = 'White'
        else:
            square.get(movedest[2]).figureColour = 'Black'

        # Save double move for pawn in chessboard memory
        square.get(lastDoubleMove).pawnDoubleMove = 0
        if movedest[0][1:-4] == 'pawn':
            if (int(movedest[1][-1:]) + 2 == int(movedest[2][-1:])) or (
                    int(movedest[1][-1:]) - 2 == int(movedest[2][-1:])):
                square.get(movedest[2]).pawnDoubleMove = 1
                lastDoubleMove = movedest[2]


        figuremove[0] = 0
        if turn == 'White':
            turn = 'Black'
        else:
            turn = 'White'
        turdiplay = Label(text=f" It is {turn} turn", bg='light green')
        turdiplay.place(x=0, y=0)

        ###############################################   TEST    BOARD    ##############################################
        testboard()
        ###############################################   END TEST BOARD   ##############################################











###############

#TODO
# print(square.get('a1').squareColour)
# WhitePawn1.place(x=square.get('a1').posX, y=square.get('a1').posY)
# dupa = PhotoImage(file=f'Figure/w_queen.png')


root.mainloop()
