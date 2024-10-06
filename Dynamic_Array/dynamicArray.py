import ctypes
class MyList:
    
    def __init__(self):
        self.size=1
        self.n=0
        # create a C type Array with size =self.size
        self.A=self.__make_array(self.size)

    def __len__(self):
        return self.n    

    def __str__(self):
        result =''
        for i in range(self.n):
            result+= str(self.A[i]) + ','  
        return '['+result[:-1]+']'    

    def __getitem__(self,index):
        if 0<= index <self.n:
                return self.A[index]
        else:
            return "Index out of Range"        
      
    def find(self,item):
        for i in range(self.__len__()):
            if self.A[i]==item:
                return i
        return "ValueError"
         

    def __make_array(self,capacity):
        # create a c type arrya(static, referential) eith size capacity
        return (capacity*ctypes.py_object)() 

    def pop(self):
        if self.n==0:
            return "array is empty"
        else:    
            self.n=self.n-1
    
    def clear(self):
        self.n=0
        self.size=1

    def append(self,item):
        if self.n==self.size:
            self.__resize(self.size*2)
        
        self.A[self.n]=item
        self.n=self.n+1

    def __resize(self,new_capacity):
        B=self.__make_array(new_capacity)
        self.size=new_capacity

        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B  

    def insert(self,index,item):
        if self.n==self.size:
            self.__resize(self.size*2)

        for i in range(self.n,index,-1):
            self.A[i]=self.A[i-1]
        self.A[index]=item
        self.n=self.n+1  
    def delete(self,index):
          if 0<=index <self.n:
                # self.A[index]=''
                for i in range(index,self.n-1):
                    self.A[i]=self.A[i+1]
                self.n-=1

    def remove(self,item):
        pos = self.find(item)
        if type(pos)==int:
            self.delete(pos)
        else:
            return pos    





list = MyList()
list.append('a')
list.append('b')
list.append(50)
list.append(80)
list.remove('b')
list.delete(3)
list.insert(2,90)
print(list.find('a'))
list.clear()
list.pop()
print(list)