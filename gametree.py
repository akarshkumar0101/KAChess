from gametree_node import gametree_node

class gametree:
    
    
    """ TODO:
        figure out right magnitudes for positional scores vs material scores
        maybe take into account how many open moves each piece has and how many pieces it is attacking
        use a game tree
        each node has chessboard, evaluation, and set of nodes corresponding to moves 
        
    """
    """ NOTES:
        self.chessboard      # a pychess_board of the current state of the game
        
        self.gametree        # a gametree that decides the moves
        
        self.sign            # sign of pieces controlled by engine
            
    """
    
    
    def __init__(self, chessboard):
        self.root = gametree_node(chessboard)
        
        """                           """
        """     engine parameters     """
        """                           """
        self.POSITION_SCALE = .1 # figure this one out
        
        self.PAWN_VALUE = 1
        self.KNIGHT_VALUE = 3
        self.BISHOP_VALUE = 3.5
        self.ROOK_VALUE = 5
        self.QUEEN_VALUE = 10
        self.KING_VALUE = 1000000
        
        """ all position tables from white perspective (top rows are farthest away). all scores positive """
        self.pawn_position =    [[10, 10, 10, 10, 10, 10, 10, 10],\
                                 [ 9,  9,  9,  9,  9,  9,  9,  9],\
                                 [ 7,  8,  8,  8,  8,  8,  8,  7],\
                                 [ 5,  5,  5,  5,  5,  5,  5,  5],\
                                 [ 2,  3,  3,  4,  4,  3,  3,  2],\
                                 [ 1,  1,  2,  2,  2,  2,  1,  1],\
                                 [ 1,  1,  1,  1,  1,  1,  1,  1],\
                                 [ 0,  0,  0,  0,  0,  0,  0,  0]]
        
        self.rook_position =    [[ 7,  8,  8,  8,  8,  8,  8,  7],\
                                 [10, 10, 10, 10, 10, 10, 10, 10],\
                                 [ 9,  9,  9,  9,  9,  9,  9,  9],\
                                 [ 3,  4,  5,  5,  5,  5,  4,  3],\
                                 [ 1,  1,  2,  2,  2,  2,  1,  1],\
                                 [ 1,  1,  1,  1,  1,  1,  1,  1],\
                                 [ 3,  4,  5,  5,  5,  5,  4,  3],\
                                 [ 3,  4,  5,  5,  5,  5,  4,  3]]
    
        self.knight_position=   [[ 0,  0,  0,  0,  0,  0,  0,  0],\
                                 [ 0,  2,  3,  4,  4,  3,  2,  0],\
                                 [ 0,  5,  8, 10, 10,  8,  5,  0],\
                                 [ 0,  0,  7,  9,  9,  7,  2,  0],\
                                 [ 0,  0,  5,  8,  8,  5,  2,  0],\
                                 [ 0,  1,  3,  4,  4,  3,  1,  0],\
                                 [ 0,  0,  0,  1,  1,  0,  0,  0],\
                                 [ 0,  0,  0,  0,  0,  0,  0,  0]]
        
        self.bishop_position=   [[ 0,  0,  0,  0,  0,  0,  0,  0],\
                                 [ 6,  7,  7,  7,  7,  7,  7,  6],\
                                 [ 6,  7,  8,  9,  9,  8,  7,  6],\
                                 [ 5,  7,  8, 10, 10,  8,  7,  5],\
                                 [ 5,  7,  8, 10, 10,  8,  7,  5],\
                                 [ 0,  1,  3,  4,  4,  3,  1,  0],\
                                 [ 0,  0,  0,  1,  1,  0,  0,  0],\
                                 [ 0,  0,  0,  0,  0,  0,  0,  0]]
        
        self.queen_position =   [[ 0,  0,  0,  0,  0,  0,  0,  0],\
                                 [ 6,  7,  7,  7,  7,  7,  7,  6],\
                                 [ 6,  7,  8,  9,  9,  8,  7,  6],\
                                 [ 5,  7,  8, 10, 10,  8,  7,  5],\
                                 [ 5,  7,  8, 10, 10,  8,  7,  5],\
                                 [ 0,  1,  3,  4,  4,  3,  1,  0],\
                                 [ 0,  0,  0,  1,  1,  0,  0,  0],\
                                 [ 0,  0,  0,  0,  0,  0,  0,  0]]
        
        self.king_position =    [[-2, -3, -4, -5, -6, -4, -3, -2],\
                                 [-2, -3, -4, -5, -6, -4, -3, -2],\
                                 [-2, -3, -4, -5, -6, -4, -3, -2],\
                                 [-2, -3, -4, -5, -6, -4, -3, -2],\
                                 [-2, -3, -4, -5, -6, -4, -3, -2],\
                                 [-2, -3, -4, -5, -6, -4, -3, -2],\
                                 [ 1,  1,  1,  1,  1,  1,  1,  1],\
                                 [10,  9,  8,  5,  5,  8,  9, 10]]
        
        
    def get_best_move(self, max_depth):
        chessboards, evaluations = self.__get_children(self.chessboard)
        self.gametree_root = chessboards
        
    
    def __get_children(self, chessboard):
        """ returns [children (in a tree) chessboards, evals of chessboards] """
        possible_moves = chessboard.get_possible_moves()
        chessboards = []
        evaluations = []
        
        for a_move in possible_moves:
            copy = chessboard.clone()
            copy.move(a_move)
            
            chessboards.extend(copy)
            evaluations.extend(self.eval_board(copy))
        
        return chessboards, evaluations
    
    
    def depth_first_search(self):
        chessboards, evaluations = self.__get_children(self.chessboard)
    
        
    def __eval_board(self, chessboard):
        """ returns a position score for chessboard board.
            positive for white, negative for black.
            chessboard is a pychess_board object. """
        
        board = chessboard.get_board()
        sum = 0
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                sum += self.__eval_material(board[row][col])
                sum += self.POSITION_SCALE * self.__eval_position(board[row][col], row, col)
                
        return sum 
    
    
    def __eval_position(self, piece, row, col):
        """ gets piece position value from lookup table """
        
        if(piece == 0):
            return 0
        elif(piece == 1):
            return self.pawn_position[row][col]
        elif(piece == 2):
            return self.rook_position[row][col]
        elif(piece == 3):
            return self.knight_position[row][col]
        elif(piece == 4):
            return self.bishop_position[row][col]
        elif(piece == 5):
            return self.queen_position[row][col]
        elif(piece == 6):
            return self.king_position[row][col]
        elif(piece == -1):
            return self.pawn_position[7-row][7-col] * -1
        elif(piece == -2):
            return self.rook_position[7-row][7-col] * -1
        elif(piece == -3):
            return self.knight_position[7-row][7-col] * -1
        elif(piece == -4):
            return self.bishop_position[7-row][7-col] * -1
        elif(piece == -5):
            return self.queen_position[7-row][7-col] * -1
        elif(piece == -6):
            return self.king_position[7-row][7-col] * -1
        else:
            raise ValueError(str(piece))


    def __eval_material(self, piece):
        
        if(piece == 0):
            return 0
        elif(piece == 1):
            return self.PAWN_VALUE
        elif(piece == 2):
            return self.ROOK_VALUE
        elif(piece == 3):
            return self.KNIGHT_VALUE
        elif(piece == 4):
            return self.BISHOP_VALUE
        elif(piece == 5):
            return self.QUEEN_VALUE
        elif(piece == 6):
            return self.KING_VALUE
        elif(piece == -1):
            return self.PAWN_VALUE * -1
        elif(piece == -2):
            return self.ROOK_VALUE * -1
        elif(piece == -3):
            return self.KNIGHT_VALUE * -1
        elif(piece == -4):
            return self.BISHOP_VALUE * -1
        elif(piece == -5):
            return self.QUEEN_VALUE * -1
        elif(piece == -6):
            return self.KING_VALUE * -1
        else:
            raise ValueError(str(piece))