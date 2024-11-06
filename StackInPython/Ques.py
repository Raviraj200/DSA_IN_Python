class Node:
    def __init__(self,data=None):

        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top==None

    def push(self,data):
        new_node = Node(data)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isEmpty()==None:
            return "Stack is Empty"
        self.top=self.top.next
   
    def travel(self):
        if self.isEmpty()==None:
            return "Stack is Empty"
        temp = self.top
        while temp!=None:
            print(temp.data)
            temp = temp.next
    
    def Ques(self,text):
        q=Stack()
        for i in text:
            if i=='['or'('or'{':
                q.push(i)
            if i==']'or ')' or '}':
                q.pop()
        if self.isEmpty()==None:
            print("True")
        else:
            print("False")                
       

s=Stack()

s.push(10)
s.push(20)
s.push(30)
s.pop()
s.Ques('[82*{}}}]')

# s.travel()

    
 