class parent:
    def inComeParent(self):
        self.p_income=8000
        print("Parent income 80000")
class Child(parent):
    def inComeChild(self):
        print("Child income 6000 and Parent income",self.p_income)
class son(Child):
    def inCome(self):
        
        print("Son income 2000")

s= son()
s.inComeParent()
s.inComeChild()                      
s.inCome()  

