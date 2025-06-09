import math 
nums = [100,4,200,1,3,2,5,6,5]
n=len(nums)
my_set =set()
for i in range(0,n):
  
    my_set.add(nums[i])
lonest =0
for num in my_set:
    print(num)
    if num-1 not in my_set:
        u=num
        count=1
        while u+1 in my_set:
            count+=1
            u+=1
        lonest=max(lonest,count)
