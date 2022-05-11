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

img_rgb = cv2.imread('images/test4.png')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template = cv2.imread('images/template4.png',0)

arr50=[(sys.float_info.max,0,0)]
arr25 = [(sys.float_info.max,0,0)]
arr=[(sys.float_info.max,0,0)]
arr200=[(sys.float_info.max,0,0)]
arr400=[(sys.float_info.max,0,0)]

h1,h2 = img_gray.shape[::]
n1,n2 = template.shape[::]

img_gray50 = img_gray
img_gray25 = img_gray50
img_gray200 = img_gray
img_gray400 = img_gray200

h3,h4 = img_gray50.shape[::]
h5,h6 = img_gray200.shape[::]

img_gray50 = cv2.pyrDown(img_gray50, dstsize=(h2//2, h1//2))
img_gray25 = cv2.pyrDown(img_gray25, dstsize=(h4//2, h3//2))
img_gray200 = cv2.pyrUp(img_gray200, dstsize=(2 * h2, 2 * h1))
img_gray400 = cv2.pyrUp(img_gray400, dstsize=(2 * h6, 2 * h5))

arr50 = traverse(template,img_gray50,arr50,h1//2,n1,h2//2,n2)
arr50.sort()

arr25 = traverse(template,img_gray25,arr25,h3//2,n1,h4//2,n2)
arr25.sort()

arr200 = traverse(template,img_gray200,arr200,h1*2,n1,h2*2,n2)
arr200.sort()

arr400 = traverse(template,img_gray400,arr400,h5*2,n1,h6*2,n2)
arr400.sort()

arr = traverse(template,img_gray,arr,h1,n1,h2,n2)
arr.sort()

mini = min(arr[0][0],min(arr50[0][0],min(arr200[0][0],min(arr400[0][0],arr25[0][0]))))

for i in range(0,len(arr)):
    if arr[i][0] <= (1.2*mini):
        top_left = (arr[i][2],arr[i][1])
        bottom_right = (top_left[0] + n2, top_left[1] + n1)
        cv2.rectangle(img_rgb,top_left,bottom_right,(255,0,0),2)
    else:
        break

for i in range(0,len(arr25)):
    if arr25[i][0] <= (1.2*mini):
        top_left = (arr25[i][2]*4,arr25[i][1]*4)
        bottom_right = ((top_left[0] + n2*4), (top_left[1] + n1*4))
        cv2.rectangle(img_rgb,top_left,bottom_right,(255,0,0),2)
    else:
        break

for i in range(0,len(arr50)):
    if arr50[i][0] <= (1.2*mini):
        top_left = (arr50[i][2]*2,arr50[i][1]*2)
        bottom_right = ((top_left[0] + n2*2), (top_left[1] + n1*2))
        cv2.rectangle(img_rgb,top_left,bottom_right,(255,0,0),2)
    else:
        break

for i in range(0,len(arr200)):
    if arr200[i][0] <= (1.2*mini):
        top_left = (arr200[i][2]//2,arr200[i][1]//2)
        bottom_right = ((top_left[0] + n2//2), (top_left[1] + n1//2))
        cv2.rectangle(img_rgb,top_left,bottom_right,(255,0,0),2)
    else:
        break

for i in range(0,len(arr400)):
    if arr400[i][0] <= (1.2*mini):
        top_left = (arr400[i][2]*4,arr400[i][1]*4)
        bottom_right = ((top_left[0] + n2*4), (top_left[1] + n1*4))
        cv2.rectangle(img_rgb,top_left,bottom_right,(255,0,0),2)
    else:
        break

cv2.imshow('Matched image',img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()
