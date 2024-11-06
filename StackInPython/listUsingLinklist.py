class Node:
    def __init__(self,size):
        self.size =size
        self.__stack = [None]*self.size
        self.top = -1
    def push(self,value):
        if self.top == self.size -1:
            return "OverFlow"
        else:
            self.top+=1 
            self.__stack[self.top]=value

    def pop(self):
        if self.top==-1:
            return 'List is OverFlow'
        else:
            data=self.__stack[self.top]
            self.top-=1
            # print(data) 

    def traverse(self):
        for i in range(self.top+1):
            print(self.__stack[i],'->',end='')
s=Node(3)
s.push(10)
s.push(20)
s.push(30)
# s.push(40)
s.traverse()
s.pop()
# print()

s.traverse()                