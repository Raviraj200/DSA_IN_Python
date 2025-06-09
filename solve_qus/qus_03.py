n = 123321
num =n 
result = 0
while num>0:
    lastNum = num%10
    result = (result*10)+lastNum
    num = num//10
print(result)