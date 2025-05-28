class Heap:
    def __init__(self):
        self.heapList = []
    def CreateList(self,list):
        for i in list:
            self.insert(i)
    def insert(self,ele):
        Index = len(self.heapList)
        parentEle = (Index-1)//2

        while Index>0 and self.heapList[parentEle]<ele:
            if Index == len(self.heapList):
                self.heapList.append(self.heapList[parentEle])
            else:
                self.heapList[Index] = self.heapList[parentEle]
            Index = parentEle
            parentEle = (Index-1)//2
        if Index == len(self.heapList):
            self.heapList.append(ele)
        else:
            self.heapList[Index] = ele        

    def PrintAll(self):
        for i in self.heapList:
            print(i)                 

list = [40,70,10,90,60,30,50,20,80]
h=Heap()
h.CreateList(list)
h.PrintAll()