
class pychess():
    # FIXME things like checkmate, stalemate, and promotion
    
    """
     * positive is white
     * negative is black
     * 
     * 1 -- pawn
     * 2 -- rook
     * 3 -- knight
     * 4 -- bishop
     * 5 -- queen
     * 6 -- king
     * 0 -- empty square
     * 
     *::-2, -3, -4, -5, -6, -4, -3, -2
     *    :-1, -1, -1, -1, -1, -1, -1, -1
     *    : 0,  0,  0,  0,  0,  0,  0,  0
     *    : 0,  0,  0,  0,  0,  0,  0,  0
     *    : 0,  0,  0,  0,  0,  0,  0,  0
     *    : 0,  0,  0,  0,  0,  0,  0,  0
     *    : 1,  1,  1,  1,  1,  1,  1,  1
     * : 2,  3,  4,  5,  6,  4,  3,  2
     
    
    self.board
    self.canEnPassant #:row, col, resetNextTurn if no row/col, set to -1. reset on 1, don't on 0
    self.whiteToMove
    self.canCastle #: [whiteKingside, whiteQueenside, blackKingside, blackQueenside] boolean array
    """
    # constructor # # # # # # # # # # # # # # # # # 
    
    def __init__(self, board_setup = None, to_move = True):
        
        if(board_setup == None):
            self.board = [[-2, -3, -4, -5, -6, -4, -3, -2],[-1, -1, -1, -1, -1, -1, -1, -1],[ 0,  0,  0,  0,  0,  0,  0,  0],[ 0,  0,  0,  0,  0,  0,  0,  0],[ 0,  0,  0,  0,  0,  0,  0,  0],[ 0,  0,  0,  0,  0,  0,  0,  0],[ 1,  1,  1,  1,  1,  1,  1,  1],[ 2,  3,  4,  5,  6,  4,  3,  2]]
        else:
            self.board = board_setup
        
        self.whiteToMove = to_move
        
        self.canEnPassant = [-1, -1, 0]
        self.canCastle = [True, True, True, True]
        
    
    
    # methods # # # # # # # # # # # # # # # # # 
    # returns int[][] of current board position
    def getBoard(self): 
        return self.board.deepcopy()
    
    def kingInDanger(currentTurn):
        # if currentTurn is True, returns if the king is in danger for player whose turn it is
        # if currentTurn is False, returns if the king is in danger for player whose turn it is not
        sign = 0
        kingRow = -1
        kingCol = -1
        
        if(currentTurn == whiteToMove):
            sign = 1
        else:
            sign = -1
        
        
        # find king
        for row in range(8):
            for col in range(8):
                if(board[row][col] == sign * 6):
                    kingRow = row
                    kingCol = col
                
            
        
        
        if(kingRow == -1 or kingCol == -1):
            # self should be an exception?
            return False
        
        
        # check enemy knights
        for row in range(-2, 3, 1):
            for col in range(-2, 3, 1):
                if(not outOfBounds(kingRow + row, kingCol + col) and Math.abs(row*col) == 2):
                    if(board[kingRow + row][kingCol + col] == sign * -3):
                        return True
                    
                
            
        
        
        # check for danger by enemy king
        for row in range(-1, 2):
            for col in range(-1, 2):
                if(not outOfBounds(kingRow + row, kingCol + col)):
                    if(board[kingRow + row][kingCol + col] == sign * -6):
                        return True
                    
                
            
        
        
        # check up and down
        for row in range(1, 7):
            if(not outOfBounds(kingRow + row, kingCol)):
                tempPiece =  board[kingRow + row][kingCol]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        for row in range(1, 7):
            if(not outOfBounds(kingRow - row, kingCol)):
                tempPiece =  board[kingRow - row][kingCol]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        # check left and right
        for col in range(1, 7):
            if(not outOfBounds(kingRow, kingCol + col)):
                tempPiece =  board[kingRow][kingCol + col]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        for col in range(1, 7):
            if(not outOfBounds(kingRow, kingCol - col)):
                tempPiece =  board[kingRow][kingCol - col]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        # check down-right
        for i in range(1, 7):
            if(not outOfBounds(kingRow + i, kingCol + i)):
                tempPiece =  board[kingRow + i][kingCol + i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        # check up-left
        for i in range(1, 7):
            if(not outOfBounds(kingRow - i, kingCol - i)):
                tempPiece =  board[kingRow - i][kingCol - i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        # check down-left
        for i in range(1, 7):
            if(not outOfBounds(kingRow + i, kingCol - i)):
                tempPiece =  board[kingRow + i][kingCol - i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        # check up-right
        for i in range(1, 7):
            if(not outOfBounds(kingRow - i, kingCol + i)):
                tempPiece =  board[kingRow - i][kingCol + i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        return False 
    
    def kingInDanger(pychessboard, currentTurn):
        return pychessboard.kingInDanger(currentTurn) # returns True if king is in danger on board b for specified turn
    
    def move(self, startRow, startCol, endRow, endCol):
        
        # if valid move
        if(checkMove(startRow, startCol, endRow, endCol)):
            movePiece(startRow, startCol, endRow, endCol)
            return True
        
        
        return False
    
    def toString():
        output = "________________________________________________\n"
        for row in range(8):
            output += "|     |     |     |     |     |     |     |     |\n"
            for col in range(8):
                if(board[row][col] == 0):
                    output+="|     "
                else:
                    if(board[row][col] < 0):
                        output += "| "
                    else:
                        output += "|  "
                    
                    output+=board[row][col] + "  "
                
            
            output +="|\n"
            output += "|_____|_____|_____|_____|_____|_____|_____|_____|\n"
        
        return output
    
    def clone(self):
        output = pychess()
        
        output.whiteToMove = self.whiteToMove
        
        for i in range(3):
            output.canEnPassant[i] = self.canEnPassant[i]
        
        
        output.copyBoard(self)
        
        return output
    
    """
     * self function returns a list of all possible moves for the piece at the given square.
     * Does take turn into account
     * 
     * @param row the current row of piece
     * @param col the current column of piece
     * @return List of containing the endRow and endCol of each possible move
     """
    def getMoves(row, col):
        piece = board[row][col]
        
        if(piece == 1 or piece == -1):
            return getMovesPawn(row, col)
        elif(piece == 2 or piece == -2):
            return getMovesRook(row, col)
        elif(piece == 3 or piece == -3):
            return getMovesKnight(row, col)
        elif(piece == 4 or piece == -4):
            return getMovesBishop(row, col)
        elif(piece == 5 or piece == -5):
            return getMovesQueen(row, col)
        elif(piece == 6 or piece == -6):
            return getMovesKing(row, col)
        else:
            return []
        
    
    ## returns a list of all possible moves. each move is a list [current_row, current_col, end_row, end_col]
    def getAllMoves(CurrentTurn):
        # TODO implement
        # TODO change get moves method to return array list of arrays
        # of the form:startRow, startCol, endRow, endCol
        return []
    
    # methods # # # # # # # # # # # # # # # # # 
    
    def castle(color, dir):
        if(color.equals("white")):
            self.canCastle[0] = False
            self.canCastle[1] = False
            if(dir.equals("kingside")):
                self.board[7][7] = 0
                self.board[7][5] = 2
            else:
                self.board[7][0] = 0
                self.board[7][3] = 2
            
        else:
            self.canCastle[2] = False
            self.canCastle[3] = False
            if(dir.equals("kingside")):
                self.board[0][7] = 0
                self.board[0][5] = -2
            else:
                self.board[0][0] = 0
                self.board[0][3] = -2
            
        
    
    def enPassant(row, col):
        board[row][col] = 0
    
    def movePiece(startRow, startCol, endRow, endCol): # TODO check movePiece
        
        # reset enPassant if reset flag is set
        if(canEnPassant[2] != 0):
            canEnPassant = getNewEnPassant()
        
        
        canEnPassant[2] = 1 # reset next move
        
        piece = board[startRow][startCol]
        
        if(piece == 6 and endRow == 7 and startRow == 7 and startCol == 4 and endCol == 7 and board[7][7] == 2):
            castle("white", "kingside")
        elif(piece == -6 and endRow == 0 and startRow == 0 and startCol == 4 and endCol == 7 and board[0][7] == -2):
            castle("black", "kingside")
        elif(piece == 6 and endRow == 7 and startRow == 7 and startCol == 4 and endCol == 2 and board[7][0] == 2):
            castle("white", "Queenside")
        elif(piece == -6 and endRow == 0 and startRow == 0 and startCol == 4 and endCol == 2 and board[0][0] == -2):
            castle("black", "Queenside")
        elif(piece > 0 and not outOfBounds(endRow + 1, endCol) and isEnemySquare(piece, endRow + 1, endCol) and canEnPassant[0] == endRow + 1 and canEnPassant[1] == endCol):
            enPassant(endRow + 1, endCol)
        elif(piece < 0 and not outOfBounds(endRow - 1, endCol) and isEnemySquare(piece, endRow - 1, endCol) and canEnPassant[0] == endRow - 1 and canEnPassant[1] == endCol):
            enPassant(endRow - 1, endCol)
        
        
        
        board[startRow][startCol] = 0 # move piece
        board[endRow][endCol] = piece
        whiteToMove = not whiteToMove
    
    def movePieceNoCheck(startRow, startCol, endRow, endCol): # returns a new pychess object with the piece moved regardless if it is a legal move
        output = self.clone() # clone is redundant but for safety
        output.movePiece(startRow, startCol, endRow, endCol)
        return output
    
    def checkMove(startRow, startCol, endRow, endCol):
        
        piece = board[startRow][startCol]
        
        # if incorrect turn
        if(piece < 0 == whiteToMove):
            return False
        
        
        # if starting or ending squares are out of bounds
        if(outOfBounds(startRow, startCol) or outOfBounds(endRow, endCol)):
            return False
        
        
        # if starting and ending squares are the same
        if(startRow == endRow and startCol == endCol):
            return False
        
        
        # if ending square is occupied by friendly piece
        if(piece*board[endRow][endCol] > 0):
            return False
        
        
        # if king is in danger after move is completed
        turnComplete = self.clone().movePieceNoCheck(startRow, startCol, endRow, endCol) 
        if(kingInDanger(turnComplete, False)):
            return False
        

        if(piece == 1 or piece == -1):
            return checkMovePawn(startRow, startCol, endRow, endCol)
        elif(piece == 2 or piece == -2):
            return checkMoveRook(startRow, startCol, endRow, endCol)
        elif(piece == 3 or piece == -3):
            return checkMoveKnight(startRow, startCol, endRow, endCol)
        elif(piece == 4 or piece == -4):
            return checkMoveBishop(startRow, startCol, endRow, endCol)
        elif(piece == 5 or piece == -5):
            return checkMoveQueen(startRow, startCol, endRow, endCol)
        elif(piece == 6 or piece == -6):
            return checkMoveKing(startRow, startCol, endRow, endCol)
        else:
            return False
        
    
    def checkMoveBishop(startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        # if not moving diagonally
        if(Math.abs(rowDiff) != Math.abs(colDiff)):
            return False
        
        
        return isEmptyBetween(startRow, startCol, endRow, endCol)
    
    def checkMoveKing(startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        piece = board[startCol][endCol]
        
        if(Math.abs(rowDiff) <= 1 and Math.abs(colDiff) <= 1):
            if(piece > 0):
                canCastle[0] = False
                canCastle[1] = False
            else:
                canCastle[2] = False
                canCastle[3] = False
            
            return True
        
        
        # castling
        if(not kingInDanger(True) and startCol == 4 and rowDiff == 0):
            # castling kingside
            if(endCol == 6 and isEmptyBetween(startRow, startCol, endRow, 7) and isSafeBetween(startRow, startCol, endRow, 7)):
                if(piece > 0 and canCastle[0] and board[7][7] == 2):
                    canCastle[0] = False
                    canCastle[1] = False
                    return True
                elif(piece < 0 and canCastle[2] and board[0][7] == -2):
                    canCastle[0] = False
                    canCastle[1] = False
                    return True
                
            # castling queenSide
            elif(endCol == 2 and isEmptyBetween(startRow, startCol, endRow, 0) and isSafeBetween(startRow, startCol, endRow, 0)):
                if(piece > 0 and canCastle[1] and board[7][0] == 2):
                    canCastle[2] = False
                    canCastle[3] = False
                    return True
                elif(piece < 0 and canCastle[3] and board[0][0] == -2):
                    canCastle[2] = False
                    canCastle[3] = False
                    return True
                
            
        
        
        return False
    
    def checkMoveKnight(startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
    
        return Math.abs(rowDiff*colDiff) == 2
    
    def checkMovePawn(startRow, startCol, endRow, endCol):
        
        piece = board[startRow][startCol]
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        
        if(colDiff == 0 and isEmptySquare(endRow, endCol)):
            
            # if moving forward one square
            if(movingForwardOne(piece, rowDiff)):
                return True
            
            
            # moving forward two squares
            if(piece < 0 and startRow == 1 and endRow == 3 and isEmptySquare(2, startCol) and isEmptySquare(3, startCol)): # black piece
                setEnPassant(endRow, endCol, 0)
                return True
            elif(piece > 0 and startRow == 6 and endRow == 4 and isEmptySquare(5, endCol) and isEmptySquare(4, startCol)):
                setEnPassant(endRow, endCol, 0)
                return True
            
            
        elif(Math.abs(colDiff) == 1 and movingForwardOne(piece, rowDiff)): # moving diagonally
            
            # if capturing diagonally forward
            if(isEnemySquare(piece, endRow, endCol)):
                return True
            
            
            # enPassanting into an enemy square is not possible
            if(piece > 0 and isEnemySquare(piece, endRow + 1, endCol) and canEnPassant[0] == endRow + 1 and canEnPassant[1] == endCol):
                enPassant(endRow + 1, endCol)
                return True
            elif(piece < 0 and isEnemySquare(piece, endRow - 1, endCol) and canEnPassant[0] == endRow - 1 and canEnPassant[1] == endCol):
                enPassant(endRow - 1, endCol)
                return True
            
        
        return False
    
    def checkMoveQueen(startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        # if not moving diagonally or in a straight line 
        if(Math.abs(rowDiff) != Math.abs(colDiff) and rowDiff * colDiff != 0):
            return False
        
        
        return isEmptyBetween(startRow, startCol, endRow, endCol)
    
    def checkMoveRook(startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        # if not moving in a straight line
        if(rowDiff * colDiff != 0):
            return False
        
        
        if(isEmptyBetween(startRow, startCol, endRow, endCol)):
            if(startRow == 7):
                if(startCol == 0):
                    canCastle[1] = False
                elif(startCol == 7):
                    canCastle[0] = False
                
            elif(startRow == 0):
                if(startCol == 0):
                    canCastle[3] = False
                elif(startCol == 7):
                    canCastle[2] = False
                
            
            return True
        
        return False
        
    
    def getMovesBishop(row, col): # returns a list of possible moves. each move is a list [end_row, end_col]
        output = []
        for i in range(8):
            if(checkMove(row, col, row + i, col + i)):
                output.add(newMove(row + i, col + i))
            
            if(checkMove(row, col, row - i, col + i)):
                output.add(newMove(row - i, col + i))
            
            if(checkMove(row, col, row + i, col - i)):
                output.add(newMove(row + i, col - i))
            
            if(checkMove(row, col, row - i, col - i)):
                output.add(newMove(row - i, col - i))
        
        return output
    
    def getMovesKing(kingRow, kingCol):
        output = []
        
        for row in range(-1, 2):
            for col in range(-1, 2):
                if(not outOfBounds(kingRow + row, kingCol + col)):
                    if(checkMove(kingRow, kingCol, kingRow + row, kingCol + col)):
                        temp = []
                        temp.add(kingRow + row)
                        temp.add(kingCol + col)
                        output.add(temp)
                    
                
            
        
        
        return output
    
    def getMovesKnight(knightRow, knightCol):
        output = []
        
        for row in range(-2, 3):
            for col in range(-2, 3):
                if(not outOfBounds(knightRow + row, knightCol + col) and Math.abs(row*col) == 2):
                    if(checkMove(knightRow, knightCol, knightRow + row, knightCol + col)):
                        temp = []
                        temp.add(knightRow + row)
                        temp.add(knightCol + col)
                        output.add(temp)
                    
                
            
        
        
        return output
    
    def newMove(self, row, col):
        output = []
        output.add(row)
        output.add(col)
        return output
    
    def getMovesPawn(row, col):
        output = []
        
        # TODO make pawn moves more efficient
        if(not outOfBounds(row, col)):
            if(board[row][col] > 0):
                
                if(checkMove(row, col, row -1, col)):
                    output.add(newMove(row - 1, col))
                
                if(checkMove(row, col, row -1, col + 1)):
                    output.add(newMove(row - 1, col + 1))
                
                if(checkMove(row, col, row -1, col - 1)):
                    output.add(newMove(row - 1, col - 1))
                    
                if(checkMove(row, col, row -2, col)):
                    output.add(newMove(row - 2, col))
                
            else:
                
                if(checkMove(row, col, row + 1, col)):
                    output.add(newMove(row + 1, col))
                
                if(checkMove(row, col, row + 1, col + 1)):
                    output.add(newMove(row + 1, col + 1))
                
                if(checkMove(row, col, row + 1, col - 1)):
                    output.add(newMove(row + 1, col - 1))
                    
                if(checkMove(row, col, row + 2, col)):
                    output.add(newMove(row + 2, col))
                
            
        
        
        return output
    
    def getMovesQueen(queenRow, queenCol):
        output = []
        
        for i in range(8):
            
            # down right
            if(checkMove(queenRow, queenCol, queenRow + i, queenCol + i)):
                output.add(newMove(queenRow + i, queenCol + i))
        
            # up right
            if(checkMove(queenRow, queenCol, queenRow - i, queenCol + i)):
                output.add(newMove(queenRow - i, queenCol + i))
        
            # down left
            if(checkMove(queenRow, queenCol, queenRow + i, queenCol - i)):
                output.add(newMove(queenRow + i, queenCol - i))
        
            # up left
            if(checkMove(queenRow, queenCol, queenRow - i, queenCol - i)):
                output.add(newMove(queenRow - i, queenCol - i))
        
            # check current column
            if(checkMove(queenRow, queenCol, i, queenCol)):
                output.add(newMove(i, queenCol))
            
            # check current row
            if(checkMove(queenRow, queenCol, queenRow, i)):
                output.add(newMove(queenRow, i))
        
        
        return output
    
    def getMovesRook(rookRow, rookCol):
        output = []
        
        for i in range(8):
            if(checkMove(rookRow, rookCol, i, rookCol)):
                output.add(newMove(i, rookCol))
            
            if(checkMove(rookRow, rookCol,  rookRow, i)):
                output.add(newMove(rookRow, i))
            
        
        return output
    
    def isEmptySquare(self, row, col):
        return (self.board[row][col] == 0)
    
    def isEmptyBetween(startRow, startCol, endRow, endCol): # TODO check isEmptyBetween
        # checks if the squares STRICTLY BETWEEN the starting and ending squares are empty
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        # if not moving diagonally or vertically or horizontally
        if(Math.abs(rowDiff) != Math.abs(colDiff) and rowDiff * colDiff != 0):
            return False
        
        
        # ensure that startRow <= endRow (problem is symmetric, so self is valid)
        
        if(rowDiff < 0):
            return isEmptyBetween(endRow, endCol, startRow, startCol)
        
        
        # actually check if empty between
        if(rowDiff == colDiff):
            for i in range(1, rowDiff):
                if(not isEmptySquare(startRow + i, startCol + i)):
                    return False
                
            
        elif(rowDiff == -colDiff):
            for i in range(1, rowDiff):
                if(not isEmptySquare(startRow + i, startCol - i)):
                    return False
                
            
        elif(rowDiff ==0):
            for col in range(startCol+1, endCol):
                if(not isEmptySquare(startRow, col)):
                    return False
                
            
        elif(colDiff == 0):
            for row in range(startRow+1, endRow):
                if(not isEmptySquare(row, startCol)):
                    return False
                
            
        
        
        
        return True
    
    def isEnemySquare(self, piece, row, col):
        return (piece * self.board[row][col] < 0)
    
    def isSafeBetween(startRow, startCol, endRow, endCol): # TODO check isSafeBetween
        # checks if the squares STRICTLY BETWEEN the starting and ending squares are safe for king to cross
        
        rowDiff = endRow - startRow
        colDiff = endCol - startCol

        if(Math.abs(rowDiff) != Math.abs(colDiff) and rowDiff * colDiff != 0):
            return False
        
        
        # ensure that startCol <= endCol and startRow <= endRow (problem is symmetric, so self is valid)
        if(colDiff < 0):
            return isSafeBetween(startRow, endCol, endRow, startCol)
        
        if(rowDiff < 0):
            return isSafeBetween(endRow, startCol, startRow, endCol)
        
        
        copy = self.clone()

        # actually check if safe between
        tempTurn = False
        if(rowDiff == colDiff):
            for i in range(1, rowDiff):
                copy = copy.movePieceNoCheck(startRow + i - 1, startCol + i - 1, startRow + i, startCol + i)
                
                if(kingInDanger(copy, tempTurn)):
                    return False
                
                tempTurn = not tempTurn
            
        elif(rowDiff == 0):
            for col in range(startCol+1, endcol):
                copy = copy.movePieceNoCheck(startRow, col - 1, startRow, col)
                if(kingInDanger(copy, tempTurn)):
                    return False
                
                tempTurn = not tempTurn
            
        elif(colDiff == 0):
            for row in range(startRow+1, endRow):
                copy = copy.movePieceNoCheck(row - 1, startCol, row, startCol)
                if(kingInDanger(copy, tempTurn)):
                    return False
                
                tempTurn = not tempTurn
            
        
        
        return True
    
    def outOfBounds(row, col):
        # makes sure a is a valid row or column
        return (row < 0 or row > 7 or col < 0 or col > 7)
    
    def movingForwardOne(piece, rowDiff):
        return (rowDiff * piece < 0 and Math.abs(rowDiff) == 1)
    
    
    # copies the board from pychess object to current pychess object
    def copyBoard(board_to_copy):
        for row in range(8):
            for col in range(8):
                self.board[row][col] = board_to_copy.board[row][col]
            
    
    def setEnPassant(self, row, col, reset):
        self.canEnPassant[0] = row
        self.canEnPassant[1] = col
        self.canEnPassant[2] = reset
    
