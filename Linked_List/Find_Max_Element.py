class Linked:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
        self.n=0

    def insertEle(self,Element):
        new_node=Linked(Element)
        new_node.next=self.head
        self.head = new_node
        self.n+=1
    def traverse(self):
        curr =self.head
        result=''
        while curr!=None:
            if self.MaxElement()==curr.data:
                curr.data=440

            result = result+str(curr.data)+'->'
            curr=curr.next 
            self.n+=1   
        return result[:-2] 

    def MaxElement(self):
        curr = self.head
        while curr!=None:
            if curr.data >curr.next.data:
                return curr.data
            curr=curr.next
            self.n+=1    


list = Linked_List()
list.insertEle(20)
list.insertEle(35000)
list.insertEle(1000)
list.insertEle(50)
print(list.traverse())
# print("Max Element in the List :",list.MaxElement())
