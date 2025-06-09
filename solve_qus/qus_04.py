n=153
num = n
count=0
length = len(str(n))
while num>0:
    lastNum =num%10
    count=count+(lastNum**length)
    num=num//10
print(count)


