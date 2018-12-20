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
        board_setup = [[0,0,0,0,0,-5,0,0],[0,0,0,0,0,0,0,0],[-2,0,0,0,0,0,0,0],[0,0,0,6,0,0,0,0],[-2,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        cb = pychess_board(board_setup)
        tester = pychess_board(board_setup)
        cb, tester = self.Test_move(cb, tester, self.new_move(3,3,3,4))
    
        
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
        startRow, startCol, endRow, endCol = self.parse(move)
        
        chess_board.move(self.new_move(startRow,startCol,endRow,endCol))
        tester_board = self.move_no_check(startRow,startCol,endRow,endCol, tester_board)
        print(chess_board.to_string())
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
    
    
    def parse(self, move):
        if(len(move) == 4): # move is a list
            startRow = move[0]
            startCol = move[1]
            endRow   = move[2]
            endCol   = move[3] 
        else: # move is a string
            # can't be used for compound moves
            squares = move.split(",")
            
            startRow = self.num_to_square(squares[0][1])
            startCol = self.letter_to_square(squares[0][0])
            endRow = self.num_to_square(squares[1][1])
            endCol = self.letter_to_square(squares[1][0])
        
        return startRow, startCol, endRow, endCol
    
   
if(__name__ == "__main__"):
    py = pychess_board_engine()
    py.main()
