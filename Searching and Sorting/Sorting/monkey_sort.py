import random
import time


# a= [1,2,3,4,5,6]
# random.shuffle(a)
# print(a)


def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            sorted = False
    return  sorted        

def monkey_sort(arr):

    while not is_sorted(arr):
        time.sleep(0.5)
        random.shuffle(arr)
        print(arr)
    print(arr)

def sleep_sort(arr):
    for i in range(len(arr)-1):
        time.sleep(arr[i])
        print(arr[i])

a = [1,2,3,40,1]  

# sleep_sort(a)

monkey_sort(a)