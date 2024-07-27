import cv2
import numpy as np
img = cv2.imread("image.jpeg")
print(img.dtype)
x,y,z = img.shape
for i in range(x):
    for j in range(y):
        print("pixel number,", i, j, " is:", img[i][j])