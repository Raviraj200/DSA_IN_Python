class PriorityQueue:
    def __init__(self):
        self.list =[]

    def is_empty(self):
        return len(self.list)==0

    def Push(self,data,priority):
        index =0
        while len(self.list)>index and self.list[index][1] > priority:
            index+=1
        self.list.insert(index,(data,priority))
    
    def Pop(self):
        if self.is_empty():
            raise IndexError("List is Empty")
        return self.list.pop(0)[0]
    def size(self):
        return len(self.list)

p1 = PriorityQueue()
p1.Push(10,1)
p1.Push(20,2)
p1.Push(50,8)
print(p1.Pop())