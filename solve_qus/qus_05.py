n=36
num=n
list =[]
length = len(str(num))
for i in range(1,num//2+1):
    if num%i==0:
        list.append(i)
list.append(n) 
print(list)

# *********************************************************************solve 2
from math import sqrt
num=36
result=[]
for i in range(1,int(sqrt(num))+1):
    if num % i ==0:
        result.append(i)
        if num//i != i:
            result.append(num//i)
result.sort()       
print(result)        
