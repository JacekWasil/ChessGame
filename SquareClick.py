from Squares import *
from MovingRules import pawnmoveenable

lastsigned = '' #last signed square
actualchoice = '' #actual signed square
figuremove = [0] #If figure move == 1 then move figure and reset this bit to 0
movedest = ['','',''] #Which figure move from where to where move figure 0-figure type, 1- from where, 2- to where
whoturn = ''


#Figure signing
def signebutton(fieldname, whostart, chessboard):
    global lastsigned, actualchoice, figuremove, movedest, whoturn
    if whoturn == '':
        whoturn = whostart

    if lastsigned == '':
        lastsigned = fieldname

    if (whoturn == 'White' and square.get(fieldname).figureColour == 'White') or (whoturn == 'Black' and square.get(fieldname).figureColour == 'Black'):
        actualchoice = fieldname
        square.get(fieldname).signed = 1
        chessboard[fieldname].config(bg='yellow')
        if fieldname != lastsigned:
            square.get(lastsigned).signed = 0
            chessboard[lastsigned].config(bg=f'{square.get(lastsigned).squareColour}')


    if actualchoice != lastsigned:
        lastsigned = square.get(fieldname).name

    #print(f'actulchoice: {actualchoice}, lastsigned: {lastsigned}')
    if lastsigned != fieldname and lastsigned != '':# and pawnmoveenable(lastsigned, actualchoice, chessboard): #warunek z dupy do zmiany
        if whoturn == 'White':
            x = 'w'
        else:
            x = 'b'

        figuremove[0] = 1
        movedest[0] = f'{x}{square.get(lastsigned).figureType}_img'
        movedest[1] = square.get(lastsigned).name
        movedest[2] = square.get(fieldname).name

        square.get(lastsigned).signed = 0
        lastsigned = ''
        actualchoice = ''

        if whoturn == 'White':
            whoturn = 'Black'
        else:
            whoturn = 'White'

    return lastsigned, actualchoice















