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
    
    def assertBoardsEqual(self, a, b):
        boardA = a.get_board()
        boardB = b.get_board()
        
        for i in range(len(boardA)):
            for j in range(len(boardA[0])):
                self.assertEqual(boardA[i][j], boardB[i][j])
        

    
    # makes a new engine with userPlayingWhite specifying whether the user is playing white
    def __init__(self, board_setup = None, white_to_move = True, user_plays_white = True):
        self.pychess_board_board = pychess_board(board_setup, white_to_move)
        self.userPlaysWhite = user_plays_white
        self.engineToMove = not user_plays_white
    
    
    
    def evaluateBoard(self):
        position = self.pychess_board.getpychess_board()
        
        self.evaluation = 0 # reset evaluation
        
        # get position metrics
        # material
        self.evaluation += self.evaluateMaterial()
        
        # position
        self.evaluation += self.evaluatePosition()
        
    
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
        
    def main(self):
        pass
if(__name__ == "__main__"):
    py = pychess_board_engine()
    py.main()
