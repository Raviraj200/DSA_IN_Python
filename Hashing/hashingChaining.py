class Node:
    def __init__(self,key,value):
        self.key = key
        self.value= value
        self.next = None
class LL:
    def __init__(self):
        self.head = None

    def add(self,key, value):
        new_node = Node(key,value)
        if self.head==None:
            self.head = new_node
        else:
            temp =self.head

            while temp.next!=None:
                temp = temp.next  
            temp.next =new_node


    def remove(self,key):
        if self.head.key==key:
            self.delete_head()
            return                  
        if self.head ==None:
            return "Empty"
        else:
            temp  = self.head   

            while temp.next != None:
                if temp.next.key==key:
                    break
                temp= temp.next

            if temp.next==None:
                return "Not found"
            else:
                temp.next= temp.next.next     

    def traverse(self):
        temp =self.head

        while temp != None:
            print(temp.key,"-->",temp.value," ")
            temp = temp.next                    


    def size(self):
        temp = self.head
        counter = 0

        while temp != None:
            counter +=1
            temp=temp.next
        return counter    


    def search(self,key):
        temp = self.head
        pos=0
        while temp!=None:
            if  temp.key == key:
                return pos
            temp = temp.next
            pos+=1
        return -1    

    def get_node_at_index(self,index):
        temp = self.head
        counter =0
        
        while temp is not None:
            if counter == index:
                return temp
            temp = temp.next
            counter+=1    

class Dictionary:
    def __init__(self,capacity):

        self.capacity= capacity
        self.size=0
        # create array of LL
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        L=[]
        for i in range(capacity):
            L.append(LL())
        return L    

    def put(self,key ,value):
        bucket_index = self.hash_function(key)
        node_index = self.get_node_index(bucket_index,key)

        if node_index ==-1:
            # insert 
            self.buckets[bucket_index].add(key,value)
            self.size+=1
            load_factor  =self.size/self.capacity
            print(load_factor)

            if self.size/self.capacity >= 2:
                self.rehash()
        else:
            # update     
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value =value


    def rehash(self):
        self.capacity=self.capacity*2
        old_buckets= self.buckets
        self.size =0
        self.buckets= self.make_array(self.capacity)

        for i in old_buckets:
            for j in range(i.size()):
                node = i.get_node_at_index(j)
                key_item = node.key
                value_item = node.value
                self.put(key_item,value_item)


    def get_node_index(self,bucket_index, key):
        node_index=self.buckets[bucket_index].search(key)
        return node_index

    def hash_function(self,key):
        return abs(hash(key)) % self.capacity            

L =LL()
L.add(2,3)
L.add(3,4)
L.add(4,5)
L.traverse()     
print("Index=",L.get_node_at_index(0).key)

d1 = Dictionary(4)
d1.put("python",10)
d1.put("c++",30)
d1.put("java",50)
d1.put("dcd",5)
d1.put("kjvnv",80)
d1.put("jvxj",100)
d1.put("c c ",302)
d1.put("knkk",60)

print("cheks",d1.buckets[0].traverse())
