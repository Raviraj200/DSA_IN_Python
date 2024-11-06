class Node:
    def __init__(self, data=None):
        self.data= data
        self.next = None
class Linked:
    def __init__(self):
        self.head= None
        self.n=0        

    def insert(self,Element):
        new_node = Node(Element)
        new_node.next = self.head
        self.head=new_node
        self.n+=1  
    def reverse(self):
        pre_node =None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next=pre_node
            pre_node=curr_node
            curr_node=next_node
        self.head=pre_node        

    def travel(self):
        curr = self.head
        s=''
        while curr!=None:
            s=s+str(curr.data)+'->'
            curr=curr.next  
        return s[:-2]       
   







list =Linked()
list.insert(10)        
list.insert(20)        
list.insert(30)        
list.insert(40)        
list.insert(50)   
# print(list.n)

list.reverse()
print(list.travel())
    