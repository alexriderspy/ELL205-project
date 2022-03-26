import cv2
import numpy as np
from matplotlib import pyplot as plt

def ssd(arr1,arr2,n1,n2,l,b):
    sum = 0.0
    for i in range(0,n1):
        for j in range(0,n2):
            sum = sum + (float(arr1[i][j]) - float(arr2[l+i][b+j]))**2
    return sum

def helper(arr1,arr2,col1_template,col2_template,col1_test,col2_test):
    val = 0.0
    for i in range(0,n1):
        val = val - (float(arr1[i][col1_template]) - float(arr2[i][col1_test]))**2 + (float(arr1[i][col2_template]) - float(arr2[i][col2_test]))**2
    return val

def traverse(arr1,arr2,arr,h1,n1,h2,n2):
    for i in range(0,h1-n1):
        val = ssd(arr1,arr2,n1,n2,i,0)
        arr.append((val,i,0))
        for j in range(0,h2-n2):
            val = val + helper(arr1,arr2,0,n2-1,j,j+n2)
            arr.append((val,i,j))
    return arr

def normal(arr1,arr2,arr,h1,n1,h2,n2):
    for i in range(0,h1-n1):            
        
        for j in range(0,h2-n2):
            val = ssd(arr1,arr2,n1,n2,i,j)
            arr.append((val,i,j))
    return arr

img_rgb = cv2.imread('test1.png')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template = cv2.imread('template1.png',0)

arr=[]

h1,h2 = img_gray.shape[::]
n1,n2 = template.shape[::]

arr = traverse(template,img_gray,arr,h1,n1,h2,n2)
arr.sort()

#res = cv2.matchTemplate(img_gray,template,cv2.TM_SQDIFF)
#print(res)
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#plt.imshow(res,cmap='gray')

# threshold = 220000
# loc = np.where(res<=threshold)

# for pt in zip (*loc[::-1]):
#     cv2.rectangle(img_rgb,pt,(pt[0] + w,pt[1]+h),(0,0,255),2)
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = (arr[0][1],arr[0][2])
bottom_right = (top_left[0] + n2, top_left[1] + n1)
cv2.rectangle(img_rgb,top_left,bottom_right,255,2)

#cv2.imshow('Matched image',img_rgb)
cv2.imshow('Matched image',img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()