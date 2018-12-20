import unittest
from pychess_board import pychess_board


class pychess_board_test(unittest.TestCase):

    def assertBoardsEqual(self, a, b):
        boardA = a.getBoard()
        boardB = b.getBoard()
        
        for i in range(len(boardA)):
            for j in range(len(boardA[0])):
                self.assertEqual(boardA[i][j], boardB[i][j])
        

    def test_Rook_Movement_In_Starting_Position(self):
        cb = pychess_board()
        
        # top right rook
        for i in range(8):
            for j in range(8):
                cb.move(0, 7, i, j)
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(0, 0, i, j)
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(7, 0, i, j)
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(7, 7, i, j)
                self.assertBoardsEqual(cb, pychess_board())
        
    
    def test_Bishop_Movement_In_Starting_Position(self):
<<<<<<< HEAD
        cb = pychess_board()
=======
        cb = pychess_board
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
        
        # bottom left bishop
        for i in range(8):
            for j in range(8):
<<<<<<< HEAD
                cb.move(7, 2, i, j)
                self.assertBoardsEqual(cb, pychess_board())
=======
                cb.move(cb, 7, 2, i, j)
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                cb.move(0, 2, i, j)
<<<<<<< HEAD
                self.assertBoardsEqual(cb, pychess_board())
=======
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                cb.move(0, 5, i, j)
<<<<<<< HEAD
                self.assertBoardsEqual(cb, pychess_board())
=======
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                cb.move(7, 5, i, j)
<<<<<<< HEAD
                self.assertBoardsEqual(cb, pychess_board())
=======
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess

    
    def test_King_Movement_In_Starting_Position(self):
        cb = pychess_board()

        for i in range(8):
            for j in range(8):
                cb.move(7, 4, i, j)
<<<<<<< HEAD
                self.assertBoardsEqual(cb, pychess_board())
=======
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                cb.move(0, 4, i, j)
<<<<<<< HEAD
                self.assertBoardsEqual(cb, pychess_board())
=======
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
        
    
    def test_Queen_Movement_In_Starting_Position(self):
        cb = pychess_board()
        
        # black queen
        for i in range(8):
            for j in range(8):
                cb.move(0, 3, i, j)
<<<<<<< HEAD
                self.assertBoardsEqual(cb, pychess_board())
=======
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                cb.move(7, 3, i, j)
<<<<<<< HEAD
                self.assertBoardsEqual(cb, pychess_board())
=======
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
            
    
    def test_Pawn_Movement_In_Starting_Position(self):
        
        cb = pychess_board()

        # test all black pawns to make sure they don't move (bc not their turn)
        pawnRow = 2 
        for pawnCol in range(8):
            for i in range(8):
                for j in range(8):
                    cb.move(pawnRow, pawnCol, i, j)
<<<<<<< HEAD
                    self.assertBoardsEqual(cb, pychess_board())
=======
                    assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                
            
        
        
        pawnRow = 6 
        for pawnCol in range(8):
            for toRow in range(8):
                for toCol in range(8):
                    cb.move(pawnRow, pawnCol, toRow, toCol)
                    
                    if((toRow == 5 or toRow == 4) and pawnCol - toCol == 0):
<<<<<<< HEAD
                        self.assertBoardsEqual(cb, self.move_no_check(pawnRow, pawnCol, toRow, toCol, pychess_board()))
=======
                        assertBoardsEqual(cb, move(pawnRow, pawnCol, toRow, toCol, pychess_board()))
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                        cb = pychess_board()
                    else:
<<<<<<< HEAD
                        self.assertBoardsEqual(cb, pychess_board())
=======
                        assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                    
    
    def test_Knight_Movement_In_Starting_Position(self):
        
        cb = pychess_board()
        
        # black knights not supposed to move on first turn
        for i in range(8):
            for j in range(8):
                cb.move(0, 1, i, j)
