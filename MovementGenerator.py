# Function is giving possible movements after check to check if check mate occured
from PawnMovingRules import pawn_move_enable
from KnightMovingRules import knight_move_enable
from BishopMovingRules import bishop_move_enable
from RookMovingRules import rook_move_enable
from QueenMovingRules import queen_move_enable
from KingMovingRules import king_move_enable

def movement_generator(fieldName, chessBoardStatus):
    horizontal = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
    vertical = ('1', '2', '3', '4', '5', '6', '7', '8')  # y axis fields
    possibitiesToMove = []

    for x in horizontal:
        for y in vertical:
            square = f'{x}{y}'
            if square != fieldName:
                if ((chessBoardStatus.get(fieldName).figureType == 'pawn' and pawn_move_enable(fieldName, square, chessBoardStatus)[0]) or
                    (chessBoardStatus.get(fieldName).figureType == 'knight' and knight_move_enable(fieldName, square, chessBoardStatus)[0]) or
                    (chessBoardStatus.get(fieldName).figureType == 'bishop' and bishop_move_enable(fieldName, square, chessBoardStatus)[0]) or
                    (chessBoardStatus.get(fieldName).figureType == 'rook' and rook_move_enable(fieldName, square, chessBoardStatus)[0]) or
                    (chessBoardStatus.get(fieldName).figureType == 'queen' and queen_move_enable(fieldName, square, chessBoardStatus)[0]) or
                    (chessBoardStatus.get(fieldName).figureType == 'king' and king_move_enable(fieldName, square, chessBoardStatus))):
                    possibitiesToMove.append(square)

    return possibitiesToMove

