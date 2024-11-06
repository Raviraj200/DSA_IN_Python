class Dictionary:

    def __init__(self,size):
        self.size=size
        self.slots=[None] * self.size
        self.data=[None] * self.size

    def put(self, key ,value):
        hash_value = self.hash_function(key)

        if self.slots[hash_value]==None:
            self.slots[hash_value]=key
            self.data[hash_value]=value
        else:
            if self.slots[hash_value]==key:
                self.data[hash_value]=value
            else:
                new_hash_value = self.rehash(hash_value)

                while self.slots[new_hash_value]!=None and self.slots[hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)

                    if self.slots[hash_value] == None:
                        self.slots[hash_value]=key
                        self.data[hash_value]=value
                    else:
                      self.data[new_hash_value] = value  

    
    def get(self,key):
        start_position = self.hash_function(key)
        curr_position = start_position

        while self.slots[curr_position] != None:
            if self.slots[curr_position]==key:
                return self.data[curr_position]

            curr_position=self.rehash(curr_position)

            if curr_position ==start_position:
                return "Not Found"    
        return "Not Found"    

    def __getitem__(self,key):
        return self.get(key)

    def rehash(self,old_hash):
        return (old_hash + 1) % self.size

    def hash_function(self,key): 
        key= abs(hash(key))
        return key%self.size    


    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i],":",self.data[i])
        return ""        



d= Dictionary(3)
d.put("raviji",28)
d.put("raj",20)
d.put("singh",10)
d.put("lodhi",30)

# print(d.get("raj"))
print(d)
print(d["raj"])
print(d.slots)
print(d.data )