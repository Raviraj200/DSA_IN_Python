class Heap:
    def __init__(self):
        self.heap=[]
    def CreateHeap(self,list):
        for i in list:
            self.insert(i)
    def insert(self,ele):
        index = len(self.heap)
        parenteEle = (index-1)//2
        while index>0 and self.heap[parenteEle]<ele:
            if index == len(self.heap):
                self.heap.append(self.heap[parenteEle])
            else:
                self.heap[index]=self.heap[parenteEle]
            index = parenteEle
            parenteEle = (index-1)//2
        if index == len(self.heap):
            self.heap.append(ele)
        else:
            self.heap[index]=ele 
    def TopEle(self):
        if self.heap==None:
            return "List is Empty"
        else:
            return self.heap[0]
    def PrintAll(self):
        for  i in self.heap:
            print(i)                       



list = [40,70,10,90,60,30,50,20,80]
c= Heap()
c.CreateHeap(list)
c.PrintAll()
print(c.TopEle())