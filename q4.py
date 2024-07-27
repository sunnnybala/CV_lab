import cv2
img = cv2.imread("image.jpeg")
start = (5,5)
end = (260,150)
color = (0,0,0)
thickness = 5
image = cv2.rectangle(img, start, end, color, thickness)

cv2.imshow("q4", image)
cv2.waitKey(10000)