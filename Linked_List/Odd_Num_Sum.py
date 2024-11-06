class Node:
    def __init__(self,data=None):
        self.data=data
        self.next = None
class Linked:
    def __init__(self):
        self.head=None
        self.n=0

    def insert(self,Element):
        new_node=Node(Element)
        new_node.next=self.head
        self.head=new_node
        self.n+=1            

    def traverse(self):
        curr =self.head
        result=''
        while curr!=None:
           
            result = result+str(curr.data)+'->'
            curr=curr.next 
            self.n+=1  
            
        return result[:-2] 


    def OddSum(self):
        curr = self.head
        count=0
        while curr!=None:
            if curr.data%2==0:
                count = count+curr.data
                curr=curr.next
            else:
                curr =curr.next

        return count



list=Linked()
list.insert(10)
list.insert(20)
list.insert(300)
list.insert(3)
list.insert(2)
list.insert(5)
print(list.OddSum())
print(list.traverse())

