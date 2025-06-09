arr = [-1,0,1,2,-1,-4]
arr.sort()
print(arr)
n=len(arr)
# mySet=set()
# for x in range(0,n):
#     for y in range(x+1,n):
#         for z in range(y+1,n):
#             if nums[x]+nums[y]+nums[z]==0:
#                 temp=[nums[x],nums[y],nums[z]]
#                 temp.sort()
#                 mySet.add(tuple(temp))

# print(mySet)
                
# result=set()
# for i in range(0,n):
#     mySet=set()
#     for j in range(i+1,n):
#         third=-(arr[i]+arr[j])
#         if third in mySet:
#             temp = [arr[i],arr[j],third]
#             temp.sort()
#             result.add(tuple(temp))
#         mySet.add(arr[j])
# print([list(ans) for ans in result])                      
        

result=[]
for i in range(0,n):
    if i!=0 and arr[i]==arr[i-1]:
        continue
    j=i+1
    k=n-1
    while j<k:
        total_sum =arr[i] +arr[j]+arr[k]
        if total_sum<0:
            j+=1
        elif total_sum>0:
            k-=1
        else:
            temp =[arr[i],arr[j],arr[k]]
            result.append(temp)
            j+=1
            k-=1
            while j<k and arr[j]==arr[j-1]:
                j+=1
            while j<k and arr[k]==arr[k+1]:
                k-=1            
 
for i in range(0,len(result)):
    print(result[i])      

