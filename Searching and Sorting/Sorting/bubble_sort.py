# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#         else:
#             i+=1
#     return arr        
    
# arr=[10,50,4,6,2,5,1]
# count =0
# for i in range(len(arr)-1):
#     count+=1
#     bubble_sort(arr)
#     if count == len(arr)-1:
#         print(bubble_sort(arr))



# second way*******************************************************

import random
import time

def bubble_sort(arr):
    
    for i in range(len(arr)-1):
        flag =0
        for j in range(len(arr)-1-i):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag = 1

        if flag == 0:
            break
                
    print(arr)

arr=[]
for i in range(1000):
    arr.append(random.randint(1,1000))

ll=arr
start = time.time()
print("time",start)
bubble_sort(arr)

print(time.time()-start)
