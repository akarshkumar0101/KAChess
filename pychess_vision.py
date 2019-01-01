import numpy as np;
import cv2;
import time;
import math;
import glob;




# top left, top right, bot left, bot right
def getPoints(corners):
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
            offset += (pt2-pt1);
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
        offset += (pt2-pt1);
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



def showChessBoard(img, scale=0.25):
    iscale = 1 / scale;
    simg = cv2.resize(img, (0, 0), fx=scale, fy=scale);

    gray = cv2.cvtColor(simg, cv2.COLOR_BGR2GRAY);

    ret = False;
    ret, corners = cv2.findChessboardCorners(gray, (7, 7));

    if ret:
        corners = np.float32(corners * iscale);
        points = getPoints(corners);

        for rx in range(0,8):
            for ry in range(0,8):

                cx = np.average(points[rx, ry, :, 0]);
                cy = np.average(points[rx, ry, :, 1]);
                for point in points[rx][ry]:

                    point = point;
                    x = point[0];
                    y = point[1];

                    cv2.circle(img, (x,y), 5, (0, 0, 255), -1);

        test(points,img);
    cv2.imshow("chess", img);
    return;


def test(points, img):
    for cy in range(0,8):
        for cx in range(0,8):
            ptsfrom = points[cx][cy];
            ptsto = np.float32([[0,0],[500,0],[0,500],[500,500]]);

            Mtrans = cv2.getPerspectiveTransform(ptsfrom,ptsto);

            sqrimg = cv2.warpPerspective(img, Mtrans, (500, 500));

            strf = "sqr "+str(cx)+","+str(cy);
            cv2.imshow(strf,sqrimg);

    return;


def isProdominantlyBlue(col):
    blue = col[0];
    green = col[1];
    red = col[2];
    avg = np.average(green, red);
    if blue > avg*1.5:
        return True;
    return False;

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001);
# Arrays to store object points and image points from all the images.
imgpoints = [];  # 2d points in image plane.

# img = cv2.imread("chessboard1.png", cv2.IMREAD_COLOR);

# showChessBoar(img);


cam = cv2.VideoCapture(0);

while True:

    ret_val, img = cam.read();
    # cv2.imshow("raw webcam", img);

    if cv2.waitKey(1) == 27:
        break  # esc to quit
    if ret_val:
        showChessBoard(img);

cv2.destroyAllWindows()
