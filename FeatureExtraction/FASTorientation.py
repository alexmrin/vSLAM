import cv2
import numpy as np

def fast_angles(grayframe, selectedcorners):
    angles = []       
        
    for corner in selectedcorners:
        sumintmomentx = 0
        sumintmomenty = 0 
        for x in range(-3, 4):
            intmomentx = x * grayframe[corner[0][0] + x, corner[0][1]]
            sumintmomentx += intmomentx
        for y in range(-3, 4):
            intmomenty = y * grayframe[corner[0][0], corner[0][1] + y]
            sumintmomenty += intmomenty
                    
        angleorientation = np.degrees(np.arctan2(sumintmomenty, sumintmomentx))
        angles.append(angleorientation)
    
    return angles