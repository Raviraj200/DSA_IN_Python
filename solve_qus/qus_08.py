n=[3,2,1,5,6,4,7,8,9,4,8,10]
m=[10,2,3,6,5,49,8,5,2,6,4,120]
dist={}
for i in range(1,len(m)):
    count=0 
    for j in range(1,len(n)):
        if m[i]==n[j]:
            count+=1
            dist[m[i]]=count
print(dist) 


