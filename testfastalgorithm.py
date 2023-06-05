import cv2
import numpy as np

def fastcornerdetect(frame, threshold, diffpixelnum):
    
    #comversion to grayscale
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #height and width of image (pixels)
    height = grayframe.shape[0]
    width = grayframe.shape[1]
    corners = []
    
    for i in range(3, height - 3):
        for j in range(3, width - 3):
            pixelpos = grayframe[i, j]
            
            #circle patttern
            patterns = [grayframe[i - 3, j - 1], grayframe[i - 3, j], grayframe[i - 3, j + 1],
                        grayframe[i - 2, j + 1], grayframe[i - 1, j + 2], grayframe[i, j + 3],
                        grayframe[i + 1, j + 2], grayframe[i + 2, j + 1], grayframe[i + 3, j],
                        grayframe[i + 2, j - 1], grayframe[i + 1, j - 2], grayframe[i, j - 3],
                        grayframe[i - 1, j - 2], grayframe[i - 2, j - 1]]
            
            #a pattern of pixels 1, 5, 9, 13
            fastpatterns = [grayframe[i + 3, j], grayframe[i, j + 3], grayframe[i - 3, j], grayframe[i, j - 3]]
            
            #Ip + t
            overthresholdvalue = pixelpos + threshold
            #Ip - t
            underthresholdvalue = pixelpos - threshold
            
            #number of pixels in the circle that are overthreshold or underthreshold
            overthreshold = np.sum(np.array(patterns) > overthresholdvalue)
            underthreshold = np.sum(np.array(patterns) < underthresholdvalue)
            #number of pixels from 1, 5, 9, 13 that are overthreshold or underthreshold
            fastoverthreshold = np.sum(np.array(fastpatterns) > overthresholdvalue)
            fastunderthreshold = np.sum(np.array(fastpatterns) < underthresholdvalue)
            
            #there must be at least 3 pixels that are overthreshold or underthreshold from pixels 1, 5, 9, 13 to be a corner  
            if fastoverthreshold >= 3 or fastunderthreshold >=3:
                #a pixel is a corner if there are n or more pixels in the circle that are overthreshold or underthreshold
                if overthreshold >= diffpixelnum or underthreshold >= diffpixelnum:
                    corners.append((j, i))
    
    return corners
            
imagepath = "fasttestimage1.jpg"
testimage = cv2.imread(imagepath)
threshold = 10
pixelnumbers = 14
fastcorners = fastcornerdetect(testimage, threshold, pixelnumbers)

for corner in fastcorners:
    cv2.circle(testimage, corner, radius = 3, color = (0,255,0), thickness = 1)

cv2.imshow("testimage", testimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
