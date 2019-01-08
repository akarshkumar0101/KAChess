from pychess_engine import pychess_engine
#from pychess_robot import pychess_robot



""" This module makes and executes decisions for the robot using pychess_engine and pychess_robot modules """

engine = pychess_engine()

def start_new_game():
    pass

def do(a,b,c,d): # start and end squares
    move = [a,b,c,d]
    assert(engine.move(move))
    print(engine.to_string())
    assert(engine.play())
    print(engine.to_string())

def main():
    #robot = pychess_robot()
    #start_new_game()
    
    print(engine.to_string())
    do(6,4,4,4)
    do(6,3,4,3)
    do(6,2,5,2)
    do(5,2,4,3)
    
   

if __name__ == "__main__":
    main()