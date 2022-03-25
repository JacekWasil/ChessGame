def check_if_check_happened(chessBoardStatus, pawnMovingRules, rookMovingRules, knightMovingRules, bishopMovingRules, queenMovingRules):
    horizontal = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # x axis fields
    vertical = ('1', '2', '3', '4', '5', '6', '7', '8')  # y axis fields
    whiteKingPosition = ' '
    blackKingPosition = ' '
    check = 0
    checkInformation = 'Who checked'
    #Find king position:
    for x in horizontal:
        for y in vertical:
            square = f'{x}{y}'
            if chessBoardStatus.get(square).figureType == 'king':
                if chessBoardStatus.get(square).figureColour == 'White':
                    whiteKingPosition = square
                if chessBoardStatus.get(square).figureColour == 'Black':
                    blackKingPosition = square

    #check if check happened
    for x in horizontal:
        for y in vertical:
            square = f'{x}{y}'
            # Check for pawn
            if chessBoardStatus.get(square).figureType == 'pawn':
                if chessBoardStatus.get(square).figureColour == 'White':
                    if (pawnMovingRules(square, blackKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by white pawn'
                if chessBoardStatus.get(square).figureColour == 'Black':
                    if (pawnMovingRules(square, whiteKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by black pawn'
            # Check for rook
            if chessBoardStatus.get(square).figureType == 'rook':
                if chessBoardStatus.get(square).figureColour == 'White':
                    if (rookMovingRules(square, blackKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by white rook'
                if chessBoardStatus.get(square).figureColour == 'Black':
                    if (rookMovingRules(square, whiteKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by black rook'
            # Check for knight
            if chessBoardStatus.get(square).figureType == 'knight':
                if chessBoardStatus.get(square).figureColour == 'White':
                    if (knightMovingRules(square, blackKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by white knight'
                if chessBoardStatus.get(square).figureColour == 'Black':
                    if (knightMovingRules(square, whiteKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by black knight'
            # Check for bishop
            if chessBoardStatus.get(square).figureType == 'bishop':
                if chessBoardStatus.get(square).figureColour == 'White':
                    if (bishopMovingRules(square, blackKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by white bishop'
                if chessBoardStatus.get(square).figureColour == 'Black':
                    if (bishopMovingRules(square, whiteKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by black bishop'
            # Check for queen
            if chessBoardStatus.get(square).figureType == 'queen':
                if chessBoardStatus.get(square).figureColour == 'White':
                    if (queenMovingRules(square, blackKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by white queen'
                if chessBoardStatus.get(square).figureColour == 'Black':
                    if (queenMovingRules(square, whiteKingPosition, chessBoardStatus))[1] == 1:
                        check = 1
                        checkInformation = 'check by black queen'

    return check, checkInformation



