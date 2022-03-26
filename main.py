import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import cv2
import sys

global arr1, arr2, n1, n2, h1, h2, arr

def ssd(l,b):
    sum = 0.0
    for i in range(0,n1):
        for j in range(0,n2):
            sum = sum + (float(arr1[i][j]) - float(arr2[l+i][b+j]))**2
    return sum

def helper(col1_template,col2_template,col1_test,col2_test):
    val = 0.0
    for i in range(0,n1):
        val = val - (float(arr1[i][col1_template]) - float(arr2[i][col1_test]))**2 + (float(arr1[i][col2_template]) - float(arr2[i][col2_test]))**2
        
    return val

def traverse():
    mini=sys.float_info.max
    for i in range(0,h1-n1):
        val = ssd(i,0)
        arr.append((val,i,0))
            
        
        for j in range(0,h2-n2):
            val = val + helper(0,n2-1,j,j+n2)
            print(val)
            arr.append((val,i,j))
        
            
    print(mini)

def normal():
    for i in range(0,h1-n1):            
        
        for j in range(0,h2-n2):
            val = ssd(i,j)
            arr.append((val,i,j))
            print(val)

test_grayscale = cv2.imread('test.jpeg',0)
template_grayscale = cv2.imread('template.jpeg',0)

cv2.imwrite('template_grayscale.png',template_grayscale)
cv2.imwrite('test_grayscale.png',test_grayscale)

arr1 = cv2.imread('template_grayscale.png',0)
arr2 = cv2.imread('test_grayscale.png',0)

arr=[]
n1 = arr1.shape[0]
n2 = arr1.shape[1]
h1 = arr2.shape[0]
h2 = arr2.shape[1]

print(n1,n2,h1,h2)

normal()

arr.sort()

print(arr)

plt.imshow(Image.open('test_grayscale.png'),cmap='gray')

print(arr[0])

# for i in range(0,len(arr)):
#     plt.gca().add_patch(patches.Rectangle((arr[i][1],arr[i][2]),n1,n2,
#                         edgecolor='blue',
#                         facecolor='none',
#                         lw=4))
plt.gca().add_patch(patches.Rectangle((arr[0][1],arr[0][2]),n1,n2,
                        edgecolor='blue',
                        facecolor='none',
                        lw=4))
plt.gca().add_patch(patches.Rectangle((arr[1][1],arr[1][2]),n1,n2,
                        edgecolor='blue',
                        facecolor='none',
                        lw=4))
plt.gca().add_patch(patches.Rectangle((arr[2][1],arr[2][2]),n1,n2,
                        edgecolor='blue',
                        facecolor='none',
                        lw=4))
plt.gca().add_patch(patches.Rectangle((arr[3][1],arr[3][2]),n1,n2,
                        edgecolor='blue',
                        facecolor='none',
                        lw=4))
# plt.gca().add_patch(patches.Rectangle((arr[0][1],arr[0][2]),n1,n2,
#                         edgecolor='blue',
#                         facecolor='none',
#                         lw=4))
# plt.gca().add_patch(patches.Rectangle((arr[0][1],arr[0][2]),n1,n2,
#                         edgecolor='blue',
#                         facecolor='none',
#                         lw=4))

plt.show()