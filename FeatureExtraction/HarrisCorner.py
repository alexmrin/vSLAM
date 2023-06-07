import cv2
import numpy as np
from nonmaxsuppression import non_max_suppression
from numpy import linalg as LA


def harris_corners(gray, corners, window_size = 3, k = 0.04):
    # Calculate gradients
    Ix = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    Iy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)

    # Calculate products of gradients
    Ixx = Ix**2
    Ixy = Iy*Ix
    Iyy = Iy**2

    corner_list = []
    offset = window_size//2

    # Apply Harris corner detection
    for corner in corners:
        if corner[0] < 1 or corner[0] > gray.shape[0] - 2 or corner[1] < 1 or corner[1] > gray.shape[1] - 2:
            continue
        x = corner[0]
        y = corner[1]
        # Calculate sum of squares
        Sxx = np.sum(Ixx[y-offset:y+offset+1, x-offset:x+offset+1])
        Syy = np.sum(Iyy[y-offset:y+offset+1, x-offset:x+offset+1])
        Sxy = np.sum(Ixy[y-offset:y+offset+1, x-offset:x+offset+1])

        # Calculate determinant and trace
        det = (Sxx * Syy) - (Sxy**2)
        trace = Sxx + Syy

        # Calculate r for Harris corner response
        r = det - k*(trace**2)

        # If r is above a threshold, mark it as a corner
        if r > 10**11:
            corner_list.append(([x, y], r))

    corner_list.sort(key=lambda x: x[1], reverse=True)
    #print([pair[1] for pair in corner_list])

    return [pair for pair in corner_list]

