class Stack(list):
    def is_empty(self):
        return len(self)==0

    def Push(self,data):
        self.append(data)

    def Pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            return IndexError("Stack is Empty")

    def Peep(self):
        if not self.is_empty():
            return self[-1]       
        else:
            return IndexError("Stack is Empty")

    def Size(self):
        return len(self)
    
    def insert(self, index, data):
        return AttributeError("Not Attribute Insert ")

s1=Stack()
s1.Push(10)
s1.Push(20)
# s1.pop()
print(s1.insert(1,30))
print(s1.Peep())
print(s1.Size())
