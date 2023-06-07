import cv2
import numpy as np

def briefdescriptor(gray, corners):
    N = 12
    binarylist = []
    pattern = [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]

    gaussian = cv2.GaussianBlur(gray, (3, 3), 1)
    
    for corner in corners:
        binarydescriptor = []
        for i in pattern:
            for j in pattern:
                if(gaussian[corner[0][0] + i, corner[0][1] + j] > gaussian[corner[0][0], corner[0][1]]):
                    binarydescriptor.append(1)
                elif(gaussian[corner[0][0] + i, corner[0][1] + j] <= gaussian[corner[0][0], corner[0][1]]):
                    binarydescriptor.append(0)
        binarylist.append(binarydescriptor)
    
    return binarylist