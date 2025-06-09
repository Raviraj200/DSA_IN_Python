def func(ele):
    if ele==0 or ele ==1:
        return ele
    return func(ele-1)+func(ele-2)

    
    



ele=[0,1,1,2,3,5,8,13,21,34]

print(func(6))

