import java.util.ArrayList

class Chessboard:
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
     *:{-2, -3, -4, -5, -6, -4, -3, -2
     *    :-1, -1, -1, -1, -1, -1, -1, -1
     *    : 0,  0,  0,  0,  0,  0,  0,  0
     *    : 0,  0,  0,  0,  0,  0,  0,  0
     *    : 0,  0,  0,  0,  0,  0,  0,  0
     *    : 0,  0,  0,  0,  0,  0,  0,  0
     *    : 1,  1,  1,  1,  1,  1,  1,  1
     * : 2,  3,  4,  5,  6,  4,  3,  2
     """
    
    board
    canEnPassant #:row, col, resetNextTurn if no row/col, set to -1. reset on 1, don't on 0
    whiteToMove
    boolean[] canCastle #:whiteKingside, whiteQueenside, blackKingside, blackQueenside
    
    # constructors # # # # # # # # # # # # # # # # # 
    
    Chessboard():
        setUpBoard()
    
    Chessboard(a):
        setUpBoard()
        whiteToMove = a
    
    Chessboard(b, a):
        setUpBoard()
        board = b
        whiteToMove = a
    
    
    # methods # # # # # # # # # # # # # # # # # 
    
    getBoard(){
        Chessboard output =  new Chessboard()
        output.copyBoard(this)
        return output.board
    
    kingInDanger(currentTurn):
        # if currentTurn is True, returns if the king is in danger for player whose turn it is
        # if currentTurn is False, returns if the king is in danger for player whose turn it is not
        int sign = 0
        int kingRow = -1
        int kingCol = -1
        
        if((currentTurn and whiteToMove) or (!currentTurn and !whiteToMove)):
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
            # this should be an exception?
            return False
        
        
        # check enemy knights
        for row in range(-2, 3, 1):
            for col in range(-2, 3, 1):
                if(!outOfBounds(kingRow + row, kingCol + col) and Math.abs(row*col) == 2):
                    if(board[kingRow + row][kingCol + col] == sign * -3):
                        return True
                    
                
            
        
        
        # check for danger by enemy king
        for row in range(-1, 2):
            for col in range(-1, 2):
                if(!outOfBounds(kingRow + row, kingCol + col)):
                    if(board[kingRow + row][kingCol + col] == sign * -6):
                        return True
                    
                
            
        
        
        # check up and down
        for row in range(1, 7):
            if(!outOfBounds(kingRow + row, kingCol)):
                int tempPiece =  board[kingRow + row][kingCol]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                else if(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        for row in range(1, 7):
            if(!outOfBounds(kingRow - row, kingCol)):
                int tempPiece =  board[kingRow - row][kingCol]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                else if(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        # check left and right
        for col in range(1, 7):
            if(!outOfBounds(kingRow, kingCol + col)):
                int tempPiece =  board[kingRow][kingCol + col]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                else if(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        for col in range(1, 7):
            if(!outOfBounds(kingRow, kingCol - col)):
                int tempPiece =  board[kingRow][kingCol - col]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                else if(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        # check down-right
        for i in range(1, 7):
            if(!outOfBounds(kingRow + i, kingCol + i)):
                int tempPiece =  board[kingRow + i][kingCol + i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                else if(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        # check up-left
        for i in range(1, 7):
            if(!outOfBounds(kingRow - i, kingCol - i)):
                int tempPiece =  board[kingRow - i][kingCol - i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                else if(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        # check down-left
        for i in range(1, 7):
            if(!outOfBounds(kingRow + i, kingCol - i)):
                int tempPiece =  board[kingRow + i][kingCol - i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                else if(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        # check up-right
        for i in range(1, 7):
            if(!outOfBounds(kingRow - i, kingCol + i)):
                int tempPiece =  board[kingRow - i][kingCol + i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                else if(tempPiece * sign > 0):
                    break
                
            else:
                break
            
        
        
        return False 
    
    kingInDanger(Chessboard b, currentTurn):
        return b.kingInDanger(currentTurn) # returns True if king is in danger on board b for specified turn
    
    move(int startRow, int startCol, int endRow, int endCol):
        
        # if valid move
        if(checkMove(startRow, startCol, endRow, endCol)):
            movePiece(startRow, startCol, endRow, endCol)
            return True
        
        
        return False
    
    String toString():
        String output = "________________________________________________\n"
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
    
    Chessboard clone():
        Chessboard output = new Chessboard()
        
        output.whiteToMove = this.whiteToMove
        
        for i in range(3):
            output.canEnPassant[i] = this.canEnPassant[i]
        
        
        output.copyBoard(this)
        
        return output
    
    """
     * This function returns a list of all possible moves for the piece at the given square.
     * Does take turn into account
     * 
     * @param row the current row of piece
     * @param col the current column of piece
     * @return List of containing the endRow and endCol of each possible move
     """
    ArrayList<int[]> getMoves(int row, int col){
        int piece = board[row][col]
        
        switch (piece):
            case 1:
            case -1:
                return getMovesPawn(row, col)
            case 2:
            case -2:
                return getMovesRook(row, col)
            case 3:
            case -3:
                return getMovesKnight(row, col)
            case 4:
            case -4:
                return getMovesBishop(row, col)
            case 5:
            case -5:
                return getMovesQueen(row, col)
            case 6:
            case -6:
                return getMovesKing(row, col)
            default:
                return new ArrayList<int[]>()
        
    
    
    ArrayList<int[]> getAllMoves(CurrentTurn){
        # TODO implement
        # TODO change get moves method to return array list of int arrays
        # of the form:startRow, startCol, endRow, endCol
        return new ArrayList<int[]>()
    
    # methods # # # # # # # # # # # # # # # # # 
    
    castle(String color, String dir):
        if(color.equals("white")):
            canCastle[0] = False
            canCastle[1] = False
            if(dir.equals("kingside")){
                board[7][7] = 0
                board[7][5] = 2
            else:
                board[7][0] = 0
                board[7][3] = 2
            
        else:
            canCastle[2] = False
            canCastle[3] = False
            if(dir.equals("kingside")){
                board[0][7] = 0
                board[0][5] = -2
            else:
                board[0][0] = 0
                board[0][3] = -2
            
        
    
    enPassant(int row, int col):
        board[row][col] = 0
    
    movePiece(int startRow, int startCol, int endRow, int endCol): # TODO check movePiece
        
        # reset enPassant if reset flag is set
        if(canEnPassant[2] != 0):
            canEnPassant = getNewEnPassant()
        
        
        canEnPassant[2] = 1 # reset next move
        
        int piece = board[startRow][startCol]
        
        if(piece == 6 and endRow == 7 and startRow == 7 and startCol == 4 and endCol == 7 and board[7][7] == 2):
            castle("white", "kingside")
        else if(piece == -6 and endRow == 0 and startRow == 0 and startCol == 4 and endCol == 7 and board[0][7] == -2):
            castle("black", "kingside")
        else if(piece == 6 and endRow == 7 and startRow == 7 and startCol == 4 and endCol == 2 and board[7][0] == 2):
            castle("white", "Queenside")
        else if(piece == -6 and endRow == 0 and startRow == 0 and startCol == 4 and endCol == 2 and board[0][0] == -2):
            castle("black", "Queenside")
        else if(piece > 0 and !outOfBounds(endRow + 1, endCol) and isEnemySquare(piece, endRow + 1, endCol) and canEnPassant[0] == endRow + 1 and canEnPassant[1] == endCol):
            enPassant(endRow + 1, endCol)
        else if(piece < 0 and !outOfBounds(endRow - 1, endCol) and isEnemySquare(piece, endRow - 1, endCol) and canEnPassant[0] == endRow - 1 and canEnPassant[1] == endCol):
            enPassant(endRow - 1, endCol)
        
        
        
        board[startRow][startCol] = 0 # move piece
        board[endRow][endCol] = piece
        whiteToMove = !whiteToMove
    
    Chessboard movePieceNoCheck(int startRow, int startCol, int endRow, int endCol):
        Chessboard output = this.clone() # clone is redundant but for safety
        output.movePiece(startRow, startCol, endRow, endCol)
        return output
    
    checkMove(int startRow, int startCol, int endRow, int endCol):
        
        int piece = board[startRow][startCol]
        
        # if incorrect turn
        if((piece < 0 and whiteToMove) or (piece > 0 and !whiteToMove)):
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
        Chessboard turnComplete = this.clone().movePieceNoCheck(startRow, startCol, endRow, endCol) 
        if(kingInDanger(turnComplete, False)):
            return False
        

        switch (piece):
            case 1:
            case -1:
                return checkMovePawn(startRow, startCol, endRow, endCol)
            case 2:
            case -2:
                return checkMoveRook(startRow, startCol, endRow, endCol)
            case 3:
            case -3:
                return checkMoveKnight(startRow, startCol, endRow, endCol)
            case 4:
            case -4:
                return checkMoveBishop(startRow, startCol, endRow, endCol)
            case 5:
            case -5:
                return checkMoveQueen(startRow, startCol, endRow, endCol)
            case 6:
            case -6:
                return checkMoveKing(startRow, startCol, endRow, endCol)
            default:
                return False
        
    
    checkMoveBishop(int startRow, int startCol, int endRow, int endCol):
        int rowDiff = endRow - startRow
        int colDiff = endCol - startCol
        
        # if not moving diagonally
        if(Math.abs(rowDiff) != Math.abs(colDiff)):
            return False
        
        
        return isEmptyBetween(startRow, startCol, endRow, endCol)
    
    checkMoveKing(int startRow, int startCol, int endRow, int endCol):
        int rowDiff = endRow - startRow
        int colDiff = endCol - startCol
        int piece = board[startCol][endCol]
        
        if(Math.abs(rowDiff) <= 1 and Math.abs(colDiff) <= 1):
            if(piece > 0):
                canCastle[0] = False
                canCastle[1] = False
            else:
                canCastle[2] = False
                canCastle[3] = False
            
            return True
        
        
        # castling
        if(!kingInDanger(True) and startCol == 4 and rowDiff == 0):
            # castling kingside
            if(endCol == 6 and isEmptyBetween(startRow, startCol, endRow, 7) and isSafeBetween(startRow, startCol, endRow, 7)):
                if(piece > 0 and canCastle[0] and board[7][7] == 2):
                    canCastle[0] = False
                    canCastle[1] = False
                    return True
                else if(piece < 0 and canCastle[2] and board[0][7] == -2):
                    canCastle[0] = False
                    canCastle[1] = False
                    return True
                
            # castling queenSide
            else if(endCol == 2 and isEmptyBetween(startRow, startCol, endRow, 0) and isSafeBetween(startRow, startCol, endRow, 0)):
                if(piece > 0 and canCastle[1] and board[7][0] == 2):
                    canCastle[2] = False
                    canCastle[3] = False
                    return True
                else if(piece < 0 and canCastle[3] and board[0][0] == -2):
                    canCastle[2] = False
                    canCastle[3] = False
                    return True
                
            
        
        
        return False
    
    checkMoveKnight(int startRow, int startCol, int endRow, int endCol):
        int rowDiff = endRow - startRow
        int colDiff = endCol - startCol
    
        return Math.abs(rowDiff*colDiff) == 2
    
    checkMovePawn(int startRow, int startCol, int endRow, int endCol):
        
        int piece = board[startRow][startCol]
        int rowDiff = endRow - startRow
        int colDiff = endCol - startCol
        
        
        if(colDiff == 0 and isEmptySquare(endRow, endCol)):
            
            # if moving forward one square
            if(movingForwardOne(piece, rowDiff)):
                return True
            
            
            # moving forward two squares
            if(piece < 0 and startRow == 1 and endRow == 3 and isEmptySquare(2, startCol) and isEmptySquare(3, startCol)): # black piece
                setEnPassant(endRow, endCol, 0)
                return True
            else if(piece > 0 and startRow == 6 and endRow == 4 and isEmptySquare(5, endCol) and isEmptySquare(4, startCol)):
                setEnPassant(endRow, endCol, 0)
                return True
            
            
        else if(Math.abs(colDiff) == 1 and movingForwardOne(piece, rowDiff)): # moving diagonally
            
            # if capturing diagonally forward
            if(isEnemySquare(piece, endRow, endCol)):
                return True
            
            
            # enPassanting into an enemy square is not possible
            if(piece > 0 and isEnemySquare(piece, endRow + 1, endCol) and canEnPassant[0] == endRow + 1 and canEnPassant[1] == endCol):
                enPassant(endRow + 1, endCol)
                return True
            else if(piece < 0 and isEnemySquare(piece, endRow - 1, endCol) and canEnPassant[0] == endRow - 1 and canEnPassant[1] == endCol):
                enPassant(endRow - 1, endCol)
                return True
            
        
        return False
    
    checkMoveQueen(int startRow, int startCol, int endRow, int endCol):
        int rowDiff = endRow - startRow
        int colDiff = endCol - startCol
        
        # if not moving diagonally or in a straight line 
        if(Math.abs(rowDiff) != Math.abs(colDiff) and rowDiff * colDiff != 0):
            return False
        
        
        return isEmptyBetween(startRow, startCol, endRow, endCol)
    
    checkMoveRook(int startRow, int startCol, int endRow, int endCol):
        int rowDiff = endRow - startRow
        int colDiff = endCol - startCol
        
        # if not moving in a straight line
        if(rowDiff * colDiff != 0):
            return False
        
        
        if(isEmptyBetween(startRow, startCol, endRow, endCol)):
            if(startRow == 7):
                if(startCol == 0):
                    canCastle[1] = False
                else if(startCol == 7):
                    canCastle[0] = False
                
            else if(startRow == 0):
                if(startCol == 0):
                    canCastle[3] = False
                else if(startCol == 7):
                    canCastle[2] = False
                
            
            return True
        
        return False
        
    
    ArrayList<int[]> getMovesBishop(int row, int col){
        ArrayList<int[]> output = new ArrayList<int[]>(14)
        for i in range(8):
            if(!outOfBounds(row + i, col + i)):
                if(checkMove(row, col, row + i, col + i)):
                    temp = new int[2]
                    temp[0] = row + i
                    temp[1] = col + i
                    output.add(temp)
                
            
        
        
        for i in range(8):
            if(!outOfBounds(row + i, col - i)):
                if(checkMove(row, col, row + i, col - i)):
                    temp = new int[2]
                    temp[0] = row + i
                    temp[1] = col - i
                    output.add(temp)
                
            
        
        
        for i in range(8):
            if(!outOfBounds(row - i, col + i)):
                if(checkMove(row, col, row - i, col + i)):
                    temp = new int[2]
                    temp[0] = row - i
                    temp[1] = col + i
                    output.add(temp)
                
            
        
        
        for i in range(8):
            if(!outOfBounds(row - i, col - i)):
                if(checkMove(row, col, row - i, col - i)):
                    temp = new int[2]
                    temp[0] = row - i
                    temp[1] = col - i
                    output.add(temp)
                
            
        
        # TODO make bishop get moves more efficient
        return output
    
    ArrayList<int[]> getMovesKing(int kingRow, int kingCol){
        ArrayList<int[]> output = new ArrayList<int[]>(10)
        
        for row in range(-1, 2):
            for col in range(-1, 2):
                if(!outOfBounds(kingRow + row, kingCol + col)):
                    if(checkMove(kingRow, kingCol, kingRow + row, kingCol + col)):
                        temp = new int[2]
                        temp[0] = kingRow + row
                        temp[1] = kingCol + col
                        output.add(temp)
                    
                
            
        
        
        return output
    
    ArrayList<int[]> getMovesKnight(int knightRow, int knightCol){
        ArrayList<int[]> output = new ArrayList<int[]>(8)
        
        for row in range(-2, 3):
            for col in range(-2, 3):
                if(!outOfBounds(knightRow + row, knightCol + col) and Math.abs(row*col) == 2):
                    if(checkMove(knightRow, knightCol, knightRow + row, knightCol + col)):
                        temp = new int[2]
                        temp[0] = knightRow + row
                        temp[1] = knightCol + col
                        output.add(temp)
                    
                
            
        
        
        return output
    
    ArrayList<int[]> getMovesPawn(int row, int col){
        ArrayList<int[]> output = new ArrayList<int[]>(4)
        
        if(!outOfBounds(row, col)):
            if(board[row][col] > 0):
                if(checkMove(row, col, row -1, col)):
                    temp = new int[2]
                    temp[0] = row - 1
                    temp[1] = col
                    output.add(temp)
                
                if(checkMove(row, col, row -1, col + 1)):
                    temp = new int[2]
                    temp[0] = row - 1
                    temp[1] = col + 1
                    output.add(temp)
                
                if(checkMove(row, col, row -1, col - 1)):
                    temp = new int[2]
                    temp[0] = row - 1
                    temp[1] = col - 1
                    output.add(temp)
                if(checkMove(row, col, row -2, col)):
                    temp = new int[2]
                    temp[0] = row - 2
                    temp[1] = col
                    output.add(temp)
                
            else:
                if(checkMove(row, col, row + 1, col)):
                    temp = new int[2]
                    temp[0] = row + 1
                    temp[1] = col
                    output.add(temp)
                
                if(checkMove(row, col, row + 1, col + 1)):
                    temp = new int[2]
                    temp[0] = row + 1
                    temp[1] = col + 1
                    output.add(temp)
                
                if(checkMove(row, col, row + 1, col - 1)):
                    temp = new int[2]
                    temp[0] = row + 1
                    temp[1] = col - 1
                    output.add(temp)
                if(checkMove(row, col, row + 2, col)):
                    temp = new int[2]
                    temp[0] = row + 2
                    temp[1] = col
                    output.add(temp)
                
            
        
        
        return output
    
    ArrayList<int[]> getMovesQueen(int queenRow, int queenCol){
        ArrayList<int[]> output = new ArrayList<int[]>(14)
        
        for row in range(8):
            if(checkMove(queenRow, queenCol, row, queenCol)):
                temp = new int[2]
                temp[0] = row
                temp[1] = queenCol
                output.add(temp)
            
        
        
        for col in range(8):
            if(checkMove(queenRow, queenCol, queenRow, col)):
                temp = new int[2]
                temp[0] = queenRow
                temp[1] = col
                output.add(temp)
            
        
        
        # TODO make queen moves more efficient
        for i in range(8):
            if(!outOfBounds(queenRow + i, queenCol + i)):
                if(checkMove(queenRow, queenCol, queenRow + i, queenCol + i)):
                    temp = new int[2]
                    temp[0] = queenRow + i
                    temp[1] = queenCol + i
                    output.add(temp)
                
            
        
        
        for i in range(8):
            if(!outOfBounds(queenRow + i, queenCol - i)):
                if(checkMove(queenRow, queenCol, queenRow + i, queenCol - i)):
                    temp = new int[2]
                    temp[0] = queenRow + i
                    temp[1] = queenCol - i
                    output.add(temp)
                
            
        
        
        for i in range(8):
            if(!outOfBounds(queenRow - i, queenCol + i)):
                if(checkMove(queenRow, queenCol, queenRow - i, queenCol + i)):
                    temp = new int[2]
                    temp[0] = queenRow - i
                    temp[1] = queenCol + i
                    output.add(temp)
                
            
        
        
        for i in range(8):
            if(!outOfBounds(queenRow - i, queenCol - i)):
                if(checkMove(queenRow, queenCol, queenRow - i, queenCol - i)):
                    temp = new int[2]
                    temp[0] = queenRow - i
                    temp[1] = queenCol - i
                    output.add(temp)
                
            
        
        
        return output
    
    ArrayList<int[]> getMovesRook(int rookRow, int rookCol){
        ArrayList<int[]> output = new ArrayList<int[]>(14)
        
        for row in range(8):
            if(checkMove(rookRow, rookCol, row, rookCol)):
                temp = new int[2]
                temp[0] = row
                temp[1] = rookCol
                output.add(temp)
            
        
        
        for col in range(8):
            if(checkMove(rookRow, rookCol, rookRow, col)):
                temp = new int[2]
                temp[0] = rookRow
                temp[1] = col
                output.add(temp)
            
        
        
        return output
    
    isEmptySquare(int row, int col):
        return (board[row][col] == 0)
    
    isEmptyBetween(int startRow, int startCol, int endRow, int endCol): # TODO check isEmptyBetween
        # checks if the squares STRICTLY BETWEEN the starting and ending squares are empty
        int rowDiff = endRow - startRow
        int colDiff = endCol - startCol
        
        # if not moving diagonally or vertically or horizontally
        if(Math.abs(rowDiff) != Math.abs(colDiff) and rowDiff * colDiff != 0):
            return False
        
        
        # ensure that startRow <= endRow (problem is symmetric, so this is valid)
        
        if(rowDiff < 0):
            return isEmptyBetween(endRow, endCol, startRow, startCol)
        
        
        # actually check if empty between
        if(rowDiff == colDiff):
            for i in range(1, rowDiff):
                if(!isEmptySquare(startRow + i, startCol + i)):
                    return False
                
            
        else if(rowDiff == -colDiff):
            for i in range(1, rowDiff):
                if(!isEmptySquare(startRow + i, startCol - i)):
                    return False
                
            
        else if(rowDiff ==0){
            for col in range(startCol+1, endCol):
                if(!isEmptySquare(startRow, col)):
                    return False
                
            
        else if(colDiff == 0):
            for row in range(startRow+1, endRow):
                if(!isEmptySquare(row, startCol)):
                    return False
                
            
        
        
        
        return True
    
    isEnemySquare(int piece, int row, int col):
        return (piece * board[row][col] < 0)
    
    isSafeBetween(int startRow, int startCol, int endRow, int endCol): # TODO check isSafeBetween
        # checks if the squares STRICTLY BETWEEN the starting and ending squares are safe for king to cross
        
        int rowDiff = endRow - startRow
        int colDiff = endCol - startCol

        if(Math.abs(rowDiff) != Math.abs(colDiff) and rowDiff * colDiff != 0):
            return False
        
        
        # ensure that startCol <= endCol and startRow <= endRow (problem is symmetric, so this is valid)
        if(colDiff < 0):
            return isSafeBetween(startRow, endCol, endRow, startCol)
        
        if(rowDiff < 0):
            return isSafeBetween(endRow, startCol, startRow, endCol)
        
        
        Chessboard copy = this.clone()

        # actually check if safe between
        tempTurn = False
        if(rowDiff == colDiff):
            for i in range(1, rowDiff):
                copy = copy.movePieceNoCheck(startRow + i - 1, startCol + i - 1, startRow + i, startCol + i)
                
                if(kingInDanger(copy, tempTurn)):
                    return False
                
                tempTurn = !tempTurn
            
        else if(rowDiff == 0){
            for col in range(startCol+1, endcol):
                copy = copy.movePieceNoCheck(startRow, col - 1, startRow, col)
                if(kingInDanger(copy, tempTurn)):
                    return False
                
                tempTurn = !tempTurn
            
        else if(colDiff == 0):
            for row in range(startRow+1, endRow):
                copy = copy.movePieceNoCheck(row - 1, startCol, row, startCol)
                if(kingInDanger(copy, tempTurn)):
                    return False
                
                tempTurn = !tempTurn
            
        
        
        return True
    
    outOfBounds(int row, int col):
        # makes sure a is a valid row or column
        return (row < 0 or row > 7 or col < 0 or col > 7)
    
    movingForwardOne(int piece, int rowDiff):
        return (rowDiff * piece < 0 and Math.abs(rowDiff) == 1)
    
    setUpBoard():
        board = getNewBoard()
        canEnPassant = getNewEnPassant()
        whiteToMove = True
        canCastle = new boolean[4]
        for i in range(4):
            canCastle[i] = True
        
    
    getNewBoard():
        output = 
           [[-2, -3, -4, -5, -6, -4, -3, -2],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [ 1,  1,  1,  1,  1,  1,  1,  1],
            [ 2,  3,  4,  5,  6,  4,  3,  2]]
        
        return output
    
    copyBoard(Chessboard from):
        for row in range(8):
            for col in range(8):
                this.board[row][col] = from.board[row][col]
            
        
    
    getNewEnPassant(){
        output = [-1, -1, 0]
        return output
    
    setEnPassant(int row, int col, int reset):
        canEnPassant[0] = row
        canEnPassant[1] = col
        canEnPassant[2] = reset
    
