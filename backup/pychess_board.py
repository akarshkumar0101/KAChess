import numpy as np
import copy

class pychess_board():
    """ This class provides chessboard logic """
    
    # FIXME promotion to piece other than queen in move_piece method
    """                                               """
    """                     NOTES                     """
    """                      """                      """
        positive is white
        negative is black
        
        1 -- pawn
        2 -- rook
        3 -- knight
        4 -- bishop
        5 -- queen
        6 -- king
        0 -- empty square
        
        [[-2, -3, -4, -5, -6, -4, -3, -2],
         [-1, -1, -1, -1, -1, -1, -1, -1],
         [ 0,  0,  0,  0,  0,  0,  0,  0],
         [ 0,  0,  0,  0,  0,  0,  0,  0],
         [ 0,  0,  0,  0,  0,  0,  0,  0],
         [ 0,  0,  0,  0,  0,  0,  0,  0],
         [ 1,  1,  1,  1,  1,  1,  1,  1],
         [ 2,  3,  4,  5,  6,  4,  3,  2]]
         
        
        self.board
        self.enPassantable #:row, col -- if no row/col, set to -1. reset on 1, don't on 0
        self.resetEnPassant -- enPassantable register to be reset next turn
        self.whiteToMove
        self.canCastle #: [whiteKingside, whiteQueenside, blackKingside, blackQueenside] boolean array
        self.game_has_ended --> true only if the current game has ended
        self.game_ending_message --> describes game ending
        self.draw_is_offered # draw offered by [white, black]
    """
    
    
    
    
    """                                               """
    """                                               """
    """                  CONSTRUCTOR                  """
    """                                               """
    """                                               """
    
    def __init__(self, board_setup = None, white_to_move = True):
        
        if(board_setup == None):
            self.board = [[-2, -3, -4, -5, -6, -4, -3, -2],\
                          [-1, -1, -1, -1, -1, -1, -1, -1],\
                          [ 0,  0,  0,  0,  0,  0,  0,  0],\
                          [ 0,  0,  0,  0,  0,  0,  0,  0],\
                          [ 0,  0,  0,  0,  0,  0,  0,  0],\
                          [ 0,  0,  0,  0,  0,  0,  0,  0],\
                          [ 1,  1,  1,  1,  1,  1,  1,  1],\
                          [ 2,  3,  4,  5,  6,  4,  3,  2]]
        else:
            temp_board = []
            for i in range(8):
                temp_board.append(board_setup[i][:])

            self.board = temp_board
            
        self.whiteToMove = white_to_move
        
        self.enPassantable = [-1, -1]
        self.resetEnPassant = False
        
        # can castle [white_kingside, white_queenside, black_kingside, black_queenside]
        self.canCastle = [True, True, True, True]
        self.game_complete = False
        self.game_complete_message = ""
        self.draw_is_offered = [False, False] # draw offered by [white, black]
        
        
        
        
    """                                               """
    """                                               """
    """                PUBLIC METHODS                 """
    """                                               """
    """                                               """
        
    def get_possible_moves(self): # returns a list of all possible moves. each move is a list [current_row, current_col, end_row, end_col]
        output = []
        for row in range(8):
            for col in range(8):
                if((self.board[row][col] > 0) == self.whiteToMove):
                    output.extend(self.__get_moves(row, col))
        
        assert(len(output) > 0)
        return output
     
     
    def move(self, move): # move is list of form [startRow, startCol, endRow, endCol]
        # returns true if move is completed
        startRow = move[0]
        startCol = move[1]
        endRow   = move[2]
        endCol   = move[3]
        
        # if valid move
        if((not self.game_complete) and self.__check_move(startRow, startCol, endRow, endCol)):
            self.__move_piece(startRow, startCol, endRow, endCol)
            self.__check_game_complete() # TODO debug
            return True
        
        return False
    
    
    def get_board(self):
        output = []
        for i in range(8):
            output.append(self.board[i][:])
            
        return output
    
    
    def white_to_move(self):
        return self.whiteToMove
    
    
    def clone(self):
        return copy.deepcopy(self)
    
    
    def to_string(self):
        output = "________________________________________________\n"
        for row in range(8):
            output += "|     |     |     |     |     |     |     |     |\n"
            for col in range(8):
                if(self.board[row][col] == 0):
                    output+="|     "
                else:
                    if(self.board[row][col] < 0):
                        output += "| "
                    else:
                        output += "|  "
                    
                    output+= str(self.board[row][col]) + "  "
                
            
            output +="|\n"
            output += "|_____|_____|_____|_____|_____|_____|_____|_____|\n"
        
        return output
    
    
    def resign(self, current_turn=True): #bool current turn
        if(current_turn):
            if(self.white_to_move()):
                self.__end_game("White resigns. Black wins!")
            else:
                self.__end_game("Black resigns. White wins!")
        else:
            if(not self.white_to_move()):
                self.__end_game("White resigns. Black wins!")
            else:
                self.__end_game("Black resigns. White wins!")

    
    def offer_draw(self, current_turn=True):
        
        if(current_turn):
            
            if(self.white_to_move()):
                self.draw_is_offered[0] = True
            else:
                self.draw_is_offered[1] = True
        else:
            
            if(self.white_to_move()):
                self.draw_is_offered[1] = True
            else:
                self.draw_is_offered[0] = True
        
        
    def accept_draw(self, current_turn=True):
        
        if(current_turn):
            
            if(self.white_to_move() and draw_is_offered[1]):
                self.__end_game("It's a draw.")
            elif(not self.white_to_move() and draw_is_offered[0]):
                self.__end_game("It's a draw.")
                
        else:
            
            if(not self.white_to_move() and draw_is_offered[1]):
                self.__end_game("It's a draw.")
            elif(self.white_to_move() and draw_is_offered[0]):
                self.__end_game("It's a draw.")
        
        
        
    """                                               """
    """                                               """
    """                PRIVATE METHODS                """
    """                                               """
    """                                               """
    
    
    
    """            methods to move pieces             """
    def __move_piece(self, startRow, startCol, endRow, endCol): # TODO check the logic 
        
        # reset enPassantable if reset flag is set (this should always be first)
        if(self.resetEnPassant):
            self.enPassantable = [-1, -1]
        
        self.resetEnPassant = True # reset next move
        
        piece = self.board[startRow][startCol]
        
        if(piece == 6):
            
            if(startCol == 4):
                if(endCol == 7):
                    self.__castle("white", "kingside")
                elif(endCol == 2):
                    self.__castle("white", "Queenside")
            else:
                self.canCastle[0] = False
                self.canCastle[1] = False
                
        elif(piece == -6):
            
            if(startCol == 4):
                if(endCol == 7):
                    self.__castle("black", "kingside")
                elif(endCol == 2):
                    self.__castle("black", "Queenside")
            else:
                self.canCastle[2] = False
                self.canCastle[3] = False
                
        elif(piece == 1):
            
            if(endRow == 0):
                self.__promote(endRow, endCol, 5)
            elif(not self.__out_of_bounds(endRow + 1, endCol) and self.__is_enemy_square(piece, endRow + 1, endCol)):
                self.__en_passant(endRow + 1, endCol)
                
            elif(startRow == 6 and endRow == 4):
                self.__set_en_passant(endRow, endCol)
            
        elif(piece == -1):
            
            if(endRow == 8):
                self.__promote(endRow, endCol, -5)
            elif(not self.__out_of_bounds(endRow - 1, endCol) and self.__is_enemy_square(piece, endRow - 1, endCol)):
                self.__en_passant(endRow - 1, endCol)
                
            elif(startRow == 1 and endRow == 3):
                self.__set_en_passant(endRow, endCol)
                
        elif(piece == -2):
            
            if(startRow == 7):
                if(startCol == 0):
                    self.canCastle[1] = False
                elif(startCol == 7):
                    self.canCastle[0] = False
                    
        elif(piece == 2):
                   
            if(startRow == 0):
                if(startCol == 0):
                    self.canCastle[3] = False
                elif(startCol == 7):
                    self.canCastle[2] = False
        
        
        self.board[startRow][startCol] = 0 # move piece
        self.board[endRow][endCol] = piece
        self.whiteToMove = not self.whiteToMove

    def __move_piece_no_check(self, startRow, startCol, endRow, endCol): # returns a new pychess_board object with the piece moved regardless if it is a legal move
        output = self.clone() # clone is redundant but for safety
        output.__move_piece(startRow, startCol, endRow, endCol)
        return output
    
                    
    
    
    """    methods to get all possible moves in the current position from the specified square    """
    def __get_moves(self, row, col):
        piece = self.board[row][col]
        
        if(piece == 1 or piece == -1):
            return self.__get_moves_pawn(row, col)
        elif(piece == 2 or piece == -2):
            return self.__get_moves_rook(row, col)
        elif(piece == 3 or piece == -3):
            return self.__get_moves_knight(row, col)
        elif(piece == 4 or piece == -4):
            return self.__get_moves_bishop(row, col)
        elif(piece == 5 or piece == -5):
            return self.__get_moves_queen(row, col)
        elif(piece == 6 or piece == -6):
            return self.__get_moves_king(row, col)
        else:
            return []
    
    def __get_moves_bishop(self, row, col): # returns a list of possible moves. each move is a list [end_row, end_col]
        output = []
        for i in range(8):
            if(self.__check_move(row, col, row + i, col + i)):
                output.append(self.__new_move(row, col, row + i, col + i))
            
            if(self.__check_move(row, col, row - i, col + i)):
                output.append(self.__new_move(row, col, row - i, col + i))
            
            if(self.__check_move(row, col, row + i, col - i)):
                output.append(self.__new_move(row, col, row + i, col - i))
            
            if(self.__check_move(row, col, row - i, col - i)):
                output.append(self.__new_move(row, col, row - i, col - i))
        
        return output
    
    def __get_moves_king(self, kingRow, kingCol):
        output = []
        
        for row in range(-1, 2):
            for col in range(-1, 2):
                if(self.__check_move(kingRow, kingCol, kingRow + row, kingCol + col)):
                    output.append(self.__new_move(kingRow, kingCol, kingRow + row,kingCol + col))
        
        return output
    
    def __get_moves_knight(self, knightRow, knightCol):
        output = []
        
        for row in range(-2, 3):
            for col in range(-2, 3):
                if(self.__check_move(knightRow, knightCol, knightRow + row, knightCol + col)):
                    output.append(self.__new_move(knightRow, knightCol, knightRow + row, knightCol + col))
        
        return output
    
    def __get_moves_pawn(self, row, col):
        output = []
        
        # TODO make pawn moves more efficient
        if(not self.__out_of_bounds(row, col)):
            if(self.board[row][col] > 0):
                
                if(self.__check_move(row, col, row -1, col)):
                    output.append(self.__new_move(row, col, row - 1, col))
                
                if(self.__check_move(row, col, row -1, col + 1)):
                    output.append(self.__new_move(row, col, row - 1, col + 1))
                
                if(self.__check_move(row, col, row -1, col - 1)):
                    output.append(self.__new_move(row, col, row - 1, col - 1))
                    
                if(self.__check_move(row, col, row -2, col)):
                    output.append(self.__new_move(row, col, row - 2, col))
                
            else:
                
                if(self.__check_move(row, col, row + 1, col)):
                    output.append(self.__new_move(row, col, row + 1, col))
                
                if(self.__check_move(row, col, row + 1, col + 1)):
                    output.append(self.__new_move(row, col, row + 1, col + 1))
                
                if(self.__check_move(row, col, row + 1, col - 1)):
                    output.append(self.__new_move(row, col, row + 1, col - 1))
                    
                if(self.__check_move(row, col, row + 2, col)):
                    output.append(self.__new_move(row, col, row + 2, col))

        
        return output
    
    def __get_moves_queen(self, queenRow, queenCol):
        output = []
        
        for i in range(8):
            
            # down right
            if(self.__check_move(queenRow, queenCol, queenRow + i, queenCol + i)):
                output.append(self.__new_move(queenRow, queenCol, queenRow + i, queenCol + i))
        
            # up right
            if(self.__check_move(queenRow, queenCol, queenRow - i, queenCol + i)):
                output.append(self.__new_move(queenRow, queenCol, queenRow - i, queenCol + i))
        
            # down left
            if(self.__check_move(queenRow, queenCol, queenRow + i, queenCol - i)):
                output.append(self.__new_move(queenRow, queenCol, queenRow + i, queenCol - i))
        
            # up left
            if(self.__check_move(queenRow, queenCol, queenRow - i, queenCol - i)):
                output.append(self.__new_move(queenRow, queenCol, queenRow - i, queenCol - i))
        
            # check current column
            if(self.__check_move(queenRow, queenCol, i, queenCol)):
                output.append(self.__new_move(queenRow, queenCol, i, queenCol))
            
            # check current row
            if(self.__check_move(queenRow, queenCol, queenRow, i)):
                output.append(self.__new_move(queenRow, queenCol, queenRow, i))
        
        
        return output
    
    def __get_moves_rook(self, rookRow, rookCol):
        output = []
        
        for i in range(8):
            if(self.__check_move(rookRow, rookCol, i, rookCol)):
                output.append(self.__new_move(rookRow, rookCol, i, rookCol))
            
            if(self.__check_move(rookRow, rookCol,  rookRow, i)):
                output.append(self.__new_move(rookRow, rookCol, rookRow, i))
            
        
        return output
    
    
    
    
    """    methods to check if moves are legal. All methods return a boolean    """
    def __check_move(self, startRow, startCol, endRow, endCol):

        piece = self.board[startRow][startCol]
        
        # if incorrect turn
        if((piece < 0) == self.whiteToMove):
            return False
        
        # if starting or ending squares are out of bounds
        if(self.__out_of_bounds(startRow, startCol) or self.__out_of_bounds(endRow, endCol)):
            return False
        

        # if starting and ending squares are the same
        if(startRow == endRow and startCol == endCol):
            return False
        
        
        # if ending square is occupied by friendly piece
        if(piece*self.board[endRow][endCol] > 0):
            return False
        
        
        # if king is in danger after move is completed
        turnComplete = self.clone().__move_piece_no_check(startRow, startCol, endRow, endCol)
        if(turnComplete.__king_in_danger(False)):
            return False
        
        if(piece == 1 or piece == -1):
            return self.__check_move_pawn(startRow, startCol, endRow, endCol)
        elif(piece == 2 or piece == -2):
            return self.__check_move_rook(startRow, startCol, endRow, endCol)
        elif(piece == 3 or piece == -3):
            return self.__check_move_knight(startRow, startCol, endRow, endCol)
        elif(piece == 4 or piece == -4):
            return self.__check_move_bishop(startRow, startCol, endRow, endCol)
        elif(piece == 5 or piece == -5):
            return self.__check_move_queen(startRow, startCol, endRow, endCol)
        elif(piece == 6 or piece == -6):
            return self.__check_move_king(startRow, startCol, endRow, endCol)
        else:
            return False
    
    def __check_move_bishop(self, startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        # if not moving diagonally
        if(np.abs(rowDiff) != np.abs(colDiff)):
            return False
        
        
        return self.__is_empty_between(startRow, startCol, endRow, endCol)
    
    def __check_move_king(self, startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        piece = self.board[startRow][startCol]
        
        if(np.abs(rowDiff) <= 1 and np.abs(colDiff) <= 1):
            return True
        
        # castling
        if(not self.__king_in_danger(True) and startCol == 4 and rowDiff == 0):
            
            # castling kingside
            if(endCol == 6 and self.__is_empty_between(startRow, startCol, endRow, 7) and self.__is_safe_between(startRow, startCol, endRow, 7)):
                
                if(piece > 0 and canCastle[0] and self.board[7][7] == 2):
                    return True
                elif(piece < 0 and canCastle[2] and self.board[0][7] == -2):
                    return True
                
            # castling queenSide
            elif(endCol == 2 and self.__is_empty_between(startRow, startCol, endRow, 0) and self.__is_safe_between(startRow, startCol, endRow, 0)):
                
                if(piece > 0 and self.canCastle[1] and self.board[7][0] == 2):
                    return True
                elif(piece < 0 and self.canCastle[3] and self.board[0][0] == -2):
                    return True

        
        return False
    
    def __check_move_knight(self, startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
    
        return np.abs(rowDiff*colDiff) == 2
    
    def __check_move_pawn(self, startRow, startCol, endRow, endCol):
        
        piece = self.board[startRow][startCol]
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        
        if(colDiff == 0 and self.__is_empty_square(endRow, endCol)):
            
            # if moving forward one square
            if(self.__moving_forward_one(piece, rowDiff)):
                return True
            
            # moving forward two squares
            if(piece < 0 and startRow == 1 and endRow == 3 and self.__is_empty_square(2, startCol) and self.__is_empty_square(3, startCol)): # black piece
                return True
            elif(piece > 0 and startRow == 6 and endRow == 4 and self.__is_empty_square(5, endCol) and self.__is_empty_square(4, startCol)):
                return True
            
        elif(np.abs(colDiff) == 1 and self.__moving_forward_one(piece, rowDiff)): # moving diagonally
            # if capturing diagonally forward
            if(self.__is_enemy_square(piece, endRow, endCol)):
                return True
            # enPassanting into an enemy square is not possible
            elif(piece > 0 and self.__is_enemy_square(piece, endRow + 1, endCol) and self.enPassantable[0] == endRow + 1 and self.enPassantable[1] == endCol):
                return True
            elif(piece < 0 and self.__is_enemy_square(piece, endRow - 1, endCol) and self.enPassantable[0] == endRow - 1 and self.enPassantable[1] == endCol):
                return True
            
        
        return False
    
    def __check_move_queen(self, startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        # if not moving diagonally or in a straight line 
        if(np.abs(rowDiff) != np.abs(colDiff) and rowDiff * colDiff != 0):
            return False
        
        
        return self.__is_empty_between(startRow, startCol, endRow, endCol)
    
    def __check_move_rook(self, startRow, startCol, endRow, endCol):
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        # if not moving in a straight line
        if(rowDiff * colDiff != 0):
            return False
        
        
        if(self.__is_empty_between(startRow, startCol, endRow, endCol)):
            return True
        
        return False
    
    
    
    
    """        methods to help with board logic        """
    def __is_empty_square(self, row, col):
        return (self.board[row][col] == 0)
    
    def __is_empty_between(self, startRow, startCol, endRow, endCol): # TODO check __is_empty_between
        # checks if the squares STRICTLY BETWEEN the starting and ending squares are empty
        rowDiff = endRow - startRow
        colDiff = endCol - startCol
        
        # if not moving diagonally or vertically or horizontally
        if(np.abs(rowDiff) != np.abs(colDiff) and rowDiff * colDiff != 0):
            return False
        
        
        # ensure that startRow <= endRow (problem is symmetric, so self is valid)
        
        if(rowDiff < 0):
            return self.__is_empty_between(endRow, endCol, startRow, startCol)
        
        
        # actually check if empty between
        if(rowDiff == colDiff):
            for i in range(1, rowDiff):
                if(not self.__is_empty_square(startRow + i, startCol + i)):
                    return False
                
            
        elif(rowDiff == -colDiff):
            for i in range(1, rowDiff):
                if(not self.__is_empty_square(startRow + i, startCol - i)):
                    return False
                
            
        elif(rowDiff ==0):
            for col in range(startCol+1, endCol):
                if(not self.__is_empty_square(startRow, col)):
                    return False
                
            
        elif(colDiff == 0):
            for row in range(startRow+1, endRow):
                if(not self.__is_empty_square(row, startCol)):
                    return False
                
        return True
    
    def __is_enemy_square(self, piece, row, col):
        return (piece * self.board[row][col] < 0)
    
    def __is_safe_between(self, startRow, startCol, endRow, endCol): # TODO check __is_safe_between
        # checks if the squares STRICTLY BETWEEN the starting and ending squares are safe for king to cross
        
        rowDiff = endRow - startRow
        colDiff = endCol - startCol

        if(np.abs(rowDiff) != np.abs(colDiff) and rowDiff * colDiff != 0):
            return False
        
        
        # ensure that startCol <= endCol and startRow <= endRow (problem is symmetric, so self is valid)
        if(colDiff < 0):
            return self.__is_safe_between(startRow, endCol, endRow, startCol)
        
        if(rowDiff < 0):
            return self.__is_safe_between(endRow, startCol, startRow, endCol)
        
        
        a_copy = self.clone()

        # actually check if safe between
        tempTurn = False
        if(rowDiff == colDiff):
            for i in range(1, rowDiff):
                a_copy = a_copy.__move_piece_no_check(startRow + i - 1, startCol + i - 1, startRow + i, startCol + i)
                
                if(kingInDanger(a_copy, tempTurn)):
                    return False
                
                tempTurn = not tempTurn
            
        elif(rowDiff == 0):
            for col in range(startCol+1, endCol):
                a_copy = a_copy.__move_piece_no_check(startRow, col - 1, startRow, col)
                if(a_copy.__king_in_danger(tempTurn)):
                    return False
                
                tempTurn = not tempTurn
            
        elif(colDiff == 0):
            for row in range(startRow+1, endRow):
                a_copy = a_copy.__move_piece_no_check(row - 1, startCol, row, startCol)
                if(a_copy.__king_in_danger(tempTurn)):
                    return False
                
                tempTurn = not tempTurn
            
        
        
        return True
    
    def __king_in_danger(self, currentTurn = True):
        # if currentTurn is True, returns if the king is in danger for player whose turn it is
        # if currentTurn is False, returns if the king is in danger for player whose turn it is not
        sign = 0
        kingRow = -1
        kingCol = -1
        
        if(currentTurn == self.whiteToMove):
            sign = 1
        else:
            sign = -1
        
        
        # find king
        for row in range(8):
            for col in range(8):
                if(self.board[row][col] == sign * 6):
                    kingRow = row
                    kingCol = col
                
            
        
        
        if(kingRow == -1 or kingCol == -1):
            # self should be an exception?
            return False
        
        
        
        
        # check enemy knights
        for row in range(-2, 3):
            for col in range(-2, 3):
                if(not self.__out_of_bounds(kingRow + row, kingCol + col) and np.abs(row*col) == 2):
                    if(self.board[kingRow + row][kingCol + col] == sign * -3):
                        return True
                    
        
        # check for danger by enemy king
        for row in range(-1, 2):
            for col in range(-1, 2):
                if(not self.__out_of_bounds(kingRow + row, kingCol + col)):
                    if(self.board[kingRow + row][kingCol + col] == sign * -6):
                        return True
        
        
        # check up and down
        for row in range(1, 8):
            if(not self.__out_of_bounds(kingRow + row, kingCol)):
                tempPiece =  self.board[kingRow + row][kingCol]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign != 0): # piece blocking
                    break
                
            else:
                break
            
        
        for row in range(1, 8):
            if(not self.__out_of_bounds(kingRow - row, kingCol)):
                tempPiece =  self.board[kingRow - row][kingCol]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign != 0):
                    break
                
            else:
                break
            
        
        
        # check left and right
        for col in range(1, 8):
            if(not self.__out_of_bounds(kingRow, kingCol + col)):
                tempPiece =  self.board[kingRow][kingCol + col]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign != 0):
                    break
                
            else:
                break
            
        
        
        for col in range(1, 8):
            if(not self.__out_of_bounds(kingRow, kingCol - col)):
                tempPiece =  self.board[kingRow][kingCol - col]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign != 0):
                    break
                
            else:
                break
            
        
        
        # check down-right
        for i in range(1, 8):
            if(not self.__out_of_bounds(kingRow + i, kingCol + i)):
                tempPiece =  self.board[kingRow + i][kingCol + i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign != 0):
                    break
                
            else:
                break
            
        
        # check up-left
        for i in range(1, 8):
            if(not self.__out_of_bounds(kingRow - i, kingCol - i)):
                tempPiece =  self.board[kingRow - i][kingCol - i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign != 0):
                    break
                
            else:
                break
            
        
        # check down-left
        for i in range(1, 8):
            if(not self.__out_of_bounds(kingRow + i, kingCol - i)):
                tempPiece =  self.board[kingRow + i][kingCol - i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign != 0):
                    break
                
            else:
                break
            
        
        # check up-right
        for i in range(1, 8):
            if(not self.__out_of_bounds(kingRow - i, kingCol + i)):
                tempPiece =  self.board[kingRow - i][kingCol + i]
                if(tempPiece == sign * -5 or tempPiece == sign * -2):
                    return True
                elif(tempPiece * sign != 0):
                    break
                
            else:
                break
            
        
        
        return False 
    
    
    
    
    """        methods to end the game        """
    def __end_game(self, message=""):
        self.game_complete = True
        
        if(len(self.get_possible_moves()) == 0):
            if(self.__king_in_danger()):
                self.game_ending_message = "Checkmate. "
                if(self.whiteToMove):
                    self.game_ending_message += "Black has won!"
                else:
                    self.game_ending_message += "White has won!"
            else:
                self.game_ending_message = "Stalemate!"
                
        self.game_ending_message = message

    def __check_game_complete(self):
        if(len(self.get_possible_moves()) == 0):
            self.__end_game()
   
       
    
    
    
    """        misc. methods to help with tasks        """
    def __moving_forward_one(self, piece, rowDiff):
        return (rowDiff * piece < 0 and np.abs(rowDiff) == 1)
    
    def __out_of_bounds(self, row, col):
        # makes sure a is a valid row or column
        return (row < 0 or row > 7 or col < 0 or col > 7)
    
    
    # copies the board from pychess_board object to current pychess_board object

    def __castle(self, color, dir):
        if(color == "white"):
            self.canCastle[0] = False
            self.canCastle[1] = False
            if(dir == "kingside"):
                self.board[7][7] = 0
                self.board[7][5] = 2
            else:
                self.board[7][0] = 0
                self.board[7][3] = 2
            
        else:
            self.canCastle[2] = False
            self.canCastle[3] = False
            if(dir == "kingside"):
                self.board[0][7] = 0
                self.board[0][5] = -2
            else:
                self.board[0][0] = 0
                self.board[0][3] = -2
    
    def __en_passant(self, row, col):
        self.board[row][col] = 0
    
    def __set_en_passant(self, row, col):
        temp = []
        temp.append(row)
        temp.append(col)
        self.enPassantable = temp
        self.resetEnPassant = False
    
    def __new_move(self, start_row, start_col, row, col):
        output = []
        output.append(start_row)
        output.append(start_col)
        output.append(row)
        output.append(col)
        return output
   
    def __promote(self, row, col, piece):
        self.board[row][col] = piece
