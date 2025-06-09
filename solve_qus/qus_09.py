s="azyxyyzaaaa"
q=["a","a","y","x"]

Hash_list =[0]*26

for ch in s:
    ascii_val=ord(ch)
    index = ascii_val-97
    Hash_list[index]+=1

for ch in q:
    ascii_val = ord(ch)
    index=ascii_val-97
    print( ch," ",  Hash_list[index])


