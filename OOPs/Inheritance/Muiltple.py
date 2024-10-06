class Phone:
    def __init__(self,prince,brand,camera):

        print("inside phone")
        self.__price = prince
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a phone",self.brand)

class Product:
    def review(self):
        print("customer review")

class SmartPhone(Phone,Product):
    pass        

obj = SmartPhone(20000, 'Apple',"3MP")
obj.buy()