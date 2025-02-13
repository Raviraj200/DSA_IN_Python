class Queue:
    def __init__(self):
        self.list = []
    
  
    def Insert(self,data):
        self.list.append(data)

    def Remove(self):
        if len(self.list)==0:
            return IndexError("Queue is Empty")
        else:
            resu = self.list.pop()
            return resu

    def get_first(self):
        if len(self.list)!=0:
            return self.list[0]
        else:
            return IndexError("Queue is Empty")

    def get_Last(self):
        if len(self.list)!=0:
            return self.list[-1]
        else:
            return IndexError("Queue is Empty")                        

q1 = Queue()
q1.Insert(10)
q1.Insert(20)
q1.Insert(30)
print(q1.list)

print(q1.get_first(), q1.get_Last())
