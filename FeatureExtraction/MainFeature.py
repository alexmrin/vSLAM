import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import time
from FASTCorner import fast_corners
from HarrisCorner import harris_corners
from nonmaxsuppression import non_max_suppression


#user can either bring an image or use the default image to corner detect
userchoice = input("Do you want to import an image (jpg) to corner detect? (y/n) If no, a default image will be used: ")
if userchoice.lower() == "y":
    root = tk.Tk()
    root.withdraw()
    imagepath = filedialog.askopenfilename()
elif userchoice.lower() == "n":
    imagepath = "/Users/alexa/Desktop/vSLAM/testimages/checkers.jpg"

starttime = time.time()

#import image
testimage = cv2.imread(imagepath)
threshold = 5
pixelnumbers = 10

#resizing
resizescale = 50
resizewidth = int(testimage.shape[1]*resizescale/100)
resizeheight = int(testimage.shape[0]*resizescale/100)
resizedim = (resizewidth, resizeheight)
resizedimage = cv2.resize(testimage, resizedim, interpolation = cv2.INTER_LANCZOS4)

#conversion to grayscale
grayframe = cv2.cvtColor(resizedimage, cv2.COLOR_BGR2GRAY)

#obtaining corner pixel candidates from FAST
fastcorners = fast_corners(grayframe, threshold, pixelnumbers)
harriscorners = harris_corners(grayframe, fastcorners)
finalcorners = non_max_suppression(harriscorners, 0.75, 100)

endtime = time.time()

for corner in finalcorners:
    cv2.circle(resizedimage, corner[0], radius = 3, color = (0,255,0), thickness = 1)

#Printing processing time and the resolutions
processtime = endtime - starttime
print(f"Process time: {processtime}")
print(f"width: {resizewidth}, height: {resizeheight}")

#Display corner detected image
cv2.imshow("corners", resizedimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
