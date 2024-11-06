
class Node:
    def __init__(self,value=None):
        self.data = value
        self.next =None

class Linked:
    def __init__(self):
        self.head=None
        self.n=0
    def __len__(self):
        return self.next

    # inset in head  ***************************************************  
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next=self.head
        self.head=new_node
        self.n+=1
        

    # inset in end********************************************************
    def insert_end(self,value):
        new_node = Node(value)
        curr=self.head
        if curr==None:
            return 'Enpty list'
        if curr ==None:
            curr=new_node
            self.n+=1
            return

        while curr.next != None:
            curr=curr.next
        curr.next=new_node
        self.n+=1
        
        
        

    # insert_mid***********************************************************
    def insert_mid(self,IndexVal,value):
        new_node = Node(value)
        curr  = self.head
        
        while curr!=None:
            if curr.data==IndexVal:
                break
            curr=curr.next
           
        if curr!= None:
            new_node.next=curr.next
            curr.next=new_node
            self.n  = self.n +1
        else:
              print("Item not found")  
            
    # All Clear***********************************************************
    def clear(self):
        self.head=None
        self.n=0

    # clear head
    def clearHead(self):
        if self.head == None:
            return
        self.head =self.head.next   
        self.n = self.n-1 

    # clear End  **************************************************************
    def clearEnd(self):
        curr = self.head
        if curr.next ==None:
            self.clearHead()
            return
        while curr.next.next != None:
            curr=curr.next  
        curr.next=None    
        self.n -=1

    # clear in Index ***************************************************
    def clearIndex(self,IndexVal):
        curr = self.head
        while curr.next!= None:
            if curr.data==IndexVal:
                break
            curr=curr.next

        if curr.next ==None:
            return 'Not found'
        else:
            curr.next=curr.next.next
       
# search**************************************************************************
    def search(self,item):
        curr =self.head
        pos=0

        while curr!=None:
            if curr.data==item:
                return pos
            curr = curr.next
            pos = pos+1
        return 'NOt Found'   

# index pos************************************************************************
    def IndexPos(self,index):
        curr = self.head
        curIndexr=0

        while curr!=None:
            if curIndexr ==index:
                return curr.data
            curr=curr.next
            curIndexr=curIndexr+1
        return 'Index Error'            
        


  

    # traverse*************************************************************
    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data)+'->'
            curr = curr.next
        return result[:-2]    


list = Linked()
list.insert_head(50)
list.insert_head(40)
list.insert_head(30)
list.insert_head(20)
list.insert_end(100)

print(list.n)
# list.clearIndex(30)
# list.clear()
# list.clearEnd()
# list.insert_mid(30,800)


# print("Element",list.search(100))
print(list.IndexPos(0))
print(list)
