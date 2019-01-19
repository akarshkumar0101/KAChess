from pychess_board import pychess_board
from move_object import move_object

board = pychess_board()
print(board.to_string())
board.move(move_object(6,4,4,4))
print(board.to_string())
board.move(move_object(0,1,2,0))
print(board.to_string())
board.move(move_object(6,2,5,2))
print(board.to_string())
print(board.move(move_object(0,3,0,1)))
print(board.to_string())