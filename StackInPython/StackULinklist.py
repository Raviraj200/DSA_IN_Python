class Node:
    def __init__(self,data=None):
        self.data=data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top ==None

    def push(self,data):
        new_node = Node(data)
        new_node.next= self.top
        self.top=new_node
    
    def pop(self):
        if self.isEmpty():
            return
        data=self.top.next.data 
        self.top = self.top.next
        return data
    def peek(self):
        if self.isEmpty():
            return "Stack Empty"
        else:
            return self.top.data 

    def travel(self):
        if self.isEmpty():
            return 
        temp = self.top
        while temp!=None:
            print(temp.data)
            temp = temp.next

    # def reversString():
    #     s=Stack()
    #     for i in "Hello":
    #         s.push(i)
    #     sting = ''

    #     while not s.isEmpty():
    #        sting= sting+s.pop()  
    #     print(sting)

s = Stack()