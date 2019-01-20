import cv2;
import numpy as np;
import time;


class pychess_vision:
    """ This class controls the robot's vision through a specified camera """

    PIECE_CODES = [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]];
    PIECE_STRINGS = ["P", "R", "H", "B", "Q", "K"];

    def __init__(self):
        pass;

    def setImage(self, newImage):
        self.image = newImage;

    def attemptFindChessboard(self, searchScale=0.25):
        iscale = 1 / searchScale;

        smallimage = cv2.resize(self.image, (0, 0), fx=searchScale, fy=searchScale);
        graysmallimg = cv2.cvtColor(smallimage, cv2.COLOR_BGR2GRAY);

        self.foundChessboard, self.rawCorners = cv2.findChessboardCorners(graysmallimg, (7, 7));

        if not self.foundChessboard:
            return False;
        self.rawCorners = np.float32(self.rawCorners * iscale);
        return self.foundChessboard;

    def establishCornerPoints(self):
        if self.foundChessboard:
            self.cornerPoints = pychess_vision.getChessboardCorners(self.rawCorners);
        return;

    def establishSquareImages(self, squareImageSize=300):

        # replicatedImage = self.image * 1;
        # replicatedImage[:, :, :] = 0;

        self.squareImages = np.zeros((8, 8), dtype=np.ndarray);

        for cx in range(0, 8):
            for cy in range(0, 8):
                Mtrans, iMtrans = pychess_vision.getMatrixTransform(self.cornerPoints, (cx, cy), squareImageSize);
                squareImage = cv2.warpPerspective(self.image, Mtrans, (squareImageSize, squareImageSize));

                self.squareImages[cx, cy] = squareImage;

                # replicated image CODE:

                # height, width = self.image.shape[:2];
                # transformedSquareImage = cv2.warpPerspective(self.squareImages[cx, cy], iMtrans, (width, height));
                # mask = transformedSquareImage[:, :, :] != 0;
                # replicatedImage[mask] = transformedSquareImage[mask];
        # cv2.imshow("replicatedimage", replicatedImage);
        return;

    def identifiyAllPieces(self):
        self.board = np.zeros((8, 8));
        for cx in range(0, 8):
            for cy in range(0, 8):
                piece = pychess_vision.identifyPiece(self.squareImages[cx, cy]);
                #cv2.imshow(str(cx)+", "+str(cy), self.squareImages[cx, cy]);
                self.board[cx][cy] = piece;
        return;

    def drawAllPieceNames(self):
        for cx in range(0, 8):
            for cy in range(0, 8):

                font = cv2.FONT_HERSHEY_SIMPLEX;
                centerx = np.average(self.cornerPoints[cx, cy, :, 0]);
                centery = np.average(self.cornerPoints[cx, cy, :, 1]);
                bottomLeftCornerOfText = (centerx, centery);
                fontColor = (0, 0, 255);
                lineType = cv2.LINE_AA;  # 2;

                piecestr = "";
                if (self.board[cx][cy] > 0):
                    piecestr = pychess_vision.PIECE_STRINGS[int(self.board[cx][cy] - 1)];

                cv2.putText(self.image, piecestr, bottomLeftCornerOfText, font, .5, fontColor, 1, cv2.LINE_AA);

    def paintChessboard(self):

        pychess_vision.paintFirstSquare(self.image, self.cornerPoints, (0, 255, 0));
        pychess_vision.paintSquareCorners(self.image, self.cornerPoints, (0, 0, 0));

        return;

    COLOR_BLUE = np.array((255, 0, 0));
    COLOR_GREEN = np.array((0, 255, 0));
    COLOR_RED = np.array((0, 0, 255));

    def colorDiff(col1, col2):
        bluediff = np.abs(col2[0] - col1[0]);
        greendiff = np.abs(col2[1] - col1[1]);
        reddiff = np.abs(col2[2] - col1[2]);
        return bluediff + greendiff + reddiff;

    CUTOFF = 50;

    def isSameColor(colDiff):
        if (colDiff < pychess_vision.CUTOFF):
            return True;
        else:
            return False;

    SOFTMULTIPLIER = 1.2;
    HARDMULTIPLIER = 1.5;



    def isGrayscale(pix):
        pix = np.array(pix);
        if (np.std(pix) < 10):
            return True;

    def paintFirstSquare(image, points, color):
        centerx = np.average(points[0, 0, :, 0]);
        centery = np.average(points[0, 0, :, 1]);

        cv2.circle(image, (centerx, centery), 5, color, -1);

        return;

    def paintSquareCorners(image, points, color):
        for rx in range(0, 8):
            for ry in range(0, 8):
                for point in points[rx][ry]:
                    x = point[0];
                    y = point[1];
                    cv2.circle(image, (x, y), 5, color, -1);
        return;

    def getMatrixTransform(cornerPoints, coord, squareImageSize):
        pointsfrom = cornerPoints[coord[0]][coord[1]];
        pointsto = np.float32([[0, 0], [squareImageSize, 0], [0, squareImageSize], [squareImageSize, squareImageSize]]);

        Mtrans = cv2.getPerspectiveTransform(pointsfrom, pointsto);
        iMtrans = cv2.getPerspectiveTransform(pointsto, pointsfrom);
        return (Mtrans, iMtrans);

    def identifyPieceColor(squareImage):
        return 1;


    def isColor(pix, colorID):
        if (pychess_vision.isGrayscale(pix)):
            return False;
        MULTIPLIER = pychess_vision.SOFTMULTIPLIER;
        if (colorID == 2):
            MULTIPLIER = pychess_vision.HARDMULTIPLIER;
        if (np.max(pix) == pix[colorID]):
            sum = np.sum(pix);
            sum -= pix[colorID];
            average = sum / 2;
            if (pix[colorID] > MULTIPLIER * average):
                return True;
        return False;

    def getColor(pix):
        colorID = np.argmax(pix);
        avg = np.average(pix);
        std = np.std(pix);
        offset = 10;
        if(colorID ==2):
            offset = 35;
        if(std >offset and pix[colorID]>avg+std):
            return colorID;
        else:
            return -1;

    def identifyPiece(squareImage):
        colorcode = [];
        height, width = squareImage.shape[:2];
        maxi = int(np.min((height,width))/2);
        for i in range(0, maxi, int(maxi/15)):
            pix = squareImage[i,i];
            color = pychess_vision.getColor(pix);
            if (color not in colorcode and color > -1):
                colorcode.append(color);
            squareImage[i+1][i] = (i,i,i);

        colorcode.reverse();

        if (colorcode not in pychess_vision.PIECE_CODES):
            return 0;
        return pychess_vision.PIECE_CODES.index(colorcode) + 1;

    # pointnumber 0 is top left, 1 is top right, 2 is bot left, 3 is bot right;
    # will return a 4d array which is points[chessboardx][chessboardy][pointnumber][x=0/y=1];
    def getChessboardCorners(corners):
        points = np.zeros((8, 8, 4, 2), dtype=np.float32);
        for cy in range(1, 7):
            for cx in range(1, 7):
                points[cx][cy][0] = corners[7 * (cy - 1) + (cx - 1)][0];
                points[cx][cy][1] = corners[7 * (cy - 1) + (cx - 1 + 1)][0];
                points[cx][cy][2] = corners[7 * (cy - 1 + 1) + (cx - 1)][0];
                points[cx][cy][3] = corners[7 * (cy - 1 + 1) + (cx - 1 + 1)][0];

        for cy in range(1, 8):

            offset = np.zeros(2, dtype=np.float32);
            for cx in range(1, 7):
                pt1 = corners[7 * (cy - 1) + (cx - 1)][0];
                pt2 = corners[7 * (cy - 1) + (cx - 1 + 1)][0];
                offset += (pt2 - pt1);
            offset /= 6;

            lpt = corners[7 * (cy - 1) + (1 - 1)][0] - offset;
            rpt = corners[7 * (cy - 1) + (7 - 1)][0] + offset;

            # left of 0
            points[0][cy][0] = lpt;
            # right of 7
            points[7][cy][1] = rpt;
            # right of 0
            points[0][cy][1] = corners[7 * (cy - 1) + (1 - 1)][0];
            # left of 7
            points[7][cy][0] = corners[7 * (cy - 1) + (7 - 1)][0];
            # upper side
            # left of 0
            points[0][cy - 1][2] = lpt;
            # right of 7
            points[7][cy - 1][3] = rpt;
            # right of 0
            points[0][cy - 1][3] = corners[7 * (cy - 1) + (1 - 1)][0];
            # left of 7
            points[7][cy - 1][2] = corners[7 * (cy - 1) + (7 - 1)][0];

        for cx in range(1, 8):

            offset = np.zeros(2, dtype=np.float32);
            for cy in range(1, 7):
                pt1 = corners[7 * (cy - 1) + (cx - 1)][0];
                pt2 = corners[7 * (cy - 1 + 1) + (cx - 1)][0];
                offset += (pt2 - pt1);
            offset /= 6;

            upt = corners[7 * (1 - 1) + (cx - 1)][0] - offset;
            dpt = corners[7 * (7 - 1) + (cx - 1)][0] + offset;

            # up of 0
            points[cx][0][0] = upt;
            # down of 7
            points[cx][7][2] = dpt;
            # down of 0
            points[cx][0][2] = corners[7 * (1 - 1) + (cx - 1)][0];
            # up of 7
            points[cx][7][0] = corners[7 * (7 - 1) + (cx - 1)][0];
            # lefter side
            # up of 0
            points[cx - 1][0][1] = upt;
            # down of 7
            points[cx - 1][7][3] = dpt;
            # down of 0
            points[cx - 1][0][3] = corners[7 * (1 - 1) + (cx - 1)][0];
            # up of 7
            points[cx - 1][7][1] = corners[7 * (7 - 1) + (cx - 1)][0];

        offset = np.zeros(2, dtype=np.float32);
        for cx in range(1, 7):
            pt1 = points[cx][0][0];
            pt2 = points[cx][0][1];
            offset += (pt2 - pt1);
        offset /= 6;

        lpt = points[0][0][1] - offset;
        rpt = points[7][0][0] + offset;

        points[0][0][0] = lpt;
        points[7][0][1] = rpt;

        offset = np.zeros(2, dtype=np.float32);
        for cx in range(1, 7):
            pt1 = points[cx][7][2];
            pt2 = points[cx][7][3];
            offset += (pt2 - pt1);
        offset /= 6;

        lpt = points[0][7][3] - offset;
        rpt = points[7][7][2] + offset;

        points[0][7][2] = lpt;
        points[7][7][3] = rpt;

        return points;


