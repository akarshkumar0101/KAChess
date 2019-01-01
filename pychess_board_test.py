import unittest
from pychess_board import pychess_board
from numpy.f2py.auxfuncs import throw_error


class pychess_board_test(unittest.TestCase):
    
    """                                                                """
    """                                                                """
    """                    starting position tests                      """
    """                                                                """
    """                                                                """
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
    
    
    
    """                                                                """
    """                                                                """
    """                            game tests                          """
    """                                                                """
    """                                                                """
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
        tester = self.erase_square(3,5, tester) # fill 3,5, with empty square
        self.assertBoardsEqual(cb, tester)
    
    # moves piece on for easy testing
    
    
    def test_simple_game_3(self):
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

        cb, tester = self.Test_move(cb, tester, "a1,b1")
        cb, tester = self.Test_move(cb, tester, "h1,h2")
        cb, tester = self.Test_move(cb, tester, "f1,g2")
        cb, tester = self.Test_move(cb, tester, "h2,g2")
        cb, tester = self.Test_move(cb, tester, "c2,c3")
        cb, tester = self.Test_move(cb, tester, "c5,e3")
        
        
    def test_simple_game_4(self):
        cb = pychess_board()
        tester = pychess_board()
        
        cb, tester = self.Test_move(cb, tester, "c2,c4")
    
    
    
    
    """                                                                """
    """                                                                """
    """                        king safety tests                       """
    """                                                                """
    """                                                                """
    def test_king_safety_1(self):
        """
             ________________________________________________
            |     |     |     |     |     |     |     |     |
            |     |     | -2  |     | -2  |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            | -2  |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |  6  |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            | -2  |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|

        """
        
        board_setup = [[0,0,-2,0,-2,0,0,0],[0,0,0,0,0,0,0,0],[-2,0,0,0,0,0,0,0],[0,0,0,6,0,0,0,0],[-2,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        cb = pychess_board(board_setup)
        tester = pychess_board(board_setup)

        for i in range(8):
            for j in range(8):
                self.Test_false_move(cb, tester, self.new_move(3,3,i,j))
        
    
    def test_king_safety_2(self):
        """
             ________________________________________________
            |     |     |     |     |     |     |     |     |
            |     |     |     |     |     | -5  |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            | -2  |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |  6  |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            | -2  |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|
            |     |     |     |     |     |     |     |     |
            |     |     |     |     |     |     |     |     |
            |_____|_____|_____|_____|_____|_____|_____|_____|

        """
        
        board_setup = [[0,0,0,0,0,-5,0,0],[0,0,0,0,0,0,0,0],[-2,0,0,0,0,0,0,0],[0,0,0,6,0,0,0,0],[-2,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        cb = pychess_board(board_setup)
        tester = pychess_board(board_setup)

        for i in range(8):
            for j in range(8):
                if(i != 3 or j != 4):
                    self.Test_false_move(cb, tester, self.new_move(3,3,i,j))
        cb, tester = self.Test_move(cb, tester, self.new_move(3,3,3,4))
        cb, tester = self.Test_move(cb, tester, self.new_move(4,0,4,1)) # so correct turn
        
        for i in range(8):
            for j in range(8):
                if(i != 3 or j != 3):
                    self.Test_false_move(cb, tester, self.new_move(3,4,i,j))
                
        
        cb, tester = self.Test_move(cb, tester, self.new_move(3,4,3,3))
        
        
    def test_king_safety_3(self):
        pass
    
    
    def test_king_safety_4(self):
        pass
    
    
    def test_king_safety_5(self):
        pass
    
    
    
    
    
    """                                                                """
    """                                                                """
    """                                                                """
    """                         helper methods                         """
    """                                                                """
    """                                                                """
    """                                                                """
    """                                                                """
    
    def erase_square(self, row, col, cboard):
        cboard.board[row][col] = 0
        return cboard
    
    
    def move_no_check(self, startRow, startCol, endRow, endCol, b):
        output = b.get_board()
        piece = output[startRow][startCol]
        if(piece == 0):
            print("cannot move empty square: row " + str(startRow) + ", col "+str(startCol) )
            print(b.to_string())
            raise ArgumentError
        output[startRow][startCol] = 0
        output[endRow][endCol] = piece
        return pychess_board(output, not b.white_to_move)
    
    
    def assertBoardsEqual(self, a, b):
        # given: board dimensions are equal
        # test whether boards are equal
        boardA = a.get_board()
        boardB = b.get_board()
        
        for i in range(len(boardA)):
            for j in range(len(boardA[0])):
                try:
                    self.assertEqual(boardA[i][j], boardB[i][j])
                except:
                    print("Assertion error at row " + str(i)+", column "+str(j)+":")
                    print("chessboard:")
                    print(a.to_string())
                    print("tester board:")
                    print(b.to_string())
                    raise AssertionError
                    
    
    def new_move(self, startRow, startCol, endRow, endCol):
        output = []
        output.append(startRow)
        output.append(startCol)
        output.append(endRow)
        output.append(endCol)
        return output
    
    
    def Test_move(self, chess_board, tester_board, move): # startsqr, comma, endsqr ex: d2,d4
        
        startRow, startCol, endRow, endCol = self.parse(move)
        
        piece = chess_board.board[startRow][startCol]
        
        # before the move
        if(piece > 0):
            self.move_black(chess_board, tester_board)
        elif(piece < 0):
            self.move_white(chess_board, tester_board)
        
        # move the piece
        # move is changing tester_board too
        chess_board.move(self.new_move(startRow,startCol,endRow,endCol))
        tester_board = self.move_no_check(startRow,startCol,endRow,endCol, tester_board)
        self.assertBoardsEqual(chess_board, tester_board)
        
        return chess_board, tester_board
     
     
    def Test_false_move(self, chess_board, tester_board, move):
        # move the piece
        startRow,startCol,endRow,endCol = self.parse(move)
        chess_board.move(self.new_move(startRow,startCol,endRow,endCol))
        self.assertBoardsEqual(chess_board, tester_board)
        
     
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
        if(isinstance(move, list)): # move is a list
            startRow = move[0]
            startCol = move[1]
            endRow   = move[2]
            endCol   = move[3] 
        elif(isinstance(move, str)): # move is a string
            # can't be used for compound moves
            squares = move.split(",")
            
            startRow = self.num_to_square(squares[0][1])
            startCol = self.letter_to_square(squares[0][0])
            endRow = self.num_to_square(squares[1][1])
            endCol = self.letter_to_square(squares[1][0])
        
        return startRow, startCol, endRow, endCol
    
    
    def move_white(self, cb, tester): # try to move every piece of white (doesn't move)
        for startRow in range(8):
            for startCol in range(8):
                if(tester.board[startRow][startCol] > 0):
                    for endRow in range(8):
                        for endCol in range(8):
                            cb.move(self.new_move(startRow,startCol,endRow,endCol))
                            self.assertBoardsEqual(cb, tester)
    
    
    def move_black(self, cb, tester): # try to move every piece of black (doesn't move)
        for startRow in range(8):
            for startCol in range(8):
                if(tester.board[startRow][startCol] < 0):
                    for endRow in range(8):
                        for endCol in range(8):
                            cb.move(self.new_move(startRow,startCol,endRow,endCol))
                            self.assertBoardsEqual(cb, tester)