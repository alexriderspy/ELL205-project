import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import sys

global arr1, arr2, n1, n2,h1,h2, arr

def ssd(arr1,arr2,l,b):
    sumr = 0.0
    sumg = 0.0
    sumb = 0.0
    #print(n1,n2)

    for i in range(0,n1):
        for j in range(0,n2):
            #print(arr1[i][j][0] - arr2[l+i][b+j][0])
            sumr = sumr + (float(arr1[i][j][0]) - float(arr2[l+i][b+j][0]))**2
            sumg = sumg + (float(arr1[i][j][1]) - float(arr2[l+i][b+j][1]))**2
            sumb = sumb + (float(arr1[i][j][2]) - float(arr2[l+i][b+j][2]))**2
    return sumr+sumg+sumb

def helper(col1_template,col2_template,col1_test,col2_test):
    val = 0.0
    for i in range(0,n1):
        val = val - ((float(arr1[i][col1_template][0]) - float(arr2[i][col1_test][0]))**2 + (float(arr1[i][col1_template][1]) - float(arr2[i][col1_test][1]))**2 + (float(arr1[i][col1_template][2]) - float(arr2[i][col1_test][2]))**2) + ((float(arr1[i][col2_template][0]) - float(arr2[i][col2_test][0]))**2 + (float(arr1[i][col2_template][1]) - float(arr2[i][col2_test][1]))**2 + (float(arr1[i][col2_template][2]) - float(arr2[i][col2_test][2]))**2)
    return val

def traverse():
    mini=sys.float_info.max
    threshold=0.5
    for i in range(0,h1-n1):
        val = ssd(arr1,arr2,i,0)
        if val < mini:
            arr.append((i,0))
            mini = min(mini,val)
        
        for j in range(0,h2-n2):
            val = val + helper(0,n2-1,j,j+n2)
            if val < mini:
                arr.append((i,j))
                mini = min(mini,val)

    # for i in range(0,h1-n1):
    #     for j in range(0,h2-n2):
    #         if ssd(arr1,arr2,i,j)<=mini+threshold:
    #             arr.append((i,j))
                
arr1 = cv2.imread("template.jpeg", cv2.IMREAD_COLOR)
arr2 = cv2.imread("test.jpeg", cv2.IMREAD_COLOR)
arr=[]
n1 = arr1.shape[0]
n2 = arr1.shape[1]
h1 = arr2.shape[0]
h2 = arr2.shape[1]
print(n1,n2,h1,h2)
traverse()

imagetest = plt.imread('test.jpeg')
fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

for i in range(0,len(arr)):
    x,y=arr[i]
    rect = patches.Rectangle((x, y), n1, n2, edgecolor='green', facecolor='none', linewidth=2)
    ax.add_patch(rect)
    
plt.show()
