def func(string,lift,right):
    if lift>=right:
        return True
    
    if string[lift]!=string[right]:
        return False 
    return func(string,lift+1,right-1)



s="raivar"
lift = 0
right = len(s)-1
print(func(s,lift,right))

    