import tkinter as tk
from tkinter import *
from SquareGeneration import *  # every square is a class-> example: square.get('b3').squareColour
from CreateFiguresImages import figure_image_generation
from FigureSigningAndMove import sign_button, figuremove, movedest
from FiguresInBoardMemoryForCheck import figures_position_in_memory_board
from CheckingIfCheckHappened import check_if_check_happened
from PawnMovingRules import pawn_move_enable
from RookMovingRules import rook_move_enable
from BishopMovingRules import bishop_move_enable
from KnightMovingRules import knight_move_enable
from QueenMovingRules import queen_move_enable

from PopUpFiguresWhenPawnAtEnd import show_buttons_pawn_at_end_board, choose_button_and_pawn_change_to_figure

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

endbuttonknight = Button(root, bg='red', command=lambda: figure_move(choose_button_and_pawn_change_to_figure('knight', endbuttonknight,
                                                                                                             endbuttonbishop,
                                                                                                             endbuttonrook,
                                                                                                             endbuttonqueen)))
endbuttonbishop = Button(root, bg='red', command=lambda: figure_move(choose_button_and_pawn_change_to_figure('bishop', endbuttonknight,
                                                                                                             endbuttonbishop,
                                                                                                             endbuttonrook,
                                                                                                             endbuttonqueen)))
endbuttonrook = Button(root, bg='red', command=lambda: figure_move(choose_button_and_pawn_change_to_figure('rook', endbuttonknight,
                                                                                                           endbuttonbishop, endbuttonrook,
                                                                                                           endbuttonqueen)))
endbuttonqueen = Button(root,  bg='red', command=lambda: figure_move(choose_button_and_pawn_change_to_figure('queen', endbuttonknight,
                                                                                                             endbuttonbishop,
                                                                                                             endbuttonrook,
                                                                                                             endbuttonqueen)))

###############################################   TEST    BOARD    ##############################################
labellist = {}
###############################################   END TEST BOARD   ##############################################

#print (square.get('a1').squareColour)
def change_figure_colour():
    global figureColours, turn, waitforfigurechoose



    #reset basic values
    waitforfigurechoose = 0
    figuremove[0] = 0
    endbuttonknight.place(x=-100, y=600)
    endbuttonbishop.place(x=-100, y=600)
    endbuttonrook.place(x=-100, y=600)
    endbuttonqueen.place(x=-100, y=600)
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

    squares_position()

    # place squares with right names on the board position (example: a1 is a button set as a square)
    iterator = iter(square)
    item = next(iterator, None)

    #Set figures on the board
    for x in range(64):
        #Write field names on left and on bottom side of chessboard
        (txt, posx, posy, create) = square_description(figureColours, item)
        if create == 1:
            text = Label(text=f"{txt}", bg='light green')
            text.place(x=posx, y=posy)
            if item in {'a1', 'h8'}:
                text = Label(text=f"{item[-1:]}", bg='light green')
                text.place(x=posx - 55, y=posy - 50)

        ###############################################   TEST    BOARD    ##############################################
        labellist[f'{item}'] = item
        ###############################################   END TEST BOARD   ##############################################

        fig = globals()[figure_image_generation(square.get(item).figureColour, square.get(item).figureType, square.get(item).squareColour)]

        squarebutton[item] = Button(root, text=f'{item}', bg=square.get(f'{item}').squareColour, image = fig, command= lambda x= item, y= squarebutton: sign_button(str(x), y) and figure_move())
        squarebutton[item].place(x=square.get(f'{item}').posX, y=square.get(f'{item}').posY)
        if item == 'a1' or  item == 'e1' or item == 'h1' or item == 'a8' or  item == 'e8' or item == 'h8':
            square.get(f'{item}').castlePossible = 1
        item = next(iterator, None)

        #delete the bug- after sign black and double reset chessboard it was black move first
        sign_button('a3', squarebutton)

    ###############################################   TEST    BOARD    ##############################################
    #test_board()
    ###############################################   END TEST BOARD   ##############################################




ChooseColourBtn = Button(root, text='Start', bg = 'yellow', padx=14, pady=16, command=change_figure_colour)
ChooseColourBtn.place(x=0, y=50)

