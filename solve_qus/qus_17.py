nums=[100,4,200,1,3,2]
n= len(nums)
max_count =0
for i in range(0,n):
    count=0
    num =i+1
    for j in range(0,n):
        if num in nums:
            count+=1
        max_count=max(max_count,count)    

print(count)