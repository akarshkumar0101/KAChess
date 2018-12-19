
class pychess_board_engine:
    
    
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
    
    # makes a new engine with userPlayingWhite specifying whether the user is playing white
    def __init__(self, board_setup = None, white_to_move = True, user_plays_white = True):
        self.pychess_board_board = pychess_board(self, board_setup, to_move)
        self.userPlaysWhite = user_plays_white
        self.engineToMove = not user_plays_white
    
    
    
    def evaluateBoard(self):
        position = self.pychess_board.getpychess_board()
        
        self.evaluation = 0 # reset evaluation
        
        # get position metrics
        # material
        self.evaluation += evaluateMaterial()
        
        # position
        self.evaluation += evaluatePosition()
        
    
    # returns a position score (double)
    def evaluatePosition(self):
        # TODO implement evaluatePosition
        return 0
    
    # returns a position score (double)
    def evaluateMaterial(self):
        # TODO implement evaluateMaterial
        return 0
    
    
    # returns move in form [startRow, startCol, endRow, endCol]
    def getBestMove(self, millisecondsToThink):
        # TODO implement getBestMove
        return []
    
    
    def play(self):
        if(engineToMove):
            nextMove = getBestMove(2000)
            self.pychess_board.move(nextMove[0], nextMove[1], nextMove[2], nextMove[3])
        
    

