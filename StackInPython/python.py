class Node:
    def __init__(self,data=None):
        self.data=data 
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head==None    

    def Insert_First(self, data):
        new_Node = Node(data)
        new_Node.next=self.head
        self.head = new_Node
    
    def Insert_Last(self, data):
        new_Node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_Node

    def Insert_mid(self,ele, data):
        new_Node  = Node(data)
        curr = self.head

        while curr!=None:
            if curr.data==ele:
                break
            curr = curr.next

        if curr is not None:
             new_Node.next = curr.next
             curr.next = new_Node
          
    def PrinteAll(self):
        if self.head == None:
            return None
        while self.head is not None:
            print(self.head.data,"," ,end=" ")
            self.head = self.head.next

    def Delet_First(self):
        self.head = self.head.next
        return self.head

# myList = LinkedList()
# myList.Insert_First(20)
# myList.Insert_First(230)
# myList.Insert_First(230)
# myList.Insert_First(230)
# myList.Insert_First(100)
# myList.Insert_Last(500)
# myList.Insert_Last(3003200)
# myList.Insert_mid(100,5060)
# myList.Delet_First()

# myList.PrinteAll()

        
          


