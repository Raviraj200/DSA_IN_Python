class customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender = gender
        self.address=address

    def strr(self):
        print( "My name is ",self.name," Gender:",self.gender, "Address :",self.address.get_city(),"pin :",self.address.pincode," state:",self.address.state)

    def change_info(self,new_name, new_city, new_pin, new_state):
        self.name=new_name
        self.address.change_add(new_city,new_pin,new_state)    

class addresss:
    def __init__(self,city,pincode,state):
        self.__city=city
        self.pincode=pincode
        self.state=state

    def change_add(self,city,pin,state):
        self.__city=city
        self.pincode=pin
        self.state =state    

    def get_city(self):
        return self.__city    

add = addresss("sagar",407000,"MP")

cus = customer("Ravi","male",add)
cus.strr()
cus.change_info("Thakur","xyz",150242,"UP")
cus.strr()