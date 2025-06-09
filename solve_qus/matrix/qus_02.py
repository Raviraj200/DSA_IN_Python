arr1= [[1,2,0,4],[4,5,6,5],[7,8,9,4],[7,8,5,3]]
r =len(arr1)
c=len(arr1[0])
rowTrack =set()
colTrack =set()

for i in range(0,r):
    for j in range(0,c):
        if arr1[i][j]==0:
            rowTrack.add(i)
            colTrack.add(j)
for i in rowTrack:
    for j in range(0,c):
        arr1[i][j]=0
for i in range(0,r):
    for j in colTrack:
        arr1[i][j]=0        
print(arr1)            