import cv2
import time 
import tkinter as tk
from tkinter import filedialog

#user can either bring an image or use the default image to corner detect
def userfilechoice():
    userchoice = input("Do you want to import an image (jpg) to corner detect? (y/n) If no, a default image will be used: ")
    if userchoice.lower() == "y":
        root = tk.Tk()
        root.withdraw()
        userchoice = filedialog.askopenfilename()
    elif userchoice.lower() == "n":
        userchoice = "/Users/alexa/Desktop/vSLAM/testimages/fasttestimage2.jpg"
    
    return userchoice



imagepath = userfilechoice()
starttime = time.time()
testimage = cv2.imread(imagepath)

#resizing
resizescale = 50
resizewidth = int(testimage.shape[1]*resizescale/100)
resizeheight = int(testimage.shape[0]*resizescale/100)
resizedim = (resizewidth, resizeheight)
resizedimage = cv2.resize(testimage, resizedim, interpolation = cv2.INTER_LANCZOS4)

#conversion to grayscale
grayframe = cv2.cvtColor(resizedimage, cv2.COLOR_BGR2GRAY)

#orb object
orb = cv2.ORB_create()
keypoints = orb.detect(grayframe, None)
keypoints, descriptors = orb.compute(grayframe, keypoints)
endtime = time.time()

for keypoint in keypoints:
    x, y = keypoint.pt
    cv2.circle(resizedimage, (int(x), int(y)), radius = 2, color = (0,255,0), thickness = 2)


#Printing processing time and the resolutions
processtime = endtime - starttime
print(f"Process time: {processtime}")
print(f"width: {resizewidth}, height: {resizeheight}")

#Display corner detected image
cv2.imshow("Detected Corners", resizedimage)
cv2.waitKey(0)
cv2.destroyAllWindows()