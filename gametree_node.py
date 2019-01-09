
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

    
            
     
