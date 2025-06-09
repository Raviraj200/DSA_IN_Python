arr1= [[1,2,3,4],[4,5,6,5],[7,8,9,4],[7,8,5,3]]
for i in range(len(arr1)):
    for j in range(len(arr1)):
        if j==i:
            print(arr1[i][j],end=" ")
        else:
            print("*",end=" ") 
    print()           


         
