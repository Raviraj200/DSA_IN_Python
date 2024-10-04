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


class Phone:
    def __init__(self,price, brand, camera):
        self.price=price
        self.brand=brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        

pho = SmartPhone(200,"moto","2Mp","osi",8)
print(pho.os)    