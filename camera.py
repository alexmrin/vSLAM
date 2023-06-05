import cv2
import numpy as np

#directly applying a while loop to the extraction process
cap = cv2.VideoCapture(1)
while(True):
    ret, frame = cap.read()
    #conversion from bgr to grayscale
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if frame is not None:
        cv2.imshow("Frame", grayframe)
    key = cv2.waitKey(1)
    #press q to close window
    if key == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()