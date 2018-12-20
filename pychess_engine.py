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
        cb, tester = self.Test_move(cb, tester, "c2,c4")
        cb, tester = self.Test_move(cb, tester, "b7,b6")
        cb, tester = self.Test_move(cb, tester, "d2,d3")
        cb, tester = self.Test_move(cb, tester, "c8,a6")
        cb, tester = self.Test_move(cb, tester, "b2,b4")
        cb, tester = self.Test_move(cb, tester, "b8,c6")
        cb, tester = self.Test_move(cb, tester, "b4,b5")
        cb, tester = self.Test_move(cb, tester, "a6,b5")
        cb, tester = self.Test_move(cb, tester, "c4,b5")
        cb, tester = self.Test_move(cb, tester, "c6,d4")
        cb, tester = self.Test_move(cb, tester, "e2,e3")
        
        cb, tester = self.Test_move(cb, tester, "d4,b5")
        cb, tester = self.Test_move(cb, tester, "b1,c3")
        cb, tester = self.Test_move(cb, tester, "e7,e6")
        cb, tester = self.Test_move(cb, tester, "c3,b5")
        cb, tester = self.Test_move(cb, tester, "a7,a6")
        cb, tester = self.Test_move(cb, tester, "b5,c7")
        cb, tester = self.Test_move(cb, tester, "d8,c7")
        cb, tester = self.Test_move(cb, tester, "a2,a4")
        
        cb, tester = self.Test_move(cb, tester, "f8,b4")
        cb, tester = self.Test_move(cb, tester, "c1,d2")
        cb, tester = self.Test_move(cb, tester, "b4,c5")
        cb, tester = self.Test_move(cb, tester, "g1,f3")
        cb, tester = self.Test_move(cb, tester, "g8,f6")
        cb, tester = self.Test_move(cb, tester, "f3,e5")
        cb, tester = self.Test_move(cb, tester, "c7,e5")
        cb, tester = self.Test_move(cb, tester, "e3,e4")
        cb, tester = self.Test_move(cb, tester, "e5,d4")
        cb, tester = self.Test_move(cb, tester, "d1,g4")
        
        cb, tester = self.Test_move(cb, tester, "f6,g4")
        cb, tester = self.Test_move(cb, tester, "g2,g3")
        cb, tester = self.Test_move(cb, tester, "d4,f2")
        cb, tester = self.Test_move(cb, tester, "e1,d1")
        cb, tester = self.Test_move(cb, tester, "f2,f3")
        cb, tester = self.Test_move(cb, tester, "d1,c2")
        cb, tester = self.Test_move(cb, tester, "f3,h1")
        cb, tester = self.Test_move(cb, tester, "d2,g5")
        cb, tester = self.Test_move(cb, tester, "a8,c8")
        print(cb.to_string())
        cb, tester = self.Test_move(cb, tester, "a1,b1")
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
    
    def Test_move(self, chess_board, tester_board, move): # startsqr, comma, endsqr ex: d2,d4
        
        squares = move.split(",")
        
        startRow = self.num_to_square(squares[0][1])
        startCol = self.letter_to_square(squares[0][0])
        endRow = self.num_to_square(squares[1][1])
        endCol = self.letter_to_square(squares[1][0])
        
        chess_board.move(self.new_move(startRow,startCol,endRow,endCol))
        tester_board = self.move_no_check(startRow,startCol,endRow,endCol, tester_board)
        return chess_board, tester_board
     
    def num_to_square(self, num):
        return 8 - int(num)
       
    def letter_to_square(self, letter):
        if(letter == "a"):
            return 0
        elif(letter == "b"):
            return 1
        elif(letter == "c"):
            return 2
        elif(letter == "d"):
            return 3
        elif(letter == "e"):
            return 4
        elif(letter == "f"):
            return 5
        elif(letter == "g"):
            return 6
        elif(letter == "h"):
            return 7
        
   
if(__name__ == "__main__"):
    py = pychess_board_engine()
    py.main()
