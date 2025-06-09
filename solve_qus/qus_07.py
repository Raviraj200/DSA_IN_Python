nums =[6,4,5,2,1,2,1,2,5,4,2]
freq_map = {}

for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1
freq_map[0]=50
print(freq_map)

# # ******************************************************************* 2 way 
# n = len(nums)
# for i in range(0,n):
#     freq_map[nums[i]] = freq_map.get(nums[i],0)+1

# print(freq_map)