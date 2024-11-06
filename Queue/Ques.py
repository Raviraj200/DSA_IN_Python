# class Node:
#     def __init__(self,data=None):
#         self.data =data
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.front=None
#         self.rear=None

#     def inQueu(self,data):
#         new_node = Node(data)

#         if self.front==None:
#             self.front=new_node
#             self.rear=self.front
#         else:
#             self.rear.next = new_node
#             self.rear=new_node   

#     def deQueue(self):
#         if self.front==None:
#             return 'Empty'
#         else:
#             self.front=self.front.next

#     def traverse(self):
#         if self.rear==None:
#             return 'Empty'
#         temp = self.front
#         while temp !=None:
#             print(temp.data,' ',end='')
#             temp=temp.next

#     def twoStack(self):
        
# d=Queue()
# d.inQueu(10)
# d.inQueu(20)
# d.inQueu(300)

# d.traverse()


class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
class Stack:
    def __init__(self):
        self.top=None
    
    def isEmpty(self):
        return self.top==None

    def insert(self,data):
        new_node = Node(data)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isEmpty()==None:
            return 
        self.top=self.top.next 
    def traverse(self):
        if self.isEmpty()==None:
            return 'Empty'
        temp = self.top
        while temp!=None:
            print(temp.data)
            temp=temp.next
  
        


        
# s=Stack()
# s.insert(10)
# s.insert(20)
# s.insert(30)
# s.insert(40)
# s.traverse()
# s.pop()
# s.pop()
# s.traverse()


