import unittest
import pychess


class ChessboardTest(unittest.TestCase):


    def Test_Rook_Movement_In_Starting_Position(self):
        cb = new Chessboard()
        
        # top right rook
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(0, 7, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        # top left rook
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(0, 0, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        # bottom left rook
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(7, 0, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        # bottom right rook
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(7, 7, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
 """       
    
    @Test
    @DisplayName("testing starting position bishop movement")
    void Test_Bishop_Movement_In_Starting_Position() :
        Chessboard cb = new Chessboard()
        
        # bottom left bishop
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(7, 2, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        # top left bishop
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(0, 2, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        # top right bishop
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(0, 5, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        # bottom right bishop
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(7, 5, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
    
    @Test
    @DisplayName("testing starting position king movement")
    void Test_King_Movement_In_Starting_Position() :
        Chessboard cb = new Chessboard()

        # white king
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(7, 4, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        # black king
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(0, 4, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
    
    @Test
    @DisplayName("testing starting position queen movement")
    void Test_Queen_Movement_In_Starting_Position() :
        Chessboard cb = new Chessboard()
        
        # black queen
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(0, 3, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        # white queen
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(7, 3, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
    
    @Test
    @DisplayName("testing starting position pawn movement")
    void Test_Pawn_Movement_In_Starting_Position() :
        
        Chessboard cb = new Chessboard()

        # test all black pawns to make sure they don't move (bc not their turn)
        int pawnRow = 2 
        for(int pawnCol = 0 pawnCol < 8 pawnCol++) :
            for(int i = 0 i < 8 i++) :
                for(int j = 0 j < 8 j++) :
                    cb.move(pawnRow, pawnCol, i, j)
                    assertBoardsEqual(cb, new Chessboard())
                
            
        
        
        pawnRow = 6 
        for(int pawnCol = 0 pawnCol < 8 pawnCol++) :
            for(int toRow = 0 toRow < 8 toRow++) :
                for(int toCol = 0 toCol < 8 toCol++) :
                    cb.move(pawnRow, pawnCol, toRow, toCol)
                    
                    if((toRow == 5 || toRow == 4) && pawnCol - toCol == 0) :
                        assertBoardsEqual(cb, move(pawnRow, pawnCol, toRow, toCol, new Chessboard()))
                        cb = new Chessboard()
                    else :
                        assertBoardsEqual(cb, new Chessboard())
                    
                
            
        
        
        
    
    @Test
    @DisplayName("testing starting position knight movement")
    void Test_Knight_Movement_In_Starting_Position() :
        
        Chessboard cb = new Chessboard()
        
        # black knights not supposed to move on first turn
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(0, 1, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(0, 6, i, j)
                assertBoardsEqual(cb, new Chessboard())
            
        
        
        
        # white knights
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(7, 1, i, j)
                if((i == 5 && j == 0) ||(i == 5 && j == 2)) :
                    assertBoardsEqual(cb, move(7, 1, i, j, new Chessboard()))
                    cb = new Chessboard()
                else :
                    assertBoardsEqual(cb, new Chessboard())
                
            
        
        
        
        for(int i = 0 i < 8 i++) :
            for(int j = 0 j < 8 j++) :
                cb.move(7, 6, i, j)
                if((i == 5 && j == 5) || (i == 5 && j == 7)) :
                    assertBoardsEqual(cb, move(7, 6, i, j, new Chessboard()))
                    cb = new Chessboard()
                else :
                    assertBoardsEqual(cb, new Chessboard())
                
            
        
        
    
    
    # TODO write tests when king is in check
    
    # TODO write test for castling 
    
    # FIXME write tests for en passant
    
    # TODO write tests for king moving into check
    
    # FIXME write tests for checkmate
    
    # TODO write more complicated tests
    
    # TODO test get moves
    
    # FIXME make sure chessboard follows real game moves
    @Test
    @DisplayName("Simple Game 1")
    void Simple_Game_1() :
        Chessboard cb = new Chessboard()
        Chessboard tester = new Chessboard()
        
        cb.move(6, 4, 4 ,4)
        tester = move(6, 4, 4, 4, tester)
        assertBoardsEqual(cb, tester)
        
        cb.move(1, 4, 3 ,4)
        tester = move(1, 4, 3 ,4, tester)
        assertBoardsEqual(cb, tester)
        
        cb.move(7, 6, 5 ,5)
        tester = move(7, 6, 5 ,5, tester)
        assertBoardsEqual(cb, tester)
        
        cb.move(1, 1, 3, 1)
        tester = move(1, 1, 3, 1, tester)
        assertBoardsEqual(cb, tester)
        
        cb.move(5, 5, 4 ,3)
        tester = move(5, 5, 4 ,3, tester)
        assertBoardsEqual(cb, tester)
        
        cb.move(3, 4, 4, 3)
        tester = move(3, 4, 4, 3, tester)
        assertBoardsEqual(cb, tester)
    
    
    @Test
    @DisplayName("Simple Game 2")
    void Simple_Game_2() :
        Chessboard cb = new Chessboard()
        Chessboard tester = new Chessboard()
        
        # uses en passant
        
        # e4
        cb.move(6, 4, 4 ,4)
        tester = move(6, 4, 4, 4, tester)
        assertBoardsEqual(cb, tester)
        
        # e5
        cb.move(1, 4, 3 ,4)
        tester = move(1, 4, 3 ,4, tester)
        assertBoardsEqual(cb, tester)
        
        # Nf3
        cb.move(7, 6, 5 ,5)
        tester = move(7, 6, 5 ,5, tester)
        assertBoardsEqual(cb, tester)
        
        # Nc6
        cb.move(0, 1, 2, 2)
        tester = move(0, 1, 2, 2, tester)
        assertBoardsEqual(cb, tester)
        
        # d4
        cb.move(6, 3, 4 ,3)
        tester = move(6, 3, 4 ,3, tester)
        assertBoardsEqual(cb, tester)
        
        # exd4
        cb.move(3, 4, 4, 3)
        tester = move(3, 4, 4, 3, tester)
        assertBoardsEqual(cb, tester)
        
        # Nxd4
        cb.move(5 ,5, 4, 3)
        tester = move(5 ,5, 4, 3, tester)
        assertBoardsEqual(cb, tester)
        
        # Nf6
        cb.move(0, 6, 2, 5)
        tester = move(0, 6, 2, 5, tester)
        assertBoardsEqual(cb, tester)
        
        # Nxc6
        cb.move(4, 3, 2, 2)
        tester = move(4, 3, 2, 2, tester)
        assertBoardsEqual(cb, tester)
        
        # bxc6
        cb.move(1,1,2,2)
        tester = move(1,1,2,2, tester)
        assertBoardsEqual(cb, tester)
        
        # e5
        cb.move(4,4,3,4)
        tester = move(4,4,3,4, tester)
        assertBoardsEqual(cb, tester)
        
        # Qe7
        cb.move(0,3,1,4)
        tester = move(0,3,1,4, tester)
        assertBoardsEqual(cb, tester)
        
        # Qe2
        cb.move(7,3,6,4)
        tester = move(7,3,6,4, tester)
        assertBoardsEqual(cb, tester)
        
        # Nd5
        cb.move(2,5,3,3)
        tester = move(2,5,3,3, tester)
        assertBoardsEqual(cb, tester)
        
        # c4
        cb.move(6,2,4,2)
        tester = move(6,2,4,2, tester)
        assertBoardsEqual(cb, tester)
        
        # Nb6
        cb.move(3,3,2,1)
        tester = move(3,3,2,1, tester)
        assertBoardsEqual(cb, tester)
        
        # Nc3
        cb.move(7,1,5,2)
        tester = move(7,1,5,2, tester)
        assertBoardsEqual(cb, tester)
        
        # Qe6
        cb.move(1,4,2,4)
        tester = move(1,4,2,4, tester)
        assertBoardsEqual(cb, tester)
        
        # Qe4
        cb.move(6,4,4,4)
        tester = move(6,4,4,4, tester)
        assertBoardsEqual(cb, tester)
        
        # Bb4
        cb.move(0,5,4,1)
        tester = move(0,5,4,1, tester)
        assertBoardsEqual(cb, tester)
        
        # Bd2
        cb.move(7,2,6,3)
        tester = move(7,2,6,3, tester)
        assertBoardsEqual(cb, tester)
        
        # Bb7
        cb.move(0,2,1,1)
        tester = move(0,2,1,1, tester)
        assertBoardsEqual(cb, tester)
        
        # Bd3
        cb.move(7,5,5,3)
        tester = move(7,5,5,3, tester)
        assertBoardsEqual(cb, tester)
        
        # 0-0-0
        cb.move(0,4,0,2)
        tester = move(0,4,0,2, tester)
        tester = move(0,0,0,3, tester)
        assertBoardsEqual(cb, tester)
        
        # 0-0-0
        cb.move(7,4,7,2)
        tester = move(7,4,7,2, tester)
        tester = move(7,0,7,3, tester)
        assertBoardsEqual(cb, tester)
        
        # c5
        cb.move(2,2,3,2)
        tester = move(2,2,3,2, tester)
        assertBoardsEqual(cb, tester)
        
        # Qe2
        cb.move(4,4,6,4)
        tester = move(4,4,6,4, tester)
        assertBoardsEqual(cb, tester)
        
        # Re8
        cb.move(0,7,0,4)
        tester = move(0,7,0,4, tester)
        assertBoardsEqual(cb, tester)
        
        # f4
        cb.move(6,5,4,5)
        tester = move(6,5,4,5, tester)
        assertBoardsEqual(cb, tester)
        
        # d6
        cb.move(1,3,2,3)
        tester = move(1,3,2,3, tester)
        assertBoardsEqual(cb, tester)
        
        # a3
        cb.move(6,0,5,0)
        tester = move(6,0,5,0, tester)
        assertBoardsEqual(cb, tester)
        
        # Bxc3
        cb.move(4,1,5,2)
        tester = move(4,1,5,2, tester)
        assertBoardsEqual(cb, tester)
        
        # Bxc3
        cb.move(6,3,5,2)
        tester = move(6,3,5,2, tester)
        assertBoardsEqual(cb, tester)
        
        # g6
        cb.move(1,6,2,6)
        tester = move(1,6,2,6, tester)
        assertBoardsEqual(cb, tester)
        
        # Rhf1
        cb.move(7,7,7,5)
        tester = move(7,7,7,5, tester)
        assertBoardsEqual(cb, tester)
        
        # Na4
        cb.move(2,1,4,0)
        tester = move(2,1,4,0, tester)
        assertBoardsEqual(cb, tester)
        
        # Ba5
        cb.move(5,2,3,0)
        tester = move(5,2,3,0, tester)
        assertBoardsEqual(cb, tester)
        
        # dxe5
        cb.move(2,3,3,4)
        tester = move(2,3,3,4, tester)
        assertBoardsEqual(cb, tester)
        
        # fxe5
        cb.move(4,5,3,4)
        tester = move(4,5,3,4, tester)
        assertBoardsEqual(cb, tester)
        
        # f5
        cb.move(1,5,3,5)
        tester = move(1,5,3,5, tester)
        assertBoardsEqual(cb, tester)
        
        # exf6!
        cb.move(3,4,2,5)
        tester = move(3,4,2,5, tester)
        tester = move(3,4,3,5, tester) # fill 3,5, with empty square
        assertBoardsEqual(cb, tester)
        
    
    
    # moves piece on Chessboard for easy testing
    private Chessboard move(int startRow, int startCol, int endRow, int endCol, Chessboard b):
        int[][] output = b.getBoard()
        int piece = output[startRow][startCol]
        output[startRow][startCol] = 0
        output[endRow][endCol] = piece
        return new Chessboard(output, true)
    
    
    # given: board dimensions are equal
    # test whether boards are equal
    
"""

def assertBoardsEqual(a, b) :
    boardA = a.getBoard()
    boardB = b.getBoard()
    
    for i in range(len(boardA)):
        for j in range(len(boardA[0])):
            assertEqual(boardA[i][j], boardB[i][j])
        
