from python import *

class Stack :
    def __init__(self):
        self.myList = LinkedList()
        self.count = 0
    def is_empty(self):
        return self.myList.is_empty()

    def Push(self, data):
        self.myList.Insert_First(data)
        self.count +=1

    def Pop(self):
        if not self.is_empty():
            data=self.myList.Delet_First()
            self.count-=1
            return data.data
           
        else:
            return IndexError("Empty")
    def Peep(self):
        if not self.is_empty():
            return self.myList.head.data
        else:
            return IndexError("Empty")        

s1 = Stack()

s1.Push(10)
s1.Push(20)
s1.Push(30)
s1.Push(40)
print(s1.Pop())
print(s1.Peep())



