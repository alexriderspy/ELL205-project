import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
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

def traverse():
    mini=4294967295
    threshold=0.5
    for i in range(0,h2-n2):
        for j in range(0,h1-n1):
            mini=min(mini,ssd(arr1,arr2,i,j))
    print(mini)

    for i in range(0,h2-n2):
        for j in range(0,h1-n1):
            if ssd(arr1,arr2,i,j)<=mini+threshold:
                arr.append((i,j))
                
arr1 = cv2.imread("template.jpg", cv2.IMREAD_COLOR)
arr2 = cv2.imread("test.jpg", cv2.IMREAD_COLOR)
arr=[]
n1 = arr1.shape[0]
n2 = arr1.shape[1]
h1 = arr2.shape[0]
h2 = arr2.shape[1]
print(n1,n2,h1,h2)
traverse()

imagetest = plt.imread('test.jpg')
fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

for i in range(0,len(arr)):
    x,y=arr[i]
    rect = patches.Rectangle((x, y), n1, n2, edgecolor='green', facecolor='none', linewidth=2)
    ax.add_patch(rect)
    
plt.show()