<<<<<<< HEAD
                self.assertBoardsEqual(cb, pychess_board())
=======
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                cb.move(0, 6, i, j)
<<<<<<< HEAD
                self.assertBoardsEqual(cb, pychess_board())
=======
                assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
        
        
        # white knights
        for i in range(8):
            for j in range(8):
                
                cb.move(7, 1, i, j)
                if((i == 5 and j == 0) or(i == 5 and j == 2)):
<<<<<<< HEAD
                    self.assertBoardsEqual(cb, self.move_no_check(7, 1, i, j, pychess_board()))
=======
                    assertBoardsEqual(cb, move(7, 1, i, j, pychess_board()))
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                    cb = pychess_board()
                else:
<<<<<<< HEAD
                    self.assertBoardsEqual(cb, pychess_board())
=======
                    assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                
                cb.move(7, 6, i, j)
                if((i == 5 and j == 5) or (i == 5 and j == 7)):
<<<<<<< HEAD
                    self.assertBoardsEqual(cb, self.move_no_check(7, 6, i, j, pychess_board()))
=======
                    assertBoardsEqual(cb, move(7, 6, i, j, pychess_board()))
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
                    cb = pychess_board()
                else:
<<<<<<< HEAD
                    self.assertBoardsEqual(cb, pychess_board())
