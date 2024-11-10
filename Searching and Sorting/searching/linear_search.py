def linear_search(arr, item):

    for i in range(len(arr)):
        if item == arr[i]:
            return "Found at Index ",i
    return "Not Found"        

arr=[40,50,30,20,40,5,0]

print(linear_search(arr,5))
