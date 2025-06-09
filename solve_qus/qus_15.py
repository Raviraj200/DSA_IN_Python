class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def solve(self,a,b):
        des={}
        l=[]
        j=0
        for i in range(0,len(a)):
            des[j]=a[i]
            j+=1
        for i in range(0,len(b)):
            if b[i] not in des:
  
                des[j]=b[i]
                j+=1
        for i in range(0,len(des)):
            l[i]=des[i]
        return l    
            
    def findUnion(self,a,b):
        res = self.solve(a,b)
        return res
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]    
find =Solution()
print(find.findUnion(a,b))