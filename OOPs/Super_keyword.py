# class Phone:
#     def __init__(self,prince,brand):
#         self.price=prince
#         self.brand=brand
#     def buy(self):
#         print("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print("Buying a SmartPhone")
#         super().buy()

# pho = SmartPhone(20000, "Moto")
# pho.buy() 
# 
#        
# ****************************************************************************************


# class Phone:
#     def __init__(self,price, brand, camera):
#         self.price=price
#         self.brand=brand
#         self.camera = camera

# class SmartPhone(Phone):
#     def __init__(self,price,brand,camera,os,ram):
#         super().__init__(price,brand,camera)
#         self.os=os
#         self.ram=ram
        

# pho = SmartPhone(200,"moto","2Mp","osi",8)
# print(pho.os)    


# *****************************************************************************************


# class Parent:

#     def __init__(self,num):
#         self.__num =num
#     def get_num(self):
#         return self.__num
# class Child(Parent):

#     def __init__(self,num,val):
#         super().__init__(num)
#         self.__val=val
#     def get_val(self):
#         return  self.__val   

# son = Child(100, 20)
# print(son.get_num())
# print(son.get_val())


# *****************************************************************************************


# class Parent:
#     def __init__(self):
#         self.num =100
# class Chils(Parent):
#     def __init__(self):
#         super().__init__()
#         self.var=200

#     def show(self):
#         print(self.num)
#         print(self.var)    

# son = Chils()
# son.show()


# ***********************************************************************************************

class Parent:
    def __init__(self):
        self.__num=100
    def show(self):
        print("Parent",self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__val=10
    def show(self):
        print("child",self.__val)                

dad=Parent()
dad.show()

son=Child()
son.show()