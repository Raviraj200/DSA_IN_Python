class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
class Queue:
    def __init__(self):
        self.front =None
        self.rear = None

    def enqueue(self,value):
        new_node=Node(value)

        if self.rear==None:
            self.front=new_node
            self.rear=self.front
        else:
            self.rear.next=new_node
            self.rear=new_node 

    def dequeue(self):
        if self.front == None:
            return 'Empty'
        else:
            self.front = self.front.next    
    def traverse(self):
        if self.rear==None:
            return 'Queue is empty'

        temp = self.front    
        while temp !=None:
            print(temp.data,' ',end='')
            temp=temp.next
    def  size(self):
        temp = self.front
        count =0 

        while temp!=None:
            count+=1
            temp = temp.next
        return count   

    def front_item(self):
        if self.front ==None:

            return "empty"
        else:
            return self.front.data

    def rear_item(self):
        if self.front ==None:
            return "empty"
        else:
            return self.rear.data

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.traverse()


q.traverse()
print(q.size())
print(q.front_item())
print(q.rear_item())
