def QuickSort(list):
    if len(list)<=1:
        return list
    else:
        pivot = list[0]
        lesser = [x for x in list[1:] if x<=pivot]
        greater = [x for x in list[1:] if x>pivot]
    return QuickSort(lesser) + [pivot] + QuickSort(greater)
    

list = [53,11,72,68,41,25,18,37,44,80]
print(QuickSort(list))
    



                
