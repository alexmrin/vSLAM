import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import time
from FASTCorner import fast_corners
from HarrisCorner import harris_corners
from nonmaxsuppression import non_max_suppression
from FASTorientation import fast_angles
from BRIEF import briefdescriptor


#user can either bring an image or use the default image to corner detect
def userfilechoice():
    userchoice = input("Do you want to import an image (jpg) to corner detect? (y/n) If no, a default image will be used: ")
    if userchoice.lower() == "y":
        root = tk.Tk()
        root.withdraw()
        userchoice = filedialog.askopenfilename()
    elif userchoice.lower() == "n":
        userchoice = "testimages/fasttestimage2.jpg"
    
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

#obtaining corner pixel candidates from FAST
threshold = 5
pixelnumbers = 10
fastcorners = fast_corners(grayframe, threshold, pixelnumbers)

#running Harris on FAST corner candidates
harriscorners = harris_corners(grayframe, fastcorners)

#running harris through NMS
supcorners = non_max_suppression(harriscorners, 0.75, 100)

#finding binary descriptor of corners
binarydesc = briefdescriptor(grayframe, supcorners)

#calculating corner angles
cornerangles = fast_angles(grayframe, supcorners)
endtime = time.time()

#a new list for all corder coordinates, angles, and binary description
cornersandangles = []
for i, supcorner in enumerate(supcorners):
    cornersandangles.append([supcorner[0][0], supcorner[0][1], cornerangles[i], binarydesc[i]])

linelength = 20
for cornerandangle in cornersandangles:
    #print coordinates, angle, and descriptor of a corner
    print(f"Coord: {(cornerandangle[0], cornerandangle[1])}")
    print(f"Angle: {cornerandangle[2]}")
    print(f"Binary Descriptor: {cornerandangle[3]}")
    
    #add a circle and line extending from a corner
    cv2.line(resizedimage, (cornerandangle[0], cornerandangle[1]), (int(cornerandangle[0] + linelength * np.cos(np.radians(cornerandangle[2]))), int(cornerandangle[1] + linelength * np.sin(np.radians(cornerandangle[2])))), (255, 0, 0), 1)
    cv2.circle(resizedimage, (cornerandangle[0], cornerandangle[1]), radius = 2, color = (0,255,0), thickness = 2)

#Printing processing time and the resolutions
processtime = endtime - starttime
print(f"Process time: {processtime}")
print(f"width: {resizewidth}, height: {resizeheight}")

#Display corner detected image
cv2.imshow("Detected Corners", resizedimage)
cv2.waitKey(0)
cv2.destroyAllWindows()