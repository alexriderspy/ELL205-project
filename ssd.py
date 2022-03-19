def ssd(arr1,arr2):
    sumr = 0
    sumg = 0
    sumb = 0
    n1 = arr1.shape[0]
    n2 = arr1.shape[1]
    for i in range(0,n1):
        for j in range(0,n2):
            sumr = sumr + (arr1[i][j][0] - arr2[i][j][0])**2
            sumg = sumg + (arr1[i][j][1] - arr2[i][j][1])**2
            sumb = sumb + (arr1[i][j][2] - arr2[i][j][2])**2
    return (sumr,sumg,sumb)