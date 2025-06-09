def reverse(num,start,end):
    if start==end or start>=end:
        return
    num[start],num[end]=num[end],num[start]
    return reverse(num,start+1,end-1)

num =[5,4,6,3,2,1,7,2,2]
print(num)
reverse(num,0,len(num)-1)
print(num)