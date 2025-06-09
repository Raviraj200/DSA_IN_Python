# def sum(count,n):
#     if n==1:
#         return
#     sum(count+n,n-1)
#     print(count)
# sum(0,5)
# ************************************************************************

# def func(n):
#     if n==1:
#         return 1
    
#     return n*func(n-1)
# print(func(5))
# **********************************************************************

# def func(sun,n):
#     if n==1:
#         return 1
#     sun = sun*n
#     print(sun)
#     func(sun,n-1)
# func(1,5)    

# **************************************************************************
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
print(factorial(5))