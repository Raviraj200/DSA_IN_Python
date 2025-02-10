class Node:
    def __init__(self, item = None, Next=None):
        self.item = item
        self.Next = Next

class CLL:
    def __init__(self):
        self.last = None

    def is_empty(self):
        return self.last==None    

    def Insert_At_First(self, data):
        new_Node = Node(data)
        if self.is_empty():
            new_Node.Next = new_Node
            self.last=new_Node
        else:
            new_Node.Next = self.last.Next
            self.last.Next = new_Node

    def Insert_at_Last(self,data):
        new_Node = Node(data)
        if self.is_empty():
            new_Node.Next=new_Node
            self.last=new_Node
        else:
            new_Node.Next = self.last.Next    
            self.last.Next = new_Node
            self.last = new_Node

    def Search(self, data):
        if self.is_empty():
            return None
        temp = self.last.Next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.Next
        if temp.item == data:
            return temp
        return None    

    def Print_All(self):
        curr = self.last.Next
        if self.is_empty():
            return None
        while curr != self.last:
            print(curr.item, end=",")
            curr = curr.Next 
        print(curr.item)       

    def Insert_after(self, ele, data):
        if ele is not None:
            new_Node=Node(data,ele.Next)
            ele.Next = new_Node
            if ele==self.last:
                self.last=new_Node

    def delete_last(self):
        if not self.is_empty():
            if self.last.Next== self.last:
                self.last=None
            else:
                temp = self.last.Next
                while temp.Next != self.last:
                    temp = temp.Next 
                temp.Next = self.last.Next
                self.last=temp                                         

    def delete_item(self,data):
        if self.is_empty():
            return None
        if self.last.Next == self.last:
            if self.last.item == data:
                self.last = None
        else:
            if self.last.Next.item==data:
                self.last.Next=self.last.Next.Next
                self.last.Next=None
            else: 
                curr = self.last.Next
                while curr!=self.last:
                    if curr.Next == self.last:
                        if self.last.item==data:
                            self.delete_last()
                        break

                    if curr.Next.item == data:
                        curr.Next = curr.Next.Next 
                        break
                    curr= curr.Next
                 



MYList = CLL()

MYList.Insert_At_First(10)
MYList.Insert_At_First(20)

MYList.Insert_At_First(30)
MYList.Insert_At_First(40)
MYList.Insert_at_Last(5)
print(MYList.Search(10))
MYList.Print_All()
MYList.Insert_after(MYList.Search(20),50)

MYList.Print_All()

