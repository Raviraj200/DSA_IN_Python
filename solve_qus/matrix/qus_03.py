arr=[[1,2,3],[4,5,6],[7,8,9]]
n=len(arr)
result =[[0 for _ in range(n)] for _ in range(n)]
for i in range(0,n-1):
    for j in range(i+1,n):
        # result[j][(n-1)-i]= arr[i][j]
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
for i in range(0,n):
    arr[i].reverse()          
print(arr)        