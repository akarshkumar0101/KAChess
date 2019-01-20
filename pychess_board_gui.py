import numpy as np
import cv2






def showBoard(board):
    PIECE_IMG_WIDTH = 50;
    PIECE_IMG_HEIGHT = 50;

    height = PIECE_IMG_HEIGHT*8;
    width = PIECE_IMG_WIDTH*8;
    img = np.zeros((height, width,4), np.uint8);
    img[:,:,:] = 255;

    for x in range(0,8):
        for y in range(0,8):
            pixx = x*PIECE_IMG_WIDTH;
            pixy = y*PIECE_IMG_HEIGHT;
            piece = board[x][y];

            piecestr="";

            if np.abs(piece) == 1:
                piecestr = "Pawn";
            if np.abs(piece) == 2:
                piecestr = "Rook";
            if np.abs(piece) == 3:
                piecestr = "Knight";
            if np.abs(piece) == 4:
                piecestr = "Bishop";
            if np.abs(piece) == 5:
                piecestr = "Queen";
            if np.abs(piece) == 6:
                piecestr = "King";

            if piece>0:
                piecestr+="true";
            if piece<0:
                piecestr+="false";

            pieceimg = cv2.imread("resources/images/"+piecestr+".png", cv2.IMREAD_UNCHANGED);
            rawpimg = np.zeros((PIECE_IMG_HEIGHT,PIECE_IMG_WIDTH,4),np.uint8);
            rawpimg[:, :, :] = 128;
            if (x+y)%2==0:
                rawpimg[:,:,:]=255;
            if pieceimg is not None:
                pieceimg = cv2.resize(pieceimg, (PIECE_IMG_HEIGHT, PIECE_IMG_WIDTH));
                mask = pieceimg[..., 3] > 0
                #print(mask);
                rawpimg[mask] = pieceimg[mask];
            img[pixx:pixx + PIECE_IMG_WIDTH, pixy:pixy + PIECE_IMG_HEIGHT] = rawpimg[:, :];



    cv2.imshow("chess", img);


    cv2.waitKey(1);
    return;