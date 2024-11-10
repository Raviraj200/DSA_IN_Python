def search(arr,start,end ,item):
    if start<=end:
        mid = (start + end)//2

        if arr[mid]== item:
            return mid
        elif arr[mid]<item:
            return search(arr,mid+1,end,item)
        else:
            return search(arr,start,mid-1, item)
    else:
        return "Not Found"

arr=[1,2,3,4,5,6,7,8,9]
print(search(arr,0,len(arr)-1,9))


# def sorting(arr):
#     sorted = True
#     for i in range(len(arr)-1):
#         if(arr[i]>arr[i+1]):
#             sorted = False
#     return sorted

# arr=[1,2,3,4,5,6,5]
# print(sorting(arr))              
