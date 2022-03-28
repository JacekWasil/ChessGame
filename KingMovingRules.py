from PawnMovingRules import pawn_move_enable
from KnightMovingRules import knight_move_enable
from BishopMovingRules import bishop_move_enable
from RookMovingRules import rook_move_enable
from QueenMovingRules import queen_move_enable

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
                                #print('king is to close')
                                movePossible = 0
                                break
                            else:
                                movePossible = 1
                        except:
                            movePossible = 1
                            #print('next to end board but ok')
                        k = k + 1
                    i = i + 1
                    if movePossible == 0:
                        break

    if chessBoardStatus.get(kingField).castlePossible and (kingXIndexField + 2 == destXIndexField or kingXIndexField - 2 == destXIndexField) and kingField[-1:] == destField[-1:]:
        if (chessBoardStatus.get(f'a{kingField[-1:]}').castlePossible and \
                chessBoardStatus.get(f'b{kingField[-1:]}').figureType == ' ' and \
                chessBoardStatus.get(f'c{kingField[-1:]}').figureType == ' ' and \
                chessBoardStatus.get(f'd{kingField[-1:]}').figureType == ' '):
            movePossible = 1

            #Check if any figure is attacking castle fields
            horizontal = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
            vertical = ('1', '2', '3', '4', '5', '6', '7', '8')  # y axis fields
            fieldToCheckForCastle = [(f'a{kingField[-1:]}'),(f'b{kingField[-1:]}'),(f'c{kingField[-1:]}'),(f'd{kingField[-1:]}')]
            if kingColour == 'White':
                oppositeKingPositionY = 2
            else:
                oppositeKingPositionY = 7
            for x in horizontal:
                for y in vertical:
                    if chessBoardStatus.get(f'{x}{y}').figureColour != kingColour:
                        choosenFigureFieldForAttackCastleplaces = f'{x}{y}'
                        for i in fieldToCheckForCastle:
                            if (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'pawn' and pawn_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or \
                                (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'knight' and knight_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or\
                                (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'bishop' and bishop_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or\
                                (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'rook' and rook_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or\
                                (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'queen' and queen_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or \
                                (chessBoardStatus.get(f'a{oppositeKingPositionY}').figureType == 'king') or (chessBoardStatus.get(f'b{oppositeKingPositionY}').figureType == 'king') or\
                                (chessBoardStatus.get(f'c{oppositeKingPositionY}').figureType == 'king'):
                                movePossible = 0

        if (chessBoardStatus.get(f'h{kingField[-1:]}').castlePossible and \
                chessBoardStatus.get(f'f{kingField[-1:]}').figureType == ' ' and \
                chessBoardStatus.get(f'g{kingField[-1:]}').figureType == ' '):
            movePossible = 1

            # Check if any figure is attacking castle fields
            horizontal = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
            vertical = ('1', '2', '3', '4', '5', '6', '7', '8')  # y axis fields
            fieldToCheckForCastle = [(f'f{kingField[-1:]}'), (f'g{kingField[-1:]}'), (f'h{kingField[-1:]}')]
            if kingColour == 'White':
                oppositeKingPositionY = 2
            else:
                oppositeKingPositionY = 7
            for x in horizontal:
                for y in vertical:
                    if chessBoardStatus.get(f'{x}{y}').figureColour != kingColour:
                        choosenFigureFieldForAttackCastleplaces = f'{x}{y}'
                        for i in fieldToCheckForCastle:
                            if (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'pawn' and
                                pawn_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or \
                                    (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'knight' and knight_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or \
                                    (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'bishop' and bishop_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or \
                                    (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'rook' and rook_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or \
                                    (chessBoardStatus.get(choosenFigureFieldForAttackCastleplaces).figureType == 'queen' and queen_move_enable(choosenFigureFieldForAttackCastleplaces, i, chessBoardStatus)[0]) or \
                                    (chessBoardStatus.get(f'g{oppositeKingPositionY}').figureType == 'king') or (chessBoardStatus.get(f'h{oppositeKingPositionY}').figureType == 'king'):
                                movePossible = 0

    if chessBoardStatus.get(destField).figureType == 'king':
        movePossible = 0

    return movePossible