import cv2
import numpy as np
from FASTCorner import fast_corners 
from HarrisCorner import harris_corners

imagepath = "/Users/alexa/vSLAM/testimages/checkers.jpg"
testimage = cv2.imread(imagepath)
threshold = 10
pixelnumbers = 12
#conversion to grayscale
grayframe = cv2.cvtColor(testimage, cv2.COLOR_BGR2GRAY)
fastcorners = fast_corners(grayframe, threshold, pixelnumbers)
fastcorners = harris_corners(grayframe, fastcorners, 0.045, 300)
print(fastcorners)

for corner in fastcorners:
    cv2.circle(testimage, corner, radius = 3, color = (0,255,0), thickness = 1)

cv2.imshow("corners", testimage)
cv2.waitKey(0)
cv2.destroyAllWindows()