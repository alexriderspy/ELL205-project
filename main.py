import cv2
import sys

def ssd(arr1,arr2,n1,n2,l,b):
    sum = 0.0
    for i in range(0,n1):
        for j in range(0,n2):
            sum = sum + (float(arr1[i][j]) - float(arr2[l+i][b+j]))**2
    return sum

def traverse(arr1,arr2,arr,h1,n1,h2,n2):
    for i in range(0,h1-n1+1):            
        for j in range(0,h2-n2+1):
            val = ssd(arr1,arr2,n1,n2,i,j)
            arr.append((val,i,j))
    return arr

#1,2,3
img_rgb = cv2.imread('images/test1.png')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template = cv2.imread('images/template1.png',0)

arr=[(sys.float_info.max,0,0)]

h1,h2 = img_gray.shape[::]
n1,n2 = template.shape[::]

arr = traverse(template,img_gray,arr,h1,n1,h2,n2)
arr.sort()

mini = arr[0][0]

for i in range(0,len(arr)):
    if arr[i][0] <= (1.2*mini):
        top_left = (arr[i][2],arr[i][1])
        bottom_right = (top_left[0] + n2, top_left[1] + n1)
        cv2.rectangle(img_rgb,top_left,bottom_right,(255,0,0),2)
    else:
        break

cv2.imshow('Matched image',img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()