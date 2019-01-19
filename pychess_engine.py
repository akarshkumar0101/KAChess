from pychess_board import pychess_board
import math
import numpy
from gametree_node import gametree_node
import datetime
from move_object import move_object

class pychess_engine:
    """ This class provides an interface to play, uses the gametree module to pick best move """
    
    """ NOTES:
        all engine parameters and strategy is stored in gametree module
        make gametree reusable
        don't check all the children nodes (use alpha-beta pruning)
    """
    
    
    
    """                                               """
    """                                               """
    """                  CONSTRUCTOR                  """
    """                                               """
    """                                               """
    
   
    def __init__(self, dpth = 2, board_setup = None, white_to_move = True, user_plays_white = True):
          
        if(user_plays_white):
            self.sign = -1
        else:
            self.sign = 1
        
        self.depth = dpth
        
        self.chessboard = pychess_board(board_setup, white_to_move)
        
        self.root = gametree_node(None)
        
        print("   eval,  search,    move,     time") # for development
        best_node, self.evaluation = self.root.get_evaluation(self.chessboard, 2)
        
        
        print(self.to_string())
        
        if(not self.__player_to_move()): # if engine's turn
            self.__make_engine_move(self.depth)
            print(self.to_string())
        
    """                                               """
    """                                               """
    """                PUBLIC METHODS                 """
    """                                               """
    """                                               """
    
    def play(self, player_move):
        """ accepts a move, makes the best move on the board, returns the move if completed (else None) """
        
        if(not self.__make_player_move(player_move)):
            print("not a legal move.")
            return None
        else:
            print(self.to_string()) # development
            best_move = self.__make_engine_move() # depends on self.depth
            print(self.to_string()) # development
            
            return best_move
    
   
    def to_string(self):
        if(self.chessboard.whiteToMove):
            to_move = "white"
        else:
            to_move = "black"
        
        eval = math.floor(100 * (self.evaluation + .5))/100 # this is updated in make engine move
        
        if(eval >= 0):
            eval = " " + str(eval)
        else:
            eval = str(eval)
            
        return "\n\n" + self.chessboard.to_string() + "\n    " \
                + eval + "                             " + to_move \
                + "\n\n" + self.chessboard.game_complete_message 
    
    
    def offer_draw(self):
        self.chessboard.offer_draw(self.__player_to_move())
        
        
    def accept_draw(self):
        self.chessboard.accept_draw(self.__player_to_move())
        
        
    def resign(self):
        self.chessboard.resign(self.__player_to_move())
     
       
    def change_depth(self, depth):
        self.depth = depth
     
     
     
      
    """                                               """
    """                                               """
    """                PRIVATE METHODS                """
    """                                               """
    """                                               """

    def __make_player_move(self, player_move):
        """ tries to make the specified player_move on the board, returns True if complete """
        
        if(not self.__player_to_move() or not isinstance(player_move, move_object)):
            return False

         # if piece moved belongs to player
        if(self.chessboard.board[player_move.start_row][player_move.start_col] * self.sign < 0):
            # try to make move on chessboard, return boolean if completed
            return self.__make_move(player_move)
        else:
            return False
    
    def __make_engine_move(self):
        """ thinks about the best move, makes it on the board """
        
        assert(not self.__player_to_move())
        
        print("   eval,  search,    move,     time") # development
        best_node, self.evaluation = self.root.get_evaluation(self.chessboard, self.depth)
        
        # update gametree root of engine according to move
        assert(self.chessboard.move(best_node.move))
        self.root = best_node
        assert(self.__player_to_move())
        
        return best_node.move 
    
    def __make_move(self, a_move):
        """ makes a move on the engine's gametree, returns true if completed """ 
        if(self.chessboard.move(a_move)): # update chessboard of engine
            if(self.root.children == None):
                self.root.children = self.root.get_children(self.chessboard)
            
            for child in self.root.children:
                if(self.__moves_are_equal(child.move, a_move)):
                    self.root = child
                    return True
        # print("False"+self.chessboard.to_string()+" "+a_move.to_string()) for development
        return False
    
    def __player_to_move(self):
        """ this method returns true if it is the player's move (not the engine's move) """
        
        return (self.chessboard.whiteToMove == (self.sign < 0))
    
    def __moves_are_equal(self, move1, move2):
        
        if(move1.start_row == move2.start_row and move1.start_col == move2.start_col and move1.end_row == move2.end_row and move1.end_col == move2.end_col and move1.promotion == move2.promotion):
            return True
                
        return False      