import cv2
import numpy as np 

path = "GT 86.jpg"

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640,240 )
cv2.createTrackbar("Hue Min", "TrackBars", 15, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 166, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask  = cv2.inRange(img_HSV, lower, upper)
    img_result = cv2.bitwise_and(img, img,mask=mask)
    
    
    cv2.imshow("image", img)
    cv2.imshow("HVS", img_HSV)
    cv2.imshow("mask", mask)
    cv2.imshow("result", img_result)
    
    cv2.waitKey(1)