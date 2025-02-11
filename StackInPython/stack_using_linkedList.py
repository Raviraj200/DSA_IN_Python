class Node:
    def __init__(self, data=None, next=None):
        self.data= data
        self.next = next

class Stack:
    def __init__(self):
        self.start = None
        self.count = 0
    def is_empty(self):
        return self.start==None

    def Push(self, data):
        new_Node = Node(data,self.start)

        self.start= new_Node
        self.count = self.count+1

    def Pop(self):
        if self.start!=None:
            data= self.start.data
            self.start = self.start.next
            self.count = self.count-1
            return data
        else:
            raise IndexError("Empty")    

    def Peep(self):
        if self.start != None:
            return self.start.data
        else:
            raise IndexError("Empty")

    def Size(self):
        return self.count

s1 = Stack()
s1.Push(10)
s1.Push(20)
s1.Push(30)
print(s1.Peep())
print(s1.Size())