###############################################   TEST    BOARD    ##############################################
def test_board():
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
lastDoubleMove = 'a1' # Inicialize
waitforfigurechoose = 0
pawnpositionforupgrate = 'Inicialize'
def figure_move(chosenfigureendboard =' '):
    global figuremove, turn, lastDoubleMove, waitforfigurechoose, pawnpositionforupgrate, figurechoosenatendofboard, \
        figures_position_in_memory_board, check_if_check_happened, pawn_move_enable, rook_move_enable, knight_move_enable, \
        bishop_move_enable, queen_move_enable


    # Check if after move check will happened
    # if figuremove[0] == 1:
    #     memoryBoardStatus = figures_position_in_memory_board(movedest[1], movedest[2], square)
    #     check = ('check happened = 1', 'which figure made check?')
    #     check = check_if_check_happened(memoryBoardStatus, pawn_move_enable, rook_move_enable, knight_move_enable, bishop_move_enable, queen_move_enable)
    #     if check[0] == 1:
    #         print (check[1])
    #     #movement can not be done cause You check Yourself
    #     if (turn == 'White' and check[1][0:14] == 'check by black') or (turn == 'Black' and check[1][0:14] == 'check by white'):
    #         figuremove[0] = 0

    if figuremove[0] == 1:
        if square.get(movedest[1]).squareColour == 'light yellow':
            squarebutton[movedest[1]].config(image=wsquare_img, bg= 'light yellow')
        else:
            squarebutton[movedest[1]].config(image=bsquare_img, bg= 'light blue')
        squarebutton[movedest[2]].config(image = img_collection[f'{movedest[0]}'])

        #Delete beating pawn after beating in fly
        if square.get(lastDoubleMove).pawnDoubleMove:
            if (movedest[2][:-1]) == (lastDoubleMove[:-1]) and ((turn == 'White' and (int(movedest[2][-1:]) - 1 == int(lastDoubleMove[-1:]))) or (turn == 'Black' and (int(movedest[2][-1:]) + 1 == int(lastDoubleMove[-1:])))):
                if square.get(lastDoubleMove).squareColour == 'light yellow':
                    squarebutton[lastDoubleMove].config(image=wsquare_img, bg='light yellow')
                else:
                    squarebutton[lastDoubleMove].config(image=bsquare_img, bg='light blue')
                square.get(lastDoubleMove).figureType = ' '
                square.get(lastDoubleMove).figureColour = ' '

        #Castle - change rook position
        if movedest[0][1:-4] == 'king' and f'{movedest[1][:-1]}' == 'e':
            if f'{movedest[2][:-1]}' == 'c':
                if turn == 'White':
                    square.get('e1').castlePossible = 0
                    squarebutton['d1'].config(image=wrook_img)
                    square.get('d1').figureType = 'rook'
                    square.get('d1').figureColour = 'White'
                    if square.get('a1').squareColour == 'light yellow':
                        squarebutton['a1'].config(image=wsquare_img)
                    else:
                        squarebutton['a1'].config(image=bsquare_img)
                    square.get('a1').figureType = ' '
                    square.get('a1').figureColour = ' '
                if turn == 'Black':
                    square.get('e8').castlePossible = 0
                    squarebutton['d8'].config(image=brook_img)
                    square.get('d8').figureType = 'rook'
                    square.get('d8').figureColour = 'Black'
                    if square.get('a8').squareColour == 'light yellow':
                        squarebutton['a8'].config(image=wsquare_img)
                    else:
                        squarebutton['a8'].config(image=bsquare_img)
                    square.get('a8').figureType = ' '
                    square.get('a8').figureColour = ' '
            if f'{movedest[2][:-1]}' == 'g':
                if turn == 'White':
                    square.get('e1').castlePossible = 0
                    squarebutton['f1'].config(image=wrook_img)
                    square.get('f1').figureType = 'rook'
                    square.get('f1').figureColour = 'White'
                    if square.get('h1').squareColour == 'light yellow':
                        squarebutton['h1'].config(image=wsquare_img)
                    else:
                        squarebutton['h1'].config(image=bsquare_img)
                    square.get('h1').figureType = ' '
                    square.get('h1').figureColour = ' '
                if turn == 'Black':
                    square.get('e8').castlePossible = 0
                    squarebutton['f8'].config(image=brook_img)
                    square.get('f8').figureType = 'rook'
                    square.get('f8').figureColour = 'Black'
                    if square.get('h8').squareColour == 'light yellow':
                        squarebutton['h8'].config(image=wsquare_img)
                    else:
                        squarebutton['h8'].config(image=bsquare_img)
                    square.get('h8').figureType = ' '
                    square.get('h8').figureColour = ' '

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

        #show 4 figures to chose after pawn reach end position
        if movedest[0][1:-4] == 'pawn' and (movedest[2][-1:] == '1' or movedest[2][-1:] == '8') and waitforfigurechoose == 0 :
            whiteorblack = movedest[0][0]
            endbuttonknight.config(image=globals()[f'{whiteorblack}knight_img'])
            endbuttonbishop.config(image = globals()[f'{whiteorblack}bishop_img'])
            endbuttonrook.config(image = globals()[f'{whiteorblack}rook_img'])
            endbuttonqueen.config(image = globals()[f'{whiteorblack}queen_img'])
            show_buttons_pawn_at_end_board(endbuttonknight, endbuttonbishop, endbuttonrook, endbuttonqueen)
            pawnpositionforupgrate = movedest[2]
            waitforfigurechoose = 1


        # change pawn to choosen figure
        if chosenfigureendboard != ' ' and waitforfigurechoose == 1:
            squarebutton[pawnpositionforupgrate].config(image=globals()[f'{turn[:-4].lower()}{chosenfigureendboard}_img'])
            #change position in board memory
            square.get(pawnpositionforupgrate).figureType = chosenfigureendboard
            waitforfigurechoose = 0
            #Check if at end position pawn will check after promotion
            sign_button(movedest[2], square, 1)

        if waitforfigurechoose == 0:
            figuremove[0] = 0
            if turn == 'White':
                turn = 'Black'
            else:
                turn = 'White'

        turdiplay = Label(text=f" It is {turn} turn", bg='light green')
        turdiplay.place(x=0, y=0)

    ###############################################   TEST    BOARD    ##############################################
    #test_board()
    ###############################################   END TEST BOARD   ##############################################



root.mainloop()
