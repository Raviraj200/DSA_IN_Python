class Cumtomer:
    def __init__(self,name,gender,add):
        self.name=name
        self.gender=gender
        self.add=add
    def edge_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.add.Change_Address(new_city,new_pin,new_state)
class Address:
    def __init__(self,city,pin,state):
        self.city=city
        self.pin=pin
        self.state=state
    def Change_Address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pin=new_pin
        self.state=new_state    
add=Address("sager",470335,"MP")

cust = Cumtomer("Ravi","male",add)
cust.edge_profile("Raj","banda",500,"UP")
print(cust.add.pin)