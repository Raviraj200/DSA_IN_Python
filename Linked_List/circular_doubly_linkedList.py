class Node:
    def __init__(self,data, prv = None, next =None):
        self.data = data
        self.prv = prv
        self.next= next

class CDLL:
    def __init__(self):
        self.start = None


    def is_empty(self):
        return self.start==None

    def Insert_At_First(self,data):
        new_Node = Node(data)
        if self.is_empty():
            new_Node.next=new_Node
            new_Node.prv=new_Node
            self.start=new_Node
            
            
        else:
            new_Node.next = self.start
            new_Node.prv = self.start.prv
            self.start.prv.next = new_Node
            self.start.prv = new_Node
            self.start = new_Node    
       
    
    def Insert_At_Last(self,data):
        new_Node = Node(data)
        curr = self.start
        if self.is_empty():
            new_Node.next=new_Node
            new_Node.prv=new_Node
            curr= new_Node
        else:
            new_Node.next = curr
            new_Node.prv = curr.prv
            curr.prv.next = new_Node
            curr.prv = new_Node
            curr = new_Node    
                
    def search(self, data):
        curr = self.start
        if curr == None:
            return None
        if curr.data == data:
            return curr
        else:
            curr = curr.next

        while curr != self.start:
            if curr.data == data:
                return curr
            curr= curr.next
        return None

    def Insert_After(self, ele, data):
        if ele is not None:
            new_Node= Node(data)
            new_Node.next= ele.next
            new_Node.prv= ele  
            ele.next.prv = new_Node
            ele.next=new_Node
   

    def Print_All(self):
        curr = self.start
        if curr is not None:
            print(curr.data,end=" ")
            curr=curr.next
            while curr is not self.start:
                print(curr.data, end=" ")
                curr= curr.next
    
    def Delete_First(self):
    

        if self.start is not None:
            if self.start.next == self.start:
                self.start =None
            else:
                self.start.prv.next = self.start.next
                self.start.next.prv= self.start.prv
                self.start= self.start.next    

    def Delete_Last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start=None
            else:
                self.start.prv.prv.next = self.start
                self.start.prv= self.start.prv.prv                

    def Delete_After_Ele(self, ele):
        if ele== self.start.prv:
            self.Delete_Last()
            
        if ele == self.start:
            self.Delete_First()
        else:
            ele.prv.next = ele.next
            ele.next.prv = ele.prv       

MyList = CDLL()
MyList.Insert_At_First(10)
MyList.Insert_At_First(20)
MyList.Insert_At_First(30)
MyList.Insert_At_First(40)
MyList.Insert_At_Last(50)
MyList.Insert_After(MyList.search(30),90)
MyList.Print_All()
MyList.Delete_First()
# MyList.Delete_Last()
print(end="\n")
MyList.Print_All()
MyList.Delete_After_Ele(MyList.search(10))
print(end="\n")

MyList.Print_All()

            