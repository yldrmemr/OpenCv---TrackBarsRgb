import cv2
import numpy as np

def nothing(x):
    pass
#-------------------------------------------------------------------------------
#-                      Kuphaneler
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
#-                     Nothing Fonksiyonu Mutlaka Olmali
#------------------------------------------------------------------------------
def nothing(x):
    pass
#-------------------------------------------------------------------------------
#-                      TrackBar Tanimlmalari
#------------------------------------------------------------------------------
def CreateTrackBar_Init():
    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("Lower - R", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("Lower - G", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("Lower - B", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("Upper - R", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("Upper - G", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("Upper - B", "Trackbars", 255, 255, nothing)

CreateTrackBar_Init()
cap =cv2.VideoCapture('Video.MKV')
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (720, 480))
    ConveredBgr = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    Lower_R_Value = cv2.getTrackbarPos("Lower - R", "Trackbars")
    Lower_G_Value = cv2.getTrackbarPos("Lower - G", "Trackbars")
    Lower_B_Value = cv2.getTrackbarPos("Lower - B", "Trackbars")
    Upper_R_Value = cv2.getTrackbarPos("Upper - R", "Trackbars")
    Upper_G_Value = cv2.getTrackbarPos("Upper - G", "Trackbars")
    Upper_B_Value = cv2.getTrackbarPos("Upper - B", "Trackbars")
#-------------------------------------------------------------------------------
#-                      Standart Maskeleme Islemleri
#-------------------------------------------------------------------------------
    lower_blue = np.array([Lower_R_Value,Lower_G_Value,Lower_B_Value])
    upper_blue = np.array([Upper_R_Value,Upper_G_Value,Upper_B_Value])
    mask = cv2.inRange(ConveredBgr, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
