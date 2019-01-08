from pychess_board import pychess_board
import math
from gametree import gametree

class pychess_engine:
    """ This class provides an interface to play, uses the gametree module to pick best move """
    
    """                                               """
    """                                               """
    """                  CONSTRUCTOR                  """
    """                                               """
    """                                               """
    
   
    def __init__(self, board_setup = None, white_to_move = True, user_plays_white = True):

        self.chessboard = pychess_board(board_setup, white_to_move)
        
        self.gametree = gametree(self.chessboard)
        
        if(user_plays_white):
            self.sign = -1
        else:
            self.sign = 1
         
        
        
    """                                               """
    """                                               """
    """                PUBLIC METHODS                 """
    """                                               """
    """                                               """
    
    def play(self): #, max_depth=10):
        """ makes the best move on the board, returns the move if completed """
        
        if(self.__player_to_move()):
            return
        
        engine_move = self.gametree.get_best_move() # max_depth)
        self.chessboard.move(engine_move)
            
        return engine_move
        
        
    def move(self, move): 
        """ move is list of form [startRow, startCol, endRow, endCol], returns true if move is completed """

        assert(len(move) == 4)
        
        startRow = move[0]
        startCol = move[1]
        
         # if piece moved belongs to player
        if(self.chessboard.get_board()[startRow][startCol] * self.sign < 0):
            # try to make move on chessboard, return boolean if completed
            return self.chessboard.move(move)
            
        return False
    
    
    def to_string(self):
        if(self.chessboard.whiteToMove):
            to_move = "white"
        else:
            to_move = "black"
        
        eval = math.floor(10 * self.gametree.get_eval(self.chessboard) + .5)/10
        
        if(eval >= 0):
            eval = " " + str(eval)
        else:
            eval = str(eval)
        
        return "\n\n" + self.chessboard.to_string() + "\n    " \
                + eval + "                              " + to_move + "\n\n"
    
    
    def offer_draw(self):
        self.chessboard.offer_draw(self.__player_to_move())
        
        
    def accept_draw(self):
        self.chessboard.accept_draw(self.__player_to_move())
        
        
    def resign(self):
        self.chessboard.resign(self.__player_to_move())
       
       
       
       
    """                                               """
    """                                               """
    """                PRIVATE METHODS                """
    """                                               """
    """                                               """

    
    def __player_to_move(self):
        return (self.chessboard.white_to_move() and (self.sign < 0)) or (not self.chessboard.white_to_move() and (self.sign > 0))
