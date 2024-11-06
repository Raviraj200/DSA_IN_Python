class Node:
    def __init__(self,data=None):
        self.data=data
        self.next = None
class Stack:
    def __init__(self):
        self.top=None
    def  isEmpty(self):
        return self.top==None

    def push(self,ele):
        new_node = Node(ele)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isEmpty()==None:
            return 
        self.top=self.top.next                    
    def travel(self):
        if self.isEmpty()==None:
            return 
        temp = self.top
        while temp!=None:
            print(temp.data)
            temp=temp.next   

    def text_editor(text="Hello",paten="ururu"):
        u=Stack()
        r=Stack()
        
        for  i in text:
            u.push(i)

        for i in  paten:
            if i=='u':
                data = u.pop()
                r.push(data)
            else:
                data = r.pop()
                u.push(data)       
        res=""

        while(not u.isEmpty()):
            res = u.pop()+res  
        print(res)           

s=Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.travel()
s.text_editor("Hello","ur")
