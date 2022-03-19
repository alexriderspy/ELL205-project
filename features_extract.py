import cv2

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("image.png", cv2.IMREAD_COLOR)
print(img.shape)