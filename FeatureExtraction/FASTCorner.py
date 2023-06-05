import cv2
import numpy as np
import os

def fast_corners(grayframe, threshold, diffpixelnum):
    
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


