
class ChessEngine:
    
    int evaluation
    Chessboard board
    boolean userPlaysWhite
    boolean engineToMove
    
    """
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
    public ChessEngine(boolean userPlayingWhite):
        board = new Chessboard()
        userPlaysWhite = userPlayingWhite
        engineToMove = !userPlayingWhite
    
    
    public static void main(String args[]):
        
    
    
    public void evaluateBoard():
        int[][] position = board.getBoard()
        
        evaluation = 0 # reset evaluation
        
        # get position metrics
        # material
        evaluation += evaluateMaterial()
        
        # position
        evaluation += evaluatePosition()
        
    
    
    public int evaluatePosition():
        # TODO implement evaluatePosition
        return 0
    
    
    public int evaluateMaterial():
        # TODO implement evaluateMaterial
        return 0
    
    
    # returns int[] with len 4 
    #:startRow, startCol, endRow, endCol
    public static int[] getBestMove(int millisecondsToThink):
        # TODO implement getBestMove
        return new int[0]
    
    
    public void play():
        if(engineToMove):
            int[] nextMove = getBestMove(2000)
            board.move(nextMove[0], nextMove[1], nextMove[2], nextMove[3])
        
    

