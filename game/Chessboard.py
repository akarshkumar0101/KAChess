'''
Created on Dec 18, 2018

@author: akarshkumar0101
'''
class Chessboard:
	EMPTY = 0;
	
	WHITE = 1;
	BLACK = -1;
	
	PAWN = 1;
	ROOK = 2;
	KNIGHT = 3;
	BISHOP = 4;
	QUEEN = 5;
	KING = 6;
	
	def __init__(self):
		self.board = list([2,3,3,2]);
		
	
	def printBoard(self):
		print(self.board.copy());
	