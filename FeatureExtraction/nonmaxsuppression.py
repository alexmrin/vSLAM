import numpy as np


def IOU(side_length, topcorner, corner):
    box1 = [topcorner[0]-side_length/2, topcorner[1]-side_length/2, topcorner[0]+side_length/2, topcorner[1]+side_length/2]
    box2 = [corner[0]-side_length/2, corner[1]-side_length/2, corner[0]+side_length/2, corner[1]+side_length/2]
    # determine the coordinates of the intersection rectangle
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    # compute the area of intersection rectangle
    inter_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)

    # compute the area of both the prediction and ground-truth rectangles
    box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    # compute the intersection over union by taking the intersection area and dividing it by the sum of prediction + ground-truth areas - the intersection area
    iou = inter_area / float(box1_area + box2_area - inter_area)

    # return the intersection over union value
    return iou

def non_max_suppression(corners, threshold, side_length):
    suppressed_corners = []
    while corners:
        topcorner = corners.pop(0)
        suppressed_corners.append(topcorner)
        corners = [corner for corner in corners if IOU(side_length, topcorner[0], corner[0]) <= threshold]
    return suppressed_corners