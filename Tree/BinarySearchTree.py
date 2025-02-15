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

b1 = BinarySearchTree()
b1.Insert(10)
b1.Insert(20)
b1.Insert(5)
print(b1.search(10))
print(b1.preOrder())
print(b1.inOrder())
print(b1.posOrder())