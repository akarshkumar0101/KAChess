<<<<<<< HEAD
import numpy
import datetime
        
"""                           """
"""     engine parameters     """
"""                           """

MIN_EVAL_POSSIBLE = -10000
MAX_EVAL_POSSIBLE = 10000

POSITION_SCALE = .1 # figure this one out
        
PAWN_VALUE = 1
KNIGHT_VALUE = 3
BISHOP_VALUE = 3.5
ROOK_VALUE = 5
QUEEN_VALUE = 10
KING_VALUE = 100000
        
""" all position tables from white perspective (top rows are farthest away). all scores positive """
pawn_position =     [[10, 10, 10, 10, 10, 10, 10, 10],\
                     [ 9,  9,  9,  9,  9,  9,  9,  9],\
                     [ 7,  8,  8,  8,  8,  8,  8,  7],\
                     [ 5,  5,  5,  5,  5,  5,  5,  5],\
                     [ 2,  3,  3,  4,  4,  3,  3,  2],\
                     [ 1,  1,  2,  2,  2,  2,  1,  1],\
                     [ 1,  1,  1,  1,  1,  1,  1,  1],\
                     [ 0,  0,  0,  0,  0,  0,  0,  0]]
        
rook_position =     [[ 7,  8,  8,  8,  8,  8,  8,  7],\
                     [10, 10, 10, 10, 10, 10, 10, 10],\
                     [ 9,  9,  9,  9,  9,  9,  9,  9],\
                     [ 3,  4,  5,  5,  5,  5,  4,  3],\
                     [ 1,  1,  2,  2,  2,  2,  1,  1],\
                     [ 1,  1,  1,  1,  1,  1,  1,  1],\
                     [ 3,  4,  5,  5,  5,  5,  4,  3],\
                     [ 3,  4,  5,  5,  5,  5,  4,  3]]
    
knight_position =   [[ 0,  0,  0,  0,  0,  0,  0,  0],\
                     [ 0,  2,  3,  4,  4,  3,  2,  0],\
                     [ 0,  5,  8, 10, 10,  8,  5,  0],\
                     [ 0,  0,  7,  9,  9,  7,  2,  0],\
                     [ 0,  0,  5,  8,  8,  5,  2,  0],\
                     [ 0,  1,  3,  4,  4,  3,  1,  0],\
                     [ 0,  0,  0,  1,  1,  0,  0,  0],\
                     [ 0,  0,  0,  0,  0,  0,  0,  0]]

bishop_position =   [[ 0,  0,  0,  0,  0,  0,  0,  0],\
                     [ 6,  7,  7,  7,  7,  7,  7,  6],\
                     [ 6,  7,  8,  9,  9,  8,  7,  6],\
                     [ 5,  7,  8, 10, 10,  8,  7,  5],\
                     [ 5,  7,  8, 10, 10,  8,  7,  5],\
                     [ 0,  1,  3,  4,  4,  3,  1,  0],\
                     [ 0,  0,  0,  1,  1,  0,  0,  0],\
                     [ 0,  0,  0,  0,  0,  0,  0,  0]]

queen_position =    [[ 0,  0,  0,  0,  0,  0,  0,  0],\
                     [ 6,  7,  7,  7,  7,  7,  7,  6],\
                     [ 6,  7,  8,  9,  9,  8,  7,  6],\
                     [ 5,  7,  8, 10, 10,  8,  7,  5],\
                     [ 5,  7,  8, 10, 10,  8,  7,  5],\
                     [ 0,  1,  3,  4,  4,  3,  1,  0],\
                     [ 0,  0,  0,  1,  1,  0,  0,  0],\
                     [ 0,  0,  0,  0,  0,  0,  0,  0]]
        
king_position =     [[-2, -3, -4, -5, -6, -4, -3, -2],\
                     [-2, -3, -4, -5, -6, -4, -3, -2],\
                     [-2, -3, -4, -5, -6, -4, -3, -2],\
                     [-2, -3, -4, -5, -6, -4, -3, -2],\
                     [-2, -3, -4, -5, -6, -4, -3, -2],\
                     [-2, -3, -4, -5, -6, -4, -3, -2],\
                     [ 1,  1,  1,  1,  1,  1,  1,  1],\
                     [10,  9,  8,  5,  5,  8,  9, 10]]
        
