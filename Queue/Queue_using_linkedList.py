class Node:
    def __init__(self, item=None, next = None):
        self.item =item
        self.next =next
class Queue:
    def __init__(self):
        self.front =None
        self.rear =None
        self.count =0
    def is_empty(self):
        return self.front==None
    def enQueue(self,data):
        new_Node =Node(data)
        if self.is_empty():
            self.front=new_Node
        else:
            self.rear.next =new_Node
        self.rear=new_Node

    def deQueue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else :
            self.front = self.front.next

        self.count-=1

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        raise IndexError("Queue in Empty")

    def get_Rear(self):
        if not self.is_empty():
            return self.rear.item

        raise IndexError("Queue is Empty")

q1 =Queue()
q1.enQueue(10)
q1.enQueue(20)
print(q1.get_front())
print(q1.get_Rear())


