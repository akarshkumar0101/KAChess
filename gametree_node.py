
class gametree_node:
    
    def __init__(self, chessboard, evaluation):
        self.board = chessboard
        self.board_eval = self.evaluate_board(chessboard)
        self.children = []
        self.parent = None
        
    def evaluate_board(self):
        pass