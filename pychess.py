from pychess_engine import pychess_engine
import datetime
from move_object import move_object
#from pychess_robot import pychess_robot



""" This module makes and executes decisions for the robot using pychess_engine and pychess_robot modules """

""" IDEAS:
    
    how do we evaluate chessboards?
    
    pieces that are in danger 
    (piece that is attacked more than defended or are higher in value than the piece attacking)
    
    how many squares a piece controls
    
    how much freedom a piece has to move
    
    the number of opponent moves
    
    
    """
    

def main():
    #robot = pychess_robot()
    
    start = datetime.datetime.now()
    engine = pychess_engine(2) # up to 5 min for depth 3, about 8 seconds for depth 2
    print("time to setup engine " + str(datetime.datetime.now() - start))
    
    while True:
        
        a_move = input("enter move: ").split(",")
        
        try:
            start = datetime.datetime.now()
            if(len(a_move) == 4):
                engine.play(move_object(int(a_move[0]), int(a_move[1]), int(a_move[2]), int(a_move[3])))
            if(len(a_move) == 5):
                engine.play(move_object(int(a_move[0]), int(a_move[1]), int(a_move[2]), int(a_move[3]), int(a_move[4])))
            print("time to move " + str(datetime.datetime.now() - start))
        except:
            pass
        
if __name__ == "__main__":
    main()