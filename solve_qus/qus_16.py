nums = [5,4,-1,7,8]
max_count=float("-inf")
total=0
for i in range(0,len(nums)):
    total +=nums[i]
    max_count=max(total,max_count)


    if total<0:
        total=0

print(max_count)