class Phone:
    def buy(self):
        print("Inside the Phone")
class SmartPhone:
    def buy(self):
        print("Inside the SmartPhone")

            # MRO
class both(SmartPhone,Phone):
    pass   

obj = both()
obj.buy()