import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('t.jpeg')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template = cv2.imread('tem.jpeg',0)

h,w = template.shape[::]

res = cv2.matchTemplate(img_gray,template,cv2.TM_SQDIFF)
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
plt.imshow(res,cmap='gray')

# threshold = 220000
# loc = np.where(res<=threshold)

# for pt in zip (*loc[::-1]):
#     cv2.rectangle(img_rgb,pt,(pt[0] + w,pt[1]+h),(0,0,255),2)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img_rgb,top_left,bottom_right,255,2)

#cv2.imshow('Matched image',img_rgb)
cv2.imshow('Matched image',img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()