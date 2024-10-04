class Cumtomer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
def greet(customer):
    if customer.gender=='male':
        print("Hello",customer.name,'sir')
    else:
        print("Hello",customer.name,"ma'am")



# Object
cust = Cumtomer("Raviraj Singh","male")            
greet(cust)