def main():
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001);

    startVideoFeed();
    #colorTestFeed();
    board = np.zeros((8,8));
    for x in range(0, 8):
        for y in range(0, 8):
            board[x,y] = x*10+y;

    newboard = rotateBoardClockwise(board);
    print(board);
    print(newboard);



    return;
    vision = pychess_vision();

    img = cv2.imread("temp.jpg", cv2.IMREAD_COLOR);
    img = cv2.resize(img, (0, 0), fx=.25, fy=.25);

    vision.setImage(img);
    if vision.attemptFindChessboard(1):
        vision.establishCornerPoints();
        vision.establishSquareImages();
        vision.identifiyAllPieces();
        print(vision.board);
        vision.showChessboard();
        vision.drawAllPieceNames();
        cv2.imshow("chess image", vision.image);

    cv2.waitKey(0);
    cv2.destroyAllWindows();
    return;

def colorTestFeed():
    cam = cv2.VideoCapture(0);
    vision = pychess_vision();

    while True:

        ret_val, img = cam.read();

        if ret_val:

            #img = cv2.resize(img, (0, 0), fx=.1, fy=.1);
            height, width = img.shape[:2];

            for x in range(0,width,10):
                for y in range(0,height,10):
                    colID = pychess_vision.getColor(img[y][x]);
                    color = [0,0,0];
                    img[y][x] = (0, 0, 0);
                    if colID > -1:
                        color[colID] = 255;
                        cv2.circle(img, (x, y), 5, color, -1);


            cv2.imshow("cam",img);


        if cv2.waitKey(1) == 27:
            break  # esc to quit

    cv2.destroyAllWindows();


