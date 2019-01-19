class move_object:
    
    def __init__(self, sr, sc, er, ec, prmt=None):
        self.start_row = sr
        self.start_col = sc
        self.end_row = er
        self.end_col = ec
        self.promotion = prmt
        
    def to_string(self, with_promo=False):
        move_string = str(self.start_row)+","+str(self.start_col)+", "+str(self.end_row)+","+str(self.end_col)
        
        if(with_promo):
            move_string += ", "+str(self.promotion)
        
        return move_string