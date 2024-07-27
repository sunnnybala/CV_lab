import cv2
import numpy as np
img = cv2.imread("image.jpeg")
print(img.dtype)

down_width = 100
down_height = 100
down_points = (down_width, down_height)
resize_down = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)
cv2.imshow('Resized Down by defining height and width', resize_down)
cv2.waitKey(1000)