def startVideoFeed():
    cam = cv2.VideoCapture(0);
    vision = pychess_vision();

    while True:
        ret_val, img = cam.read();

        if ret_val:
            cv2.imshow("cam", img);

            sst = time.time();
            st = time.time();

            vision.setImage(img);
            if vision.attemptFindChessboard():
                print("attempt " + str(time.time() - st));
                st = time.time();
                vision.establishCornerPoints();
                print("establish corners " + str(time.time() - st));
                st = time.time();
                vision.establishSquareImages();
                print("establish square images " + str(time.time() - st));
                st = time.time();
                vision.identifiyAllPieces();
                print("identify all pieces " + str(time.time() - st));
                st = time.time();
                print(vision.board);
                vision.paintChessboard();
                print("paint chessboard " + str(time.time() - st));
                st = time.time();
                vision.drawAllPieceNames();
                print("draw piece names " + str(time.time() - st));
                st = time.time();
                cv2.imshow("chess image ", vision.image);
                print("show img " + str(time.time() - st));
                print(time.time()-sst);
                print("");
                print("");

        if cv2.waitKey(1) == 27:
            break  # esc to quit

    cv2.destroyAllWindows();


def rotateBoardClockwise(board):
    newboard = board * 1;

    for x in range(0,8):
        if x < 4:
            nx = x - 4;
        else:
            nx = x - 3;
        for y in range(0,8):
            if y < 4:
                ny = y - 4;
            else:
                ny = y - 3;
            pnx = -ny;
            pny = nx;
            if pnx<0:
                px = pnx+4;
            else:
                px = pnx+3;
            if pny<0:
                py = pny+4;
            else:
                py = pny+3;
            newboard[x,y] = board[px,py];
    return newboard;

if __name__ == "__main__":
    main();




