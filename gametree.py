from gametree_node import gametree_node

class gametree:
    """ This class provides an interface to play, uses the gametree module to pick best move """
    
    
    """ TODO:
        figure out right magnitudes for positional scores vs material scores
        maybe take into account how many open moves each piece has and how many pieces it is attacking
        use a game tree
        each node has chessboard, evaluation, and set of nodes corresponding to moves 
        
    """
    
    
    """                                               """
    """                                               """
    """                  CONSTRUCTOR                  """
    """                                               """
    """                                               """
    
   
    def __init__(self, chessboard, plays_white):
        self.engine_plays_white = plays_white
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
        

    """                                               """
    """                                               """
    """                PUBLIC METHODS                 """
    """                                               """
    """                                               """
    
    def get_best_move(self, chessboard, max_depth):
        """ this method returns the best move for the current board position """
        for child in self.root.children:
            if(self.boards_are_equal(chessboard, child)):
                self.root = child
        
        best_node, best_move = self.root.get_best_move()
        
        self.root = best_node
        
        return best_move
    
    def get_evaluation(self):
        return self.root.get_evaluation()
    
    def boards_are_equal(self, b1, b2):
        board1 = b1.get_board()
        board2 = b2.get_board()
        
        for row in range(8):
            for col in range(8):
                if(board1[row][col] != board2[row][col]):
                    return False
                
        return True