# vSLAM

## Camera Connection

download [iriun webcam](https://iriun.com/) on both phone and pc.

```pip install opencv-python```

## FAST (Features from Accelerated Segment Test) Algorithm

### FAST Algorithm
- Choose one pixel and let $I_p$ be its pixel value and let $t$ be the threshold value.
- Create a Bresenham circle of radius 3 around the pixel
- Check if there are 3 or more pixels from pixels 1, 5, 9, 13 with pixel value greater than $I_p+t$ or 3 or more pixels with pixel values less than $I_p-t$
- Check if there are 12 or more pixels from the circle with a pixel value greater than $I_p+t$ or 12 or more pixels with pixel values less than $I_p-t$
- Append to a list of corners
- Repeat for all pixels of the image

<img src="https://www.mdpi.com/applsci/applsci-10-00443/article_deploy/html/images/applsci-10-00443-g002.png" height="500" width="500" >

### Harris Corner Detection
*After obtaining candidate corner points from FAST, we now further refine and narrow down the actual corners.*
First we want a function that can calculate the variation in intensity if we move in a small direction $(u, v)$ from our point of interest $(x, y)$. $$E(u, v) = \sum_{x, y} w(x, y) [I(x + u, y + v) - I(x, y)]^2$$ where $I$ is an intensity function. Using the first-order taylor approximation, $$I(x + u, y + v) \approx I(x, y) + uI_x(x, y) + vI_y(x, y)$$ Substituting, we get $$E(u, v) \approx \sum_{x, y} w(x, y) [uI_x(x, y) + vI_y(x, y)]^2 = \sum_{x, y} w(x, y) [u^2I_x(x, y)^2 + uvI_xy(x, y) + v^2I_y(x, y)^2]$$ We can rewrite this in matrix form, 
<img src="https://latex.codecogs.com/svg.image?&space;E(u,&space;v)&space;\approx&space;\left[&space;\begin{matrix}&space;u&space;&&space;v&space;\end{matrix}&space;\right]&space;\left(&space;\sum_{x,&space;y}&space;w(x,&space;y)&space;\left[&space;\begin{matrix}&space;I^2_x&space;&&space;I_xI_y&space;\\&space;I_xI_y&space;&&space;I^2_y&space;\end{matrix}&space;\right]&space;\right)&space;\left[&space;\begin{matrix}&space;u&space;\\&space;v&space;\end{matrix}&space;\right]" height="150px" width="400px" >
Let $$H = \sum_{x, y} w(x, y) \left[ \begin{matrix} I^2_x & I_xI_y \\ I_xI_y & I^2_y \end{matrix} \right]$$ This is the harris matrix we are interested in. The eigenvalues of this matrix represent the variance in orthogonal directions. If both eigenvalues are large, there is high variance in two directions, meaning that the point of interest is a corner. If one eigenvalue is much larger than the other, it should correspond to an edge, and if both are small, we can think of it as flat. In order to derive an equation for the "cornerness" of a point, we assign it an R-value, $$R = \det(H) - k (\mathrm{trace}(H))^2$$ where a higher R represents a higher quality corner, and k is an experimentally determined constant ($0.04 - 0.06$). We determined a threshold for the minimum value of R and only accepted points above this threshold.


### FAST Corner detection vs. threshold

<img
     src = "/fastexperiment/fastcorner_threshold(5).jpg"
     alt = "threshold5"
     title = "Fast Corner Detection (threshold = 5)"
     width = "300"
     height = "300">
<img
     src = "/fastexperiment/fastcorner_threshold(10).jpg"
     alt = "threshold10"
     title = "Fast Corner Detection (threshold = 10)"
     width = "300"
     height = "300">
<img
     src = "/fastexperiment/fastcorner_threshold(15).jpg"
     alt = "threshold5"
     title = "Fast Corner Detection (threshold = 15)"
     width = "300"
     height = "300">
<img
     src = "/fastexperiment/fastcorner_threshold(20).jpg"
     alt = "threshold5"
     title = "Fast Corner Detection (threshold = 20)"
     width = "300"
     height = "300">
<img
     src = "/fastexperiment/fastcorner_threshold(25).jpg"
     alt = "threshold5"
     title = "Fast Corner Detection (threshold = 25)"
     width = "300"
     height = "300">
<img
     src = "/fastexperiment/fastcorner_threshold(30).jpg"
     alt = "threshold5"
     title = "Fast Corner Detection (threshold = 30)"
     width = "300"
     height = "300">
