import cv2
import numpy as np
import os

def fastcornerdetect(grayframe, threshold, diffpixelnum):
    
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

def harris_corners(grayframe, corners, k, N):
    R_values = []
    # Calculate the partial derivatives for each pixel
    sobelx = cv2.Sobel(grayframe, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(grayframe, cv2.CV_64F, 0, 1, ksize=5)
    
    # Create a Gaussian kernel
    gkern = cv2.getGaussianKernel(ksize=5, sigma=-1)
    gkern = gkern * gkern.T
    
    # Calculate the R value for every candidate corner
    for corner in corners:
        harris_matrix = np.zeros((2, 2))
        # calculate the harris matrix by summing each x, y matrix
        for i in range(25):
            x = corner[0] - 2 + i // 5
            y = corner[1] - 2 + i % 5
            grad = np.array([sobelx[x, y], sobely[x, y]])
            
            # Apply the Gaussian window
            weighted_grad = gkern[i // 5, i % 5] * grad
            
            harris_matrix += np.outer(weighted_grad, weighted_grad)
        # Calculate R value
        R_value = np.linalg.det(harris_matrix) - k * (np.trace(harris_matrix))**2
        R_values.append((corner, R_value))

    R_values.sort(key=lambda x: x[1], reverse=True)
    # Return the top N corners
    return [pair[0] for pair in R_values[:N]]



imagepath = "/Users/alexa/vSLAM/testimages/fasttestimage3.jpg"
testimage = cv2.imread(imagepath)
threshold = 10
pixelnumbers = 12
#conversion to grayscale
grayframe = cv2.cvtColor(testimage, cv2.COLOR_BGR2GRAY)
fastcorners = fastcornerdetect(grayframe, threshold, pixelnumbers)
# fastcorners = harris_corners(grayframe, fastcorners, 0.04, 20)
# print(fastcorners)

for corner in fastcorners:
    cv2.circle(testimage, corner, radius = 3, color = (0,255,0), thickness = 1)

cv2.imshow("corners", testimage)
cv2.waitKey(0)
cv2.destroyAllWindows()