=======
                    assertBoardsEqual(cb, pychess_board())
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
            
    
    # TODO write tests when king is in check
    
    # TODO write test for castling 
    
    # FIXME write tests for en passant
    
    # TODO write tests for king moving into check
    
    # FIXME write tests for checkmate
    
    # TODO write more complicated tests
    
    # TODO test get moves
    
    # FIXME make sure follows real game moves
    
    def test_Simple_Game_1(self):
        cb = pychess_board()
        tester = pychess_board()
        
        cb.move(6, 4, 4 ,4)
        tester = self.move_no_check(6, 4, 4, 4, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(1, 4, 3 ,4)
        tester = self.move_no_check(1, 4, 3 ,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(7, 6, 5 ,5)
        tester = self.move_no_check(7, 6, 5 ,5, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(1, 1, 3, 1)
        tester = self.move_no_check(1, 1, 3, 1, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(5, 5, 4 ,3)
        tester = self.move_no_check(5, 5, 4 ,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(3, 4, 4, 3)
        tester = self.move_no_check(3, 4, 4, 3, tester)
        self.assertBoardsEqual(cb, tester)
    
    
    
    def test_Simple_Game_2(self):
        cb = pychess_board()
        tester = pychess_board()
        
        # uses en passant
        
        # e4
        cb.move(6, 4, 4 ,4)
        tester = self.move_no_check(6, 4, 4, 4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # e5
        cb.move(1, 4, 3 ,4)
        tester = self.move_no_check(1, 4, 3 ,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nf3
        cb.move(7, 6, 5 ,5)
        tester = self.move_no_check(7, 6, 5 ,5, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nc6
        cb.move(0, 1, 2, 2)
        tester = self.move_no_check(0, 1, 2, 2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # d4
        cb.move(6, 3, 4 ,3)
        tester = self.move_no_check(6, 3, 4 ,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # exd4
        cb.move(3, 4, 4, 3)
        tester = self.move_no_check(3, 4, 4, 3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nxd4
        cb.move(5 ,5, 4, 3)
        tester = self.move_no_check(5 ,5, 4, 3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nf6
        cb.move(0, 6, 2, 5)
        tester = self.move_no_check(0, 6, 2, 5, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nxc6
        cb.move(4, 3, 2, 2)
        tester = self.move_no_check(4, 3, 2, 2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # bxc6
        cb.move(1,1,2,2)
        tester = self.move_no_check(1,1,2,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # e5
        cb.move(4,4,3,4)
        tester = self.move_no_check(4,4,3,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe7
        cb.move(0,3,1,4)
        tester = self.move_no_check(0,3,1,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe2
        cb.move(7,3,6,4)
        tester = self.move_no_check(7,3,6,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nd5
        cb.move(2,5,3,3)
        tester = self.move_no_check(2,5,3,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # c4
        cb.move(6,2,4,2)
        tester = self.move_no_check(6,2,4,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nb6
        cb.move(3,3,2,1)
        tester = self.move_no_check(3,3,2,1, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nc3
        cb.move(7,1,5,2)
        tester = self.move_no_check(7,1,5,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe6
        cb.move(1,4,2,4)
        tester = self.move_no_check(1,4,2,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe4
        cb.move(6,4,4,4)
        tester = self.move_no_check(6,4,4,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bb4
        cb.move(0,5,4,1)
        tester = self.move_no_check(0,5,4,1, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bd2
        cb.move(7,2,6,3)
        tester = self.move_no_check(7,2,6,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bb7
        cb.move(0,2,1,1)
        tester = self.move_no_check(0,2,1,1, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bd3
        cb.move(7,5,5,3)
        tester = self.move_no_check(7,5,5,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # 0-0-0
        cb.move(0,4,0,2)
        tester = self.move_no_check(0,4,0,2, tester)
        tester = self.move_no_check(0,0,0,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # 0-0-0
        cb.move(7,4,7,2)
        tester = self.move_no_check(7,4,7,2, tester)
        tester = self.move_no_check(7,0,7,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # c5
        cb.move(2,2,3,2)
        tester = self.move_no_check(2,2,3,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe2
        cb.move(4,4,6,4)
        tester = self.move_no_check(4,4,6,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Re8
        cb.move(0,7,0,4)
        tester = self.move_no_check(0,7,0,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # f4
        cb.move(6,5,4,5)
        tester = self.move_no_check(6,5,4,5, tester)
        self.assertBoardsEqual(cb, tester)
        
        # d6
        cb.move(1,3,2,3)
        tester = self.move_no_check(1,3,2,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # a3
        cb.move(6,0,5,0)
        tester = self.move_no_check(6,0,5,0, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bxc3
        cb.move(4,1,5,2)
        tester = self.move_no_check(4,1,5,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bxc3
        cb.move(6,3,5,2)
        tester = self.move_no_check(6,3,5,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # g6
        cb.move(1,6,2,6)
        tester = self.move_no_check(1,6,2,6, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Rhf1
        cb.move(7,7,7,5)
        tester = self.move_no_check(7,7,7,5, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Na4
        cb.move(2,1,4,0)
        tester = self.move_no_check(2,1,4,0, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Ba5
        cb.move(5,2,3,0)
        tester = self.move_no_check(5,2,3,0, tester)
        self.assertBoardsEqual(cb, tester)
        
        # dxe5
        cb.move(2,3,3,4)
        tester = self.move_no_check(2,3,3,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # fxe5
        cb.move(4,5,3,4)
        tester = self.move_no_check(4,5,3,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # f5
        cb.move(1,5,3,5)
        tester = self.move_no_check(1,5,3,5, tester)
        self.assertBoardsEqual(cb, tester)
        
        # exf6!
        cb.move(3,4,2,5)
        tester = self.move_no_check(3,4,2,5, tester)
        tester = self.move_no_check(3,4,3,5, tester) # fill 3,5, with empty square
        self.assertBoardsEqual(cb, tester)
        
    
    
    # moves piece on for easy testing
<<<<<<< HEAD
    
    def move_no_check(self, startRow, startCol, endRow, endCol, b):
=======
    def move(startRow, startCol, endRow, endCol, b):
>>>>>>> branch 'master' of https://github.com/akarshkumar0101/KAChess
        output = b.getBoard()
        piece = output[startRow][startCol]
        output[startRow][startCol] = 0
        output[endRow][endCol] = piece
        return pychess_board(output, True)
    
    
    # given: board dimensions are equal
    # test whether boards are equal


    
if __name__ == '__main__':
    unittest.main()
