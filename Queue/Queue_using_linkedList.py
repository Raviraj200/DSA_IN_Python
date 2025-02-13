class Node:
    def __init__(self,data =None, next =None):
        self.data=data
        self.next=next

class Queue:
    def __init__(self):
        self.front =None
        self.reat=None
        self.count=0

    def is_empty(self):
        return self.front==None

    def enQueue(self,data):
        new_Node = Node(data)
        if self.is_empty():
            self.front = new_Node
        else:
            self.reat.next = new_Node
        self.reat=new_Node
        self.count+=1

    def deQueue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        elif self.front==self.reat:
            self.front=None
            self.reat=None
        else:
            self.front=self.front.next
        self.count-=1

    def get_front(self):
        if self.is_empty() is not None:
            return self.front.data
        else:
            raise IndexError("Queue is Empty")

    def get_rear(self):
        if self.is_empty() is not None:
            return self.reat.data
        else:
            raise IndexError("Queue is EMpty")                                    


q1 =Queue()
q1.enQueue(10)
q1.enQueue(20)
q1.enQueue(30)
print(q1.get_front())
print(q1.get_rear())


            