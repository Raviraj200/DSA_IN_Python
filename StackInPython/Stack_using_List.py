class Stack:
    def __init__(self):
        self.items= []

    def is_empty(self):
        return len(self.items)==0 

    def Push(self, data):
        self.items.append(data)

    def Pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")

    def Peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    
    def Size(self):
        return len(self.items)

s1 = Stack()
s1.Push(10)
s1.Push(20)
s1.Push(30)
print(s1.Size())
s1.Pop()
print(s1.Pop())
