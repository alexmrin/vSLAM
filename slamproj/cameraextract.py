import cv2
import numpy as np
import time

#Function to convert webcam to frames
def extractframes():
    cap = cv2.VideoCapture(1)
    while True:
        time.sleep(0.2)
        ret, frame = cap.read()
        if ret:
            yield frame
        else:
            print("no frame")
            break
    cap.release()


#We can call extractframes function and perform a while loop with it, it'll be really slow because the funciton is called for every loop.
for frame in extractframes():
    cv2.imshow("preview", frame)
    #press q to close window
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cv2.destroyAllWindows()

