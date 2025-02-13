class Deque:
    def __init__(self):
        self.list=[]

    def is_empty(self):
        return len(self.list)==0

    def Insert_Start(self,data):
        self.list.insert(0,data)

    def Insert_Last(self,data):
        self.list.insert(-1,data)

    def Remove_start(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            self.list.pop(0)

    def Remove_Last(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            self.list.pop(-1)

    def get_Start(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.list[0]

    def get_Last(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.list[-1]
d1 = Deque()

d1.Insert_Start(10)
d1.Insert_Last(10)
d1.Insert_Start(20)
d1.Insert_Start(30)
d1.Insert_Start(40)
d1.Remove_start()
print(d1.get_Start())
