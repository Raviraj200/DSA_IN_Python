class Node:
    def __init__(self,prv = None , data = None, next = None):
        self.data = data
        self.next = None
        self.prv = None

class Doubly_Linked_List:
    def __init__(self,head=None):
        self.head= head

    def is_empty(self):
        return self.head==None
# *************************************************************************
    def Insert_First(self, data): 
        new_Node = Node(None, data, self.head)
        if not self.is_empty():
            self.head.prv =new_Node
        self.head = new_Node

# *****************************************************************************
    def Insert_Last(self, data):
        curr = self.head
        if self.is_empty():
            curr = Node(None,data,None)
        while curr.next is not None:
            curr = curr.next
        new_Node = Node(curr, data, None)
        curr.next =new_Node
        new_Node = curr
# *****************************************************************************
    def Search(self,data):
        curr = self.head
        count =1
        if self.is_empty():
            return "List is Empty"
        while curr is not None:
            if curr.data == data:
                return count 
            curr = curr.next
            count = count +1
# **********************************************************************************
    def Insert_After(self,ele,data):
        if self.is_empty():
            return "list is empty"
        curr = self.head
        while curr.next != None:
            if curr.data == ele:
                break
            curr = curr.next
        new_Node = Node(curr,data,curr.next)
        curr.next=new_Node
        new_Node = curr
        
    


# ******************************************************************************
    def Print_All(self):
        curr = self.head
        if curr == None:
            return None

        while curr is not None:
            print(curr.data,end=",")
            curr = curr.next


List = Doubly_Linked_List()
List.Insert_First(20)
List.Insert_First(30)
List.Insert_First(30)
List.Insert_First(30)
List.Insert_Last(50)
List.Insert_Last(500)
List.Insert_Last(5335)
List.Insert_After(50,80)
List.Insert_After(80,6000)
print(List.Search(500))

List.Print_All()