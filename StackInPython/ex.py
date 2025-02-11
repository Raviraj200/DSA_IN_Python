class Node :
    def __init__(self, data):
        self.data= data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_Empty(self):
        return self.top==None

    def Push(self, data):
        new_Node = Node(data)
        new_Node.next = self.top
        self.top = new_Node
    
    def pop(self):
        if self.is_Empty():
            return 
        else:
            data = self.top.next.data
            self.top = self.top.next
            print(data)    
    def peek(self):
        if self.is_Empty():
            return None
        else:
            print(self.top.data)    
    def Print(self):
        curr = self.top

        if self.is_Empty():
            return None
        else:
            while curr is not None:
                print(curr.data, end=",")
                curr= curr.next
MyStack = Stack()
MyStack.Push(10)
MyStack.Push(20)
MyStack.Push(30)
MyStack.Push(40)
MyStack.Push(50)

MyStack.Print()
print("\n")     
MyStack.pop()
MyStack.Print()
MyStack.pop()
MyStack.Print()
MyStack.peek()                  

