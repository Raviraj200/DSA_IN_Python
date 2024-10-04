# Method OverRinding ->PloymorPhism

# class Phone:
#     def __init__(self, price,brand, camera):
#         self.__price = price
#         self.banda=brand
#         self.camera = camera
#     def buy(self):
#         print("Buying a Phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print("Buying a SmartPhone")

# s=SmartPhone(2000, "Moto","5MP")
# s.buy()        
# 
# 
# ************************************************************************************************


# class Parent:
#     def __init__(self,num):
#         self.__num=num

#     def get_num(self):
#         return self.__num    
# class Child(Parent):
#     def show(self):
#         print("this is in child class")        

# son = Child(100)
# print(son.get_num())
# son.show()        

# ***************************************************************************************************************

# class Parent:
#     def __init__(self,val,num):
#         print("i am parent")
#         self.__num=num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def __init__(self,val,num):
#         print("i am a child")

#         self.__val=val

#     def get_val(self):
#         return self.__val

# son = Child(100,10)
# print("Parent Number", son.get_val())        
