from pychess_board import pychess_board

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
        
    def main(self):
        cb = pychess_board()
        tester = pychess_board()
        
        # uses en passant
        
        # e4
        cb.move(self.new_move(6, 4, 4 ,4))
        tester = self.move_no_check(6, 4, 4, 4, tester)
        print(cb.to_string())
        
        # e5
        cb.move(self.new_move(1, 4, 3 ,4))
        tester = self.move_no_check(1, 4, 3 ,4, tester)
        print(cb.to_string())
        
        # Nf3
        cb.move(self.new_move(7, 6, 5 ,5))
        tester = self.move_no_check(7, 6, 5 ,5, tester)
        print(cb.to_string())
        
        # Nc6
        cb.move(self.new_move(0, 1, 2, 2))
        tester = self.move_no_check(0, 1, 2, 2, tester)
        print(cb.to_string())
        
        # d4
        cb.move(self.new_move(6, 3, 4 ,3))
        tester = self.move_no_check(6, 3, 4 ,3, tester)
        print(cb.to_string())
        
        # exd4
        cb.move(self.new_move(3, 4, 4, 3))
        tester = self.move_no_check(3, 4, 4, 3, tester)
        print(cb.to_string())
        
        # Nxd4
        cb.move(self.new_move(5 ,5, 4, 3))
        tester = self.move_no_check(5 ,5, 4, 3, tester)
        print(cb.to_string())
        
        # Nf6
        cb.move(self.new_move(0, 6, 2, 5))
        tester = self.move_no_check(0, 6, 2, 5, tester)
        print(cb.to_string())
        
        # Nxc6
        cb.move(self.new_move(4, 3, 2, 2))
        tester = self.move_no_check(4, 3, 2, 2, tester)
        print(cb.to_string())
        
        # bxc6
        cb.move(self.new_move(1,1,2,2))
        tester = self.move_no_check(1,1,2,2, tester)
        print(cb.to_string())
        
        # e5
        cb.move(self.new_move(4,4,3,4))
        tester = self.move_no_check(4,4,3,4, tester)
        print(cb.to_string())
        
        # Qe7
        cb.move(self.new_move(0,3,1,4))
        tester = self.move_no_check(0,3,1,4, tester)
        print(cb.to_string())
        
        # Qe2
        cb.move(self.new_move(7,3,6,4))
        tester = self.move_no_check(7,3,6,4, tester)
        print(cb.to_string())
        
        # Nd5
        cb.move(self.new_move(2,5,3,3))
        tester = self.move_no_check(2,5,3,3, tester)
        print(cb.to_string())
        
        # c4
        cb.move(self.new_move(6,2,4,2))
        tester = self.move_no_check(6,2,4,2, tester)
        print(cb.to_string())
        
        # Nb6
        cb.move(self.new_move(3,3,2,1))
        tester = self.move_no_check(3,3,2,1, tester)
        print(cb.to_string())
        
        # Nc3
        cb.move(self.new_move(7,1,5,2))
        tester = self.move_no_check(7,1,5,2, tester)
        print(cb.to_string())
        
        # Qe6
        cb.move(self.new_move(1,4,2,4))
        tester = self.move_no_check(1,4,2,4, tester)
        print(cb.to_string())
        
        # Qe4
        cb.move(self.new_move(6,4,4,4))
        tester = self.move_no_check(6,4,4,4, tester)
        print(cb.to_string())
        
        # Bb4
        cb.move(self.new_move(0,5,4,1))
        tester = self.move_no_check(0,5,4,1, tester)
        print(cb.to_string())
        
        # Bd2
        cb.move(self.new_move(7,2,6,3))
        tester = self.move_no_check(7,2,6,3, tester)
        print(cb.to_string())
        
        # Bb7
        cb.move(self.new_move(0,2,1,1))
        tester = self.move_no_check(0,2,1,1, tester)
        print(cb.to_string())
        
        # Bd3
        cb.move(self.new_move(7,5,5,3))
        tester = self.move_no_check(7,5,5,3, tester)
        print(cb.to_string())
        
        # 0-0-0
        cb.move(self.new_move(0,4,0,2))
        tester = self.move_no_check(0,4,0,2, tester)
        tester = self.move_no_check(0,0,0,3, tester)
        print(cb.to_string())
        
        # 0-0-0
        cb.move(self.new_move(7,4,7,2))
        tester = self.move_no_check(7,4,7,2, tester)
        tester = self.move_no_check(7,0,7,3, tester)
        print(cb.to_string())
        
        # c5
        cb.move(self.new_move(2,2,3,2))
        tester = self.move_no_check(2,2,3,2, tester)
        print(cb.to_string())
        
        # Qe2
        cb.move(self.new_move(4,4,6,4))
        tester = self.move_no_check(4,4,6,4, tester)
        print(cb.to_string())
        
        # Re8
        cb.move(self.new_move(0,7,0,4))
        tester = self.move_no_check(0,7,0,4, tester)
        print(cb.to_string())
        
        # f4
        cb.move(self.new_move(6,5,4,5))
        tester = self.move_no_check(6,5,4,5, tester)
        print(cb.to_string())
        
        # d6
        cb.move(self.new_move(1,3,2,3))
        tester = self.move_no_check(1,3,2,3, tester)
        print(cb.to_string())
        
        # a3
        cb.move(self.new_move(6,0,5,0))
        tester = self.move_no_check(6,0,5,0, tester)
        print(cb.to_string())
        
        # Bxc3
        cb.move(self.new_move(4,1,5,2))
        tester = self.move_no_check(4,1,5,2, tester)
        print(cb.to_string())
        
        # Bxc3
        cb.move(self.new_move(6,3,5,2))
        tester = self.move_no_check(6,3,5,2, tester)
        print(cb.to_string())
        
        # g6
        cb.move(self.new_move(1,6,2,6))
        tester = self.move_no_check(1,6,2,6, tester)
        print(cb.to_string())
        
        # Rhf1
        cb.move(self.new_move(7,7,7,5))
        tester = self.move_no_check(7,7,7,5, tester)
        print(cb.to_string())
        
        # Na4
        cb.move(self.new_move(2,1,4,0))
        tester = self.move_no_check(2,1,4,0, tester)
        print(cb.to_string())
        
        # Ba5
        cb.move(self.new_move(5,2,3,0))
        tester = self.move_no_check(5,2,3,0, tester)
        print(cb.to_string())
        
        # dxe5
        cb.move(self.new_move(2,3,3,4))
        tester = self.move_no_check(2,3,3,4, tester)
        print(cb.to_string())
        
        # fxe5
        cb.move(self.new_move(4,5,3,4))
        tester = self.move_no_check(4,5,3,4, tester)
        print(cb.to_string())
        
        # f5
        cb.move(self.new_move(1,5,3,5))
        tester = self.move_no_check(1,5,3,5, tester)
        print(cb.to_string())
        
        # exf6!
        cb.move(self.new_move(3,4,2,5))
        tester = self.move_no_check(3,4,2,5, tester)
        tester = self.move_no_check(3,4,3,5, tester) # fill 3,5, with empty square
        print(cb.to_string())
        
    def move_no_check(self, startRow, startCol, endRow, endCol, b):
        output = b.get_board()
        piece = output[startRow][startCol]
        output[startRow][startCol] = 0
        output[endRow][endCol] = piece
        return pychess_board(output, True)
    
    def new_move(self, startRow, startCol, endRow, endCol):
        output = []
        output.append(startRow)
        output.append(startCol)
        output.append(endRow)
        output.append(endCol)
        return output
    
   
if(__name__ == "__main__"):
    py = pychess_board_engine()
    py.main()
