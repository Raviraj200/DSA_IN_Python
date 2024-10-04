class Cumtomer2:
    def __init__(self,name,age):
        self.name=name
        self.age=age

cum=Cumtomer2("ravi",22)
cum1=Cumtomer2("Raj",13)
cum2=Cumtomer2("Singh",15)

l=[cum,cum1,cum2]
for i in l:
    print(i.name,i.age)