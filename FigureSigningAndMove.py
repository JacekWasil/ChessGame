from PawnMovingRules import pawn_move_enable
from KnightMovingRules import knight_move_enable
from BishopMovingRules import bishop_move_enable
from RookMovingRules import rook_move_enable
from QueenMovingRules import queen_move_enable
from KingMovingRules import king_move_enable
from FiguresInBoardMemoryForCheck import figures_position_in_memory_board
from CheckingIfCheckHappened import check_if_check_happened

from SquareGeneration import *


lastsigned = '' #last signed square
actualchoice = '' #actual signed square
figuremove = [0] #If figure move == 1 then move figure and reset this bit to 0
movedest = ['','',''] #Which figure move from where to where move figure 0-figure type, 1- from where, 2- to where
whoturn = ' '
lastsquarecolour = 'light blue'
#Figure signing
def sign_button(fieldname, chessboard):
    global lastsigned, actualchoice, figuremove, movedest, whoturn, lastsquarecolour, stillCheck
    # Block signing if pawn is at end of board and is not changed to figure
    donotsignfigure = 0

    for i in ('a', 'b','c','d','e','f','g','h'):
        if square.get(f'{i}1').figureType == 'pawn' or square.get(f'{i}8').figureType == 'pawn':
            donotsignfigure = 1

    # Chessboard reset
    if lastsquarecolour != square.get('a1').squareColour:
        lastsquarecolour = square.get('a1').squareColour
        whoturn = 'White'

    if whoturn == ' ':
        whoturn = 'White'

    if lastsigned == '':
        lastsigned = fieldname


    if donotsignfigure == 0 and ((whoturn == 'White' and square.get(fieldname).figureColour == 'White') or (whoturn == 'Black' and square.get(fieldname).figureColour == 'Black')):
        actualchoice = fieldname
        square.get(fieldname).signed = 1
        chessboard[fieldname].config(bg='yellow')
        if fieldname != lastsigned:
            square.get(lastsigned).signed = 0
            chessboard[lastsigned].config(bg=f'{square.get(lastsigned).squareColour}')

    if actualchoice != lastsigned and donotsignfigure == 0:
        lastsigned = square.get(fieldname).name

    #check if move is possible
    if donotsignfigure == 0 and lastsigned != fieldname and lastsigned != '' and \
            ((square.get(lastsigned).figureType == 'pawn' and pawn_move_enable(lastsigned, fieldname, square)[0]) or
             (square.get(lastsigned).figureType == 'knight' and knight_move_enable(lastsigned, fieldname, square)[0]) or
             (square.get(lastsigned).figureType == 'bishop' and bishop_move_enable(lastsigned, fieldname, square)[0]) or
             (square.get(lastsigned).figureType == 'rook' and rook_move_enable(lastsigned, fieldname, square)[0]) or
             (square.get(lastsigned).figureType == 'queen' and queen_move_enable(lastsigned, fieldname, square)[0]) or
             (square.get(lastsigned).figureType == 'king' and king_move_enable(lastsigned, fieldname, square))):

        if whoturn == 'White':
            x = 'w'
        else:
            x = 'b'


        ############################################ Check if after move check will happened
        figuremove[0] = 1
        movedest[0] = f'{x}{square.get(lastsigned).figureType}_img'
        movedest[1] = square.get(lastsigned).name
        movedest[2] = square.get(fieldname).name

        memoryBoardStatus = figures_position_in_memory_board((movedest[1]), movedest[2], square)
        check = ('check happened = 1', 'which figure made check?')
        check = check_if_check_happened(memoryBoardStatus, pawn_move_enable, rook_move_enable, knight_move_enable, bishop_move_enable, queen_move_enable)
        if check[0] == 1:
            #figuremove[0] = 0
            print (check[1])


        #movement can not be done cause You check Yourself
        if (whoturn == 'White' and check[1][0:14] == 'check by black') or (whoturn == 'Black' and check[1][0:14] == 'check by white'):
            #figuremove[0] = 0
            print('still check')




        ###########################################################



        if figuremove[0] == 1:
            square.get(lastsigned).signed = 0
            lastsigned = ''
            actualchoice = ''
            if whoturn == 'White':
                whoturn = 'Black'
            else:
                whoturn = 'White'

    return lastsigned, actualchoice















