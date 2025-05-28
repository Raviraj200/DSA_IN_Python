# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left =None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root =None

#     def Insert(self,data):
#         self.root = self.Rinsert(self.root,data)
#     def Rinsert(self, root ,data):
#         if root is None:
#             return Node(data)
#         elif root.data > data:
#             root.left= self.Rinsert(root.left,data)
#         elif root.data<data:
#             root.right = self.Rinsert(root.right,data)
#         return root          

#     def Min_Ele(self,root):
#         curr = root 
#         while curr != None:
#             curr = curr.left
#         return curr

#     def delete(self, data):
#         self.root = self.Rdelete(self.root,data)
#     def Rdelete(self,root,data):
#         if root == None:
#             return None
#         if root.data>data:
#             root.left = self.Rdelete(root.left,data)
#         elif root.data<data:
#             root.right = self.Rdelete(root.right,data)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             else:
#                 root.data = self.Min_Ele(root.right)       
#                 self.Rdelete(root.right, root.data)
#             return root                                          
    
#     def posOrder(self):
#         result =[]
#         self.Rposorder(self.root,result)
#         return result
#     def Rposorder(self,root, result):
#         if root:
#             self.Rposorder(root.left,result)
#             self.Rposorder(root.right,result)              
#             result.append(root.data)

# b1= BST()
# b1.Insert(10)
# b1.Insert(20)
# b1.Insert(30)
# b1.Insert(5)
# b1.delete(10)
# print(b1.posOrder())

class Node:
    def __init__(self, v_no):
        self.vertex = v_no
        self.list ={v:[] for v in range(v_no) }
    def add(self,u,v,wight =1):
        if 0<=u<self.vertex or 0<=v<self.vertex:
            self.list[u].append((v,wight))
            self.list[v].append((u,wight))
        else:
            print("Not Founde")
    def print_All(self):
        for v,i in self.list.items():
            print("V",v,":",i )            

g=Node(5)
g.add(0,1)
g.add(1,2)
g.add(1,3)
g.add(2,4)
g.add(3,4)
g.print_All()