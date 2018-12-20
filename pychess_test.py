import unittest
from pychess_board import pychess_board


class pychess_board_test(unittest.TestCase):

    def test_rook_movement_in_starting_position(self):
        cb = pychess_board()
        
        # top right rook
        for i in range(8):
            for j in range(8):
                cb.move(self.new_move(0, 7, i, j))
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(self.new_move(0, 0, i, j))
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(self.new_move(7, 0, i, j))
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(self.new_move(7, 7, i, j))
                self.assertBoardsEqual(cb, pychess_board())
        
    
    def test_bishop_movement_in_starting_position(self):
        cb = pychess_board()
        
        # bottom left bishop
        for i in range(8):
            for j in range(8):
                cb.move(self.new_move(7, 2, i, j))
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(self.new_move(0, 2, i, j))
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(self.new_move(0, 5, i, j))
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(self.new_move(7, 5, i, j))
                self.assertBoardsEqual(cb, pychess_board())

    
    def test_king_movement_in_starting_position(self):
        cb = pychess_board()

        for i in range(8):
            for j in range(8):
                cb.move(self.new_move(7, 4, i, j))
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(self.new_move(0, 4, i, j))
                self.assertBoardsEqual(cb, pychess_board())
        
    
    def test_queen_movement_in_starting_position(self):
        cb = pychess_board()
        
        # black queen
        for i in range(8):
            for j in range(8):
                cb.move(self.new_move(0, 3, i, j))
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(self.new_move(7, 3, i, j))
                self.assertBoardsEqual(cb, pychess_board())
            
    
    def test_pawn_movement_in_starting_position(self):
        
        cb = pychess_board()

        # test all black pawns to make sure they don't move (bc not their turn)
        pawnRow = 2 
        for pawnCol in range(8):
            for i in range(8):
                for j in range(8):
                    cb.move(self.new_move(pawnRow, pawnCol, i, j))
                    self.assertBoardsEqual(cb, pychess_board())
        
        pawnRow = 6 
        for pawnCol in range(8):
            for toRow in range(8):
                for toCol in range(8):
                    cb.move(self.new_move(pawnRow, pawnCol, toRow, toCol))
                    
                    if((toRow == 5 or toRow == 4) and pawnCol - toCol == 0):
                        self.assertBoardsEqual(cb, self.move_no_check(pawnRow, pawnCol, toRow, toCol, pychess_board()))
                        cb = pychess_board()
                    else:
                        self.assertBoardsEqual(cb, pychess_board())
                    
    
    def test_knight_movement_in_starting_position(self):
        
        cb = pychess_board()
        
        # black knights not supposed to move on first turn
        for i in range(8):
            for j in range(8):
                cb.move(self.new_move(0, 1, i, j))
                self.assertBoardsEqual(cb, pychess_board())
                cb.move(self.new_move(0, 6, i, j))
                self.assertBoardsEqual(cb, pychess_board())
        
        # white knights
        for i in range(8):
            for j in range(8):
                
                cb.move(self.new_move(7, 1, i, j))
                if((i == 5 and j == 0) or(i == 5 and j == 2)):
                    self.assertBoardsEqual(cb, self.move_no_check(7, 1, i, j, pychess_board()))
                    cb = pychess_board()
                else:
                    self.assertBoardsEqual(cb, pychess_board())
                
                cb.move(self.new_move(7, 6, i, j))
                if((i == 5 and j == 5) or (i == 5 and j == 7)):
                    self.assertBoardsEqual(cb, self.move_no_check(7, 6, i, j, pychess_board()))
                    cb = pychess_board()
                else:
                    self.assertBoardsEqual(cb, pychess_board())
            
    
    # TODO write tests when king is in check
    
    # TODO write test for castling 
    
    # FIXME write tests for en passant
    
    # TODO write tests for king moving into check
    
    # FIXME write tests for checkmate
    
    # TODO write more complicated tests
    
    # TODO test get moves
    
    # FIXME make sure follows real game moves
    
    def test_simple_game_1(self):
        cb = pychess_board()
        tester = pychess_board()
        
        cb.move(self.new_move(6, 4, 4 ,4))
        tester = self.move_no_check(6, 4, 4, 4, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(self.new_move(1, 4, 3 ,4))
        tester = self.move_no_check(1, 4, 3 ,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(self.new_move(7, 6, 5 ,5))
        tester = self.move_no_check(7, 6, 5 ,5, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(self.new_move(1, 1, 3, 1))
        tester = self.move_no_check(1, 1, 3, 1, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(self.new_move(5, 5, 4 ,3))
        tester = self.move_no_check(5, 5, 4 ,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        cb.move(self.new_move(3, 4, 4, 3))
        tester = self.move_no_check(3, 4, 4, 3, tester)
        self.assertBoardsEqual(cb, tester)
    
    def test_simple_game_2(self):
        cb = pychess_board()
        tester = pychess_board()
        
        # uses en passant
        
        # e4
        cb.move(self.new_move(6, 4, 4 ,4))
        tester = self.move_no_check(6, 4, 4, 4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # e5
        cb.move(self.new_move(1, 4, 3 ,4))
        tester = self.move_no_check(1, 4, 3 ,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nf3
        cb.move(self.new_move(7, 6, 5 ,5))
        tester = self.move_no_check(7, 6, 5 ,5, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nc6
        cb.move(self.new_move(0, 1, 2, 2))
        tester = self.move_no_check(0, 1, 2, 2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # d4
        cb.move(self.new_move(6, 3, 4 ,3))
        tester = self.move_no_check(6, 3, 4 ,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # exd4
        cb.move(self.new_move(3, 4, 4, 3))
        tester = self.move_no_check(3, 4, 4, 3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nxd4
        cb.move(self.new_move(5 ,5, 4, 3))
        tester = self.move_no_check(5 ,5, 4, 3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nf6
        cb.move(self.new_move(0, 6, 2, 5))
        tester = self.move_no_check(0, 6, 2, 5, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nxc6
        cb.move(self.new_move(4, 3, 2, 2))
        tester = self.move_no_check(4, 3, 2, 2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # bxc6
        cb.move(self.new_move(1,1,2,2))
        tester = self.move_no_check(1,1,2,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # e5
        cb.move(self.new_move(4,4,3,4))
        tester = self.move_no_check(4,4,3,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe7
        cb.move(self.new_move(0,3,1,4))
        tester = self.move_no_check(0,3,1,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe2
        cb.move(self.new_move(7,3,6,4))
        tester = self.move_no_check(7,3,6,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nd5
        cb.move(self.new_move(2,5,3,3))
        tester = self.move_no_check(2,5,3,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # c4
        cb.move(self.new_move(6,2,4,2))
        tester = self.move_no_check(6,2,4,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nb6
        cb.move(self.new_move(3,3,2,1))
        tester = self.move_no_check(3,3,2,1, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Nc3
        cb.move(self.new_move(7,1,5,2))
        tester = self.move_no_check(7,1,5,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe6
        cb.move(self.new_move(1,4,2,4))
        tester = self.move_no_check(1,4,2,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe4
        cb.move(self.new_move(6,4,4,4))
        tester = self.move_no_check(6,4,4,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bb4
        cb.move(self.new_move(0,5,4,1))
        tester = self.move_no_check(0,5,4,1, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bd2
        cb.move(self.new_move(7,2,6,3))
        tester = self.move_no_check(7,2,6,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bb7
        cb.move(self.new_move(0,2,1,1))
        tester = self.move_no_check(0,2,1,1, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bd3
        cb.move(self.new_move(7,5,5,3))
        tester = self.move_no_check(7,5,5,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # 0-0-0
        cb.move(self.new_move(0,4,0,2))
        tester = self.move_no_check(0,4,0,2, tester)
        tester = self.move_no_check(0,0,0,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # 0-0-0
        cb.move(self.new_move(7,4,7,2))
        tester = self.move_no_check(7,4,7,2, tester)
        tester = self.move_no_check(7,0,7,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # c5
        cb.move(self.new_move(2,2,3,2))
        tester = self.move_no_check(2,2,3,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Qe2
        cb.move(self.new_move(4,4,6,4))
        tester = self.move_no_check(4,4,6,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Re8
        cb.move(self.new_move(0,7,0,4))
        tester = self.move_no_check(0,7,0,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # f4
        cb.move(self.new_move(6,5,4,5))
        tester = self.move_no_check(6,5,4,5, tester)
        self.assertBoardsEqual(cb, tester)
        
        # d6
        cb.move(self.new_move(1,3,2,3))
        tester = self.move_no_check(1,3,2,3, tester)
        self.assertBoardsEqual(cb, tester)
        
        # a3
        cb.move(self.new_move(6,0,5,0))
        tester = self.move_no_check(6,0,5,0, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bxc3
        cb.move(self.new_move(4,1,5,2))
        tester = self.move_no_check(4,1,5,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Bxc3
        cb.move(self.new_move(6,3,5,2))
        tester = self.move_no_check(6,3,5,2, tester)
        self.assertBoardsEqual(cb, tester)
        
        # g6
        cb.move(self.new_move(1,6,2,6))
        tester = self.move_no_check(1,6,2,6, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Rhf1
        cb.move(self.new_move(7,7,7,5))
        tester = self.move_no_check(7,7,7,5, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Na4
        cb.move(self.new_move(2,1,4,0))
        tester = self.move_no_check(2,1,4,0, tester)
        self.assertBoardsEqual(cb, tester)
        
        # Ba5
        cb.move(self.new_move(5,2,3,0))
        tester = self.move_no_check(5,2,3,0, tester)
        self.assertBoardsEqual(cb, tester)
        
        # dxe5
        cb.move(self.new_move(2,3,3,4))
        tester = self.move_no_check(2,3,3,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # fxe5
        cb.move(self.new_move(4,5,3,4))
        tester = self.move_no_check(4,5,3,4, tester)
        self.assertBoardsEqual(cb, tester)
        
        # f5
        cb.move(self.new_move(1,5,3,5))
        tester = self.move_no_check(1,5,3,5, tester)
        self.assertBoardsEqual(cb, tester)

        # exf6!
        cb.move(self.new_move(3,4,2,5))
        tester = self.move_no_check(3,4,2,5, tester)
        tester = self.move_no_check(3,4,3,5, tester) # fill 3,5, with empty square
        self.assertBoardsEqual(cb, tester)
    
    # moves piece on for easy testing
    
    def test_simple_game_3(self):
        pass # TODO implement
    
    
    """                         helper methods                         """
    def move_no_check(self, startRow, startCol, endRow, endCol, b):
        output = b.get_board()
        piece = output[startRow][startCol]
        output[startRow][startCol] = 0
        output[endRow][endCol] = piece
        return pychess_board(output, True)
    
    def assertBoardsEqual(self, a, b):
        # given: board dimensions are equal
        # test whether boards are equal
        boardA = a.get_board()
        boardB = b.get_board()
        
        for i in range(len(boardA)):
            for j in range(len(boardA[0])):
                self.assertEqual(boardA[i][j], boardB[i][j])
    
    def new_move(self, startRow, startCol, endRow, endCol):
        output = []
        output.append(startRow)
        output.append(startCol)
        output.append(endRow)
        output.append(endCol)
        return output