class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=Node
class Linked:
    def __init__(self):
        self.head=None
        self.n=0

    def insert(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.n+1

    def travel(self):
        curr = self.head
        s=''
        while curr!=None:
            s=s+str(curr.data)+'->'
            curr=curr.next  
        Linked.fun(self.head)    
        # self.fun(self.head)    f
        return s[:-2]  


                       

list = Linked()
list.insert(10)
list.insert(20)
list.insert(30)
list.insert(40)

print(list.travel())
