import cv2

img = cv2.imread("image.png", cv2.IMREAD_COLOR)
print(img.shape[0])
print(img.shape[1])
print(img)