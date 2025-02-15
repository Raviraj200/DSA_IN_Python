class Node:
    def __init__(self , data=None, pro = None, next = None):
        self.data =data
        self.pro =pro
        self.next =next

class PriorityQueue:
    def __init__(self):
        self.start = None
        self.count =0
 
    def is_empty(self):
        return self.start==None

    def Push(self, data , pro):
        new_Node = Node(data, pro)
        if not self.start or pro <self.start.pro:
            new_Node.next = self.start
            self.start=new_Node
        else:
            curr = self.start
            while curr.next is not None and curr.next.pro <= pro:
                curr = curr.next
            new_Node.next = curr.next
            curr.next = new_Node

    def Pop(self):
        if self.is_empty() is not None:
            data = self.start.data
            self.start = self.start.next
            return data


p1 = PriorityQueue()
p1.Push(10,1)   
p1.Push(20,3)
p1.Push(40,0)  
print(p1.Pop())         

