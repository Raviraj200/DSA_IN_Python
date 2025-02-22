class Sort:
    def Sorts(self,list):
        n = len(list)
        for i in range(n):
            for j in range(i, n-1):
                if list[i]>list[i+1]:
                    list[i],list[i+1]=list[i+1],list[i]
        return list              
list =[64, 34, 25, 12, 22, 11, 90]        
s =Sort()
for i in range(0,len(list)-1):
    s.Sorts(list) 
print(s.Sorts(list))    
            