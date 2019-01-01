from pychess_board import pychess_board

class pychess_board_engine:
    """ This class chooses the best move based on the position of a pychess_board """
    
    """
    int evaluation
    Chesspychess_board pychess_board
    boolean userPlaysWhite
    boolean engineToMove
    
     * white is positive
     * black is negative
     * 
     * pawns are 1 pt
     * knights are 3 pts
     * bishops are 3.5 pts
     * Rooks are 5 pts
     * Queens are 12 pts
     * King is infinity pts
     """
    """                                               """
    """                                               """
    """                  CONSTRUCTOR                  """
    """                                               """
    """                                               """
    
   
    def __init__(self, board_setup = None, white_to_move = True, user_plays_white = True):
        # TODO init position look up tables
        
        self.chessboard = pychess_board(board_setup, white_to_move)
        
        if(user_plays_white):
            self.sign = -1 # sign of pieces controlled by engine
        else:
            self.sign = 1
    
        
         
        
    """                                               """
    """                                               """
    """                PUBLIC METHODS                 """
    """                                               """
    """                                               """
    
    def get_best_move(self, milliseconds_to_think):
        """ returns move in form [startRow, startCol, endRow, endCol] """
        """ this is a simple engine. could do a lot better with a game tree """
        """ not using milliseconds to think, only searches moves one level deep """
        possible_moves = self.chessboard.get_possible_moves()
        chessboard_copy = self.chessboard.copy()
        best_move = None
        max_evaluation = 0
        
        for a_move in possible_moves:
            chessboard_copy = self.chessboard.copy()
            chessboard_copy.move(a_move)
            current_evaluation = self.__evaluate_board(chessboard_copy)
            if max_evaluation < current_evaluation:
                max_evaluation = current_evaluation
                best_move = a_move
            
        return best_move
       
       
    """                                               """
    """                                               """
    """                PRIVATE METHODS                """
    """                                               """
    """                                               """
        
    def __evaluate_board(self):
        """ returns a position score """
        # combination of material and position evaluation
        evaluation = self.__evaluate_material(self.chessboard) + self.__evaluate_position(self.chessboard)
        
        return evaluation 
    
    def __evaluate_position(self, chessboard):
        """ chessboard is a pychess_board object """
        board = chessboard.get_board()
        sum = 0
        
        for row in range(board):
            for col in range(board[0]):
                sum += self.__evaluate_piece_position(board[row][col], row, col)

        return sum * self.sign
    
    # returns a position score (double)

    def __evaluate_material(self, chessboard):
        """ chessboard is a pychess_board object. 
        returns positive rating if good for engine, negative if bad """
        
        board = chessboard.get_board()
        sum = 0
        
        for row in range(board):
            for col in range(board[0]):
                sum += board[row][col]
        
        return sum * self.sign
    
    def __evaluate_piece_position(self, piece, row, col):
        """ gets piece position value from lookup table """
        
        if(piece == 1):
            return self.white_pawn_position_table[row][col]
        elif(piece == 2):
            return self.white_rook_position_table[row][col]
        elif(piece == 3):
            return self.white_knight_position_table[row][col]
        elif(piece == 4):
            return self.white_bishop_position_table[row][col]
        elif(piece == 5):
            return self.white_queen_position_table[row][col]
        elif(piece == 6):
            return self.white_king_position_table[row][col]
        elif(piece == -1):
            return self.black_pawn_position_table[row][col]
        elif(piece == -2):
            return self.black_rook_position_table[row][col]
        elif(piece == -3):
            return self.black_knight_position_table[row][col]
        elif(piece == -4):
            return self.black_bishop_position_table[row][col]
        elif(piece == -5):
            return self.black_queen_position_table[row][col]
        elif(piece == -6):
            return self.black_king_position_table[row][col]
        else:
            raise ValueError
