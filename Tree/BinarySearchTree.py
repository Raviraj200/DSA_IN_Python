class Node:
    def __init__(self, data =None, r=None,l=None):
        self.data=data
        self.r=r
        self.l=l
class BinarySearchTree:
    def __init__(self):
        self.root =None         

    def Insert(self, data):
        self.root = self.Rinsert(self.root,data)

    def Rinsert(self, root , data):
        if root is None:
            return Node(data)
        if data< root.data:
            root.l =self.Rinsert(root.l , data)
        elif data > root.data:
            root.r = self.Rinsert(root.r, data)
        elif data ==root.data:
            raise IndexError("This value is Already insert in Tree")    
        return root            

    def search(self,data):
        return self.Rsearch(self.root,data)
    def Rsearch(self, root,data):
        if root is None or root.data == data:
            return root
        elif root.data > data:
            return self.Rsearch(root.l, data)
        else :
            return self.Rinsert(root.r,data)
    

    def inOrder(self):
        result =[]
        self.Rinorder(self.root,result)
        return result
    def Rinorder(self,root, result):
        if root:
            self.Rinorder(root.l,result)
            result.append(root.data)
            self.Rinorder(root.r,result)   

    def preOrder(self):
        result =[]
        self.Rpreorder(self.root,result)
        return result
    def Rpreorder(self,root, result):
        if root:
            result.append(root.data)
            self.Rpreorder(root.l,result)
            self.Rpreorder(root.r,result)     

    def posOrder(self):
        result =[]
        self.Rposorder(self.root,result)
        return result
    def Rposorder(self,root, result):
        if root:
            self.Rposorder(root.l,result)
            self.Rposorder(root.r,result)              
            result.append(root.data)

    def MinEle(self,root):
        curr = root
        while curr.l != None:
            curr = curr.l
        return curr.data    
    
    def MixEle(self):
        curr =self.root
        while curr.r != None:
            curr =curr.r
        return curr.data    



    def delete(self,data):
        self.root = self.Rdelete(self.root , data)
    def Rdelete(self,root,data):
        if root == None:
            return None
        if root.data > data:
            root.l = self.Rdelete(root.l,data)
        elif root.data<data:
            root.r = self.Rdelete(root.r,data)
        else:
            if root.r is None:
                return root.l
            elif root.l is None:
                return root.r
            root.data = self.MinEle(root.r)
            self.Rdelete(root.r, root.data)
        return root   

b1 = BinarySearchTree()
b1.Insert(10)
b1.Insert(20)
b1.Insert(5)
print(b1.search(10))
print(b1.preOrder())
b1.delete(5)
print(b1.preOrder())