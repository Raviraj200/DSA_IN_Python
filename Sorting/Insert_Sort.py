
def Insert_Sort(list):
    for i in range(1,len(list)):
        temp = list[i]
        j=i-1
        while j>=0 and temp<list[j]:
            list[j+1] = list[j]
            j-=1
        list[j+1] = temp    

list=[12, 11, 13, 5, 6]
Insert_Sort(list)
print(list)