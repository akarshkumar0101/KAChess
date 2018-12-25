import numpy as np;
import cv2;
import time;
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
        avgdx = 0.0;
        avgdy = 0.0;
        for cx in range(1, 6):
            pt1 = corners[7 * (cy - 1) + (cx - 1)][0];
            pt2 = corners[7 * (cy - 1) + (cx - 1 + 1)][0];
            avgdx += pt2[0] - pt1[0];
            avgdy += pt2[1] - pt1[1];
        avgdx /= 6;
        avgdy /= 6;

        lpt = np.zeros((2), dtype=np.float32);
        rpt = np.zeros((2), dtype=np.float32);

        lpt[0] = corners[7 * (cy - 1) + (1 - 1)][0][0] - avgdx;
        lpt[1] = corners[7 * (cy - 1) + (1 - 1)][0][1] - avgdy;
        rpt[0] = corners[7 * (cy - 1) + (1 - 1 + 6)][0][0] + avgdx;
        rpt[1] = corners[7 * (cy - 1) + (1 - 1 + 6)][0][1] + avgdy;

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
        avgdx = 0.0;
        avgdy = 0.0;
        for cy in range(1, 6):
            pt1 = corners[7 * (cy - 1) + (cx - 1)][0];
            pt2 = corners[7 * (cy - 1 + 1) + (cx - 1)][0];
            avgdx += pt2[0] - pt1[0];
            avgdy += pt2[1] - pt1[1];
        avgdx /= 6;
        avgdy /= 6;

        upt = np.zeros((2), dtype=np.float32);
        dpt = np.zeros((2), dtype=np.float32);

        upt[0] = corners[7 * (1 - 1) + (cx - 1)][0][0] - avgdx;
        upt[1] = corners[7 * (1 - 1) + (cx - 1)][0][1] - avgdy;
        dpt[0] = corners[7 * (1 - 1) + (cx - 1 + 6)][0][0] + avgdx;
        dpt[1] = corners[7 * (1 - 1) + (cx - 1 + 6)][0][1] + avgdy;

        # up of 0
        points[cx][0][0] = upt;
        # down of 7
        points[cx][7][2] = dpt;
        # down of 0
        points[cx][0][2] = corners[7 * (1 - 1) + (cx - 1)][0];
        # up of 7
        points[cy][7][0] = corners[7 * (7 - 1) + (cx - 1)][0];
        # lefter side
        # up of 0
        points[cx - 1][0][1] = upt;
        # down of 7
        points[cx - 1][7][3] = dpt;
        # down of 0
        points[cx - 1][0][3] = corners[7 * (1 - 1) + (cx - 1)][0];
        # up of 7
        points[cx - 1][7][1] = corners[7 * (7 - 1) + (cx - 1)][0];

    avgdx = 0.0;
    avgdy = 0.0;
    for cx in range(1, 6):
        pt1 = points[cx][0][0];
        pt2 = points[cx][0][1];
        avgdx += pt2[0] - pt1[0];
        avgdy += pt2[1] - pt1[1];
    avgdx /= 6;
    avgdy /= 6;

    lpt = np.zeros(2, dtype=np.float32);
    rpt = np.zeros(2, dtype=np.float32);
    lpt[0] = points[0][0][1][0] - avgdx;
    lpt[1] = points[0][0][1][1] - avgdy;
    rpt[0] = points[7][0][0][0] + avgdx;
    rpt[1] = points[7][0][0][1] + avgdy;

    points[0][0][0] = lpt;
    points[7][0][1] = rpt;

    avgdx = 0.0;
    avgdy = 0.0;
    for cx in range(1, 6):
        pt1 = points[cx][7][0];
        pt2 = points[cx][7][1];
        avgdx += pt2[0] - pt1[0];
        avgdy += pt2[1] - pt1[1];
    avgdx /= 6;
    avgdy /= 6;

    lpt = np.zeros(2, dtype=np.float32);
    rpt = np.zeros(2, dtype=np.float32);
    lpt[0] = points[0][7][1][0] - avgdx;
    lpt[1] = points[0][7][1][1] - avgdy;
    rpt[0] = points[7][7][2][0] + avgdx;
    rpt[1] = points[7][7][2][1] + avgdy;

    points[0][7][0] = lpt;
    points[7][7][1] = rpt;

    return points;



def showChessBoard(img, scale=0.3):
    iscale = 1 / scale;
    simg = cv2.resize(img, (0, 0), fx=scale, fy=scale);

    gray = cv2.cvtColor(simg, cv2.COLOR_BGR2GRAY);

    ret = False;
    ret, corners = cv2.findChessboardCorners(gray, (7, 7));

    if ret:
        corners = np.float32(corners * iscale);
        points = getPoints(corners);

        for point in corners:
            point = point[0];
            x = point[0];
            y = point[1];
            # x *= np.float32(iscale);
            # y *= np.float32(iscale);

            cv2.circle(img, (x, y), 2, (0, 255, 0), -1);


        #rx = np.random.randint(0, 8);
        #ry = np.random.randint(0, 8);
        rx = (int(time.time()*10))%8;
        ry = (int(time.time()*10/8))%8;

        for rx in range(0,8):
            for ry in range(0,8):

                cx = np.average(points[rx, ry, :, 0]);
                cy = np.average(points[rx, ry, :, 1]);
                for point in points[rx][ry]:

                    point = point;
                    x = point[0]+cx;
                    y = point[1]+cy;
                    x = np.float32(x/2);
                    y = np.float32(y/2);


                    cv2.circle(img, (x, y), 2, (0, 0, 255), -1);

    cv2.imshow("chess", img);


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
