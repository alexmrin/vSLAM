import cv2
import numpy as np

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