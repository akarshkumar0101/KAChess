class move:
    
    def __init__(self, sr, sc, er, ec, prmt=None):
        self.start_row = sr
        self.start_col = sc
        self.end_row = er
        self.end_col = ec
        self.promotion = prmt