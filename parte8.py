import cv2
import numpy as np
from matplotlib import pyplot as plt

video = cv2.VideoCapture(0)
points = []

while(True):
    _, frame = video.read()

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #vermelho=165-179 / verde=45-75 
    lower = np.array([45, 100, 50])
    upper = np.array([100, 255, 255])

    mask = cv2.inRange(hsvFrame, lower, upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        i = 0
        maxArea = cv2.contourArea(contours[0])
        idContourMaxArea = 0
        for c in contours:
            if maxArea < cv2.contourArea(c):
                maxArea = cv2.contourArea(c)
                idContourMaxArea = i
            i += 1
        x, y, w, h = cv2.boundingRect(contours[idContourMaxArea])

        if cv2.contourArea(contours[idContourMaxArea]) > 50:
            points.append((int(w/2+x), int(h/2+y)))

        if len(points) > 1:
            for i in range(1, len(points)):
                cv2.line(frame, points[i], points[i-1], (255,255,0), i)

        if len(points) > 20:
            points.pop(0)

        if(maxArea > 100.0):
            cv2.circle(frame, (int(x+(w/2)+1), int(y+(h/2)+1)), int(h/2), (0, 0, 255), 3)
            cv2.drawContours(frame, [contours[idContourMaxArea]], 0, (0, 255, 0), 3)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()