class gametree_node:
    
    
    def __init__(self, a_move):
        self.move = a_move
        self.children = None
        self.best_child_node = None # best child node
         

             
    """ TODO optimize """
    def get_evaluation(self, board, depth_to_go, threshold=None): # most time intensive method, takes 20 seconds for depth 1
        """ recursive function that returns the gametree node's evaluation.
            Positive for white, negative for black.
            Chessboard is after self.move is made
        """
        
        if(depth_to_go <= 0):
            return None, self.__heuristic_evaluation(board)
        
        if(self.children == None):
            self.children = self.get_children(board)
                
        start = datetime.datetime.now() # for development
        get_max = board.white_to_move() # if white to move, get max; if black to move, get min
        
        # initialize best_eval based on if getting max or getting min
        if(get_max):
            if(threshold == None):
                threshold = MAX_EVAL_POSSIBLE # check this
            best_eval = MIN_EVAL_POSSIBLE
        else:
            if(threshold == None):
                threshold = MIN_EVAL_POSSIBLE
            best_eval =  MAX_EVAL_POSSIBLE 
            
        # need better way of evaluating children. maybe only search children highest eval, use alpha-beta pruning
        for child in self.children:
            
            child_board = board.clone()
            assert(child_board.move(child.move))
            
            # takes about 1 second to analyze move with depth 1, actual heuristic eval takes no time
            temp, child_eval = child.get_evaluation(child_board, depth_to_go - 1, best_eval)
            
            if(get_max):
                if(child_eval > threshold):
                    return child, child_eval
                elif(child_eval > best_eval): # get max
                    best_eval = child_eval
                    self.best_child_node = child
            else:
                if(child_eval < threshold):
                    return child, child_eval 
                elif(child_eval < best_eval): # get min
                    best_eval = child_eval
                    self.best_child_node = child



        
        # for development                ##                        ##                        ##                        ##                        ##                        ##
        if(self.move != None):
            heuristic_eval = numpy.floor(100 * (self.__heuristic_evaluation(board) + .5))/100
            a_eval = numpy.floor(100 * (best_eval + .5))/100
            if(best_eval < 0):
                print("   "+str(heuristic_eval)+"    "+str(a_eval) + "    " +self.move.to_string()+"    "+ str(datetime.datetime.now() - start))
            else:
                print("    "+str(heuristic_eval)+"     "+str(a_eval) + "    " +self.move.to_string()+"    "+ str(datetime.datetime.now() - start))
        ##                                ##                        ##                        ##                        ##                        ##                        ##
         
         
         
         

        return self.best_child_node, best_eval
        

    
    def get_children(self, chessboard): # use list comprehension
        """ returns children gametree_nodes. chessboard is current state of game """
        # chessboard is current state of board after move has been made
        possible_moves = chessboard.get_possible_moves()
        children_nodes = []
        
        for a_move in possible_moves:
            
            children_nodes.append(gametree_node(a_move))
        
        return children_nodes # [gametree_node(a_move) for a_move in chessboard.get_possible_moves]
    
    """                                               """
    """                                               """
    """                PRIVATE METHODS                """
    """                                               """
    """                                               """

    
    def __heuristic_evaluation(self, chessboard):
        """ returns a position score for specified chessboard. positive for white, negative for black. """
        board = chessboard.get_board()
        sum = 0
        
        if(chessboard.game_complete):
            if(chessboard.white_to_move()):
                return MIN_EVAL_POSSIBLE
            else:
                return  MAX_EVAL_POSSIBLE
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                sum += self.__heuristically_evaluate_board_material(board[row][col])
                sum += POSITION_SCALE * self.__heuristically_evaluate_board_position(board[row][col], row, col)
                
        return sum 
    
    def __heuristically_evaluate_board_position(self, piece, row, col): # make better evaluation
        """ #returns the position score of piece in row, col from piece lookup table """
        
        if(piece == 0):
            return 0
        elif(piece == 1):
            return pawn_position[row][col]
        elif(piece == 2):
            return rook_position[row][col]
        elif(piece == 3):
            return knight_position[row][col]
        elif(piece == 4):
            return bishop_position[row][col]
        elif(piece == 5):
            return queen_position[row][col]
        elif(piece == 6):
            return king_position[row][col]
        elif(piece == -1):
            return pawn_position[7-row][7-col] * -1
        elif(piece == -2):
            return rook_position[7-row][7-col] * -1
        elif(piece == -3):
            return knight_position[7-row][7-col] * -1
        elif(piece == -4):
            return bishop_position[7-row][7-col] * -1
        elif(piece == -5):
            return queen_position[7-row][7-col] * -1
        elif(piece == -6):
            return king_position[7-row][7-col] * -1
        else:
            raise ValueError(str(piece))
    
    def __heuristically_evaluate_board_material(self, piece):
        """ #returns the material score of specified piece """
        
        if(piece == 0):
            return 0
        elif(piece == 1):
            return PAWN_VALUE
        elif(piece == 2):
            return ROOK_VALUE
        elif(piece == 3):
            return KNIGHT_VALUE
        elif(piece == 4):
            return BISHOP_VALUE
        elif(piece == 5):
            return QUEEN_VALUE
        elif(piece == 6):
            return KING_VALUE
        elif(piece == -1):
            return PAWN_VALUE * -1
        elif(piece == -2):
            return ROOK_VALUE * -1
        elif(piece == -3):
            return KNIGHT_VALUE * -1
        elif(piece == -4):
            return BISHOP_VALUE * -1
        elif(piece == -5):
            return QUEEN_VALUE * -1
        elif(piece == -6):
            return KING_VALUE * -1
        else:
            raise ValueError(str(piece))
=======

class gametree_node:
    
    def __init__(self, board, eval, parent_node, children_nodes, move, dpt):
        self.chessboard = board
        self.evaluation = eval
        self.children = children_nodes
        self.parent = parent_node
        self.last_move = move
        self.depth = dpt # depth in tree
      
      
      
    def get_best_move(self):
        pass  
        return best_node, best_move
    
    def get_evaluation(self):
        pass
        """ this method returns the current board evaluation. pos for white, neg for black """
    """                                               """
    """                                               """
    """                PRIVATE METHODS                """
    """                                               """
    """                                               """

    
    def __player_to_move(self):
        """ this method returns true if it is the player's move (not the engine's move) """
        
        return (self.chessboard.white_to_move() and (self.sign < 0)) or (not self.chessboard.white_to_move() and (self.sign > 0))
    def __heuristically_evaluate_board(self, chessboard):
        """ returns a position score for specified chessboard. positive for white, negative for black. """
        
        board = chessboard.get_board()
        sum = 0
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                sum += self.__heuristically_evaluate_board_material(board[row][col])
                sum += self.POSITION_SCALE * self.__heuristically_evaluate_board_position(board[row][col], row, col)
                
        return sum 
    def __heuristically_evaluate_board_position(self, piece, row, col):
        """ returns the position score of piece in row, col from piece lookup table """
        
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
    def __heuristically_evaluate_board_material(self, piece):
        """ returns the material score of specified piece """
        
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
    

    def __get_children_of_node(self, node):
        """ returns [children (in a tree) chessboards, evals of chessboards] """
        
        possible_moves = node.chessboard.get_possible_moves()
        children_nodes = []
        
        for a_move in possible_moves:
            copy = node.chessboard.clone()
            copy.move(a_move)
            
            children_nodes.extend(gametree_node(copy, self.__eval_board(copy), node, [], move))
        
        return children_nodes
    
        
    def __new_gametree_node(self, chessboard, parent = None, move = None):
        node = gametree_node(chessboard, self.__heuristically_evaluate_board(chessboard), parent, None, move)
        node.children = self.__get_children_of_node(node)
        return node
     
        
    def __get_best_move(self, max_depth):
        """ returns the best move for current position """
        
        self.__evaluate_gametree_node(self.gametree)
        max_score = -100000
        
        for child in self.gametree.children:
            if(child.evaluation > max_score):
                max_score = child.evaluation
                max_node = child
        
        return max_node.last_move
    
    def __evaluate_gametree_node(self, node):
        if(node.children == None):
            node.children = self.__get_children_of_node(node)
            
        for child in node.children:
            if(True): # if search should stop after this node
                return child.evaluation
            child.evaluation = self.explore_node(child)
            
        # need to decide whether to min or max based on depth
        if(node.chessboard.__player_to_move()): # children node moves are player moves
            node.evaluation = math.min(node.children)
        else: # children node moves are engine moves
            node.evaluation = math.max(node.children)

    
            
     
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
