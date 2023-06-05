import cv2
import numpy as np

def fastcornerdetect(frame, threshold, diffpixelnum):
    
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    height = grayframe.shape[0]
    width = grayframe.shape[1]
    corners = []
    
    for i in range(3, height - 3):
        for j in range(3, width - 3):
            pixelpos = grayframe[i, j]
            
            patterns = [grayframe[i - 3, j - 1], grayframe[i - 3, j], grayframe[i - 3, j + 1],
                        grayframe[i - 2, j + 1], grayframe[i - 1, j + 2], grayframe[i, j + 3],
                        grayframe[i + 1, j + 2], grayframe[i + 2, j + 1], grayframe[i + 3, j],
                        grayframe[i + 2, j - 1], grayframe[i + 1, j - 2], grayframe[i, j - 3],
                        grayframe[i - 1, j - 2], grayframe[i - 2, j - 1]]
            
            pixeldiff = np.abs(np.array(patterns) - pixelpos)
            overthreshold = np.sum(pixeldiff > threshold)
            underthreshold = np.sum(pixeldiff < threshold)
            
            if overthreshold >= diffpixelnum or underthreshold >= diffpixelnum:
                corners.append((j, i))
    
    return corners
            

imagepath = "testimage path"
testimage = cv2.imread(imagepath)
threshold = 10
pixelnumbers = 14
fastcorners = fastcornerdetect(testimage, threshold, pixelnumbers)

for corner in fastcorners:
    cv2.circle(testimage, corner, radius = 3, color = (0,255,0), thickness = 1)

cv2.imshow("testimage", testimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
