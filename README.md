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

### Intensity Centroid Orientation

For each corner detected, the intensity moment can be calculated as:

$m_{pq} = \displaystyle\sum_{x, y}x^py^qI(x, y)$

from -r to r (r: radius of Bresenham circle)

The corner angle can be calculated as:

$\theta = \arctan2(m_{01}, m_{10})$

Whre $arctan2$ is a quadrant aware version of arctan (accesible from numpy libary)

### Oriented FAST Test

<img
     src = "/fastexperiment/oFASTfinal.jpg"
     alt = "woodenblocks"
     title = "oFAST (woodenblock)"
     width = "400"
     height = "400">

<img
     src = "/fastexperiment/oFASTfinal2.jpg"
     alt = "rubiccube"
     title = "oFAST (rubics cube)"
     width = "250"
     height = "250">

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
