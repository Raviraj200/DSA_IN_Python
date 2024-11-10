
import time
import random

def selectionSort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    print(arr)

arr=[]

for i in range(1000):
    arr.append(random.randint(1,1000))

start = time.time()
selectionSort(arr)     
print(time.time()-start)           