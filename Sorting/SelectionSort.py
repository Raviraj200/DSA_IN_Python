class Sort:

    def sorts(self,list):
        n=len(list)
        for i in range(n-1):
            for j in range(i,n-1):
                if list[i] > list[j]:
                    list[i],list[j] = list[j],list[i]
        return list            




list =[64, 34, 25, 12, 22, 11, 90]        
s =Sort()

print(s.sorts(list))    
            