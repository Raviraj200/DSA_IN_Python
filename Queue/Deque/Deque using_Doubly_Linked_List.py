class Node:
    def __init__(self, data=None, prv=None, next=None):
        self.data=data
        self.prv=prv
        self.next=next
class Deque_Doubly_LinkedList:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count =0

    def is_empty(self):
        return self.front==None

    def Insert_front(self,data): 
        new_Node = Node(data,None,self.front)
        if self.is_empty():
            self.rear = new_Node
        else:
            self.front.prv=new_Node    
        self.front = new_Node

    def Insert_rear(self,data):
        new_Node= Node(data,self.rear)
        if self.is_empty():
            self.front=new_Node
        else:
            self.rear.next =new_Node
        self.rear = new_Node

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.front ==self.rear :
            self.front=Nones
            self.rear=None
        else:
            self.front = self.front.next
            self.front.prv =None

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")   
        elif self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prv
            self.rear.next=None                        

    def get_Front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")  
        return self.front.data    
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")  
        return self.rear.data

d1 = Deque_Doubly_LinkedList()
d1.Insert_front(10)
d1.Insert_front(20)
print(d1.get_Front())