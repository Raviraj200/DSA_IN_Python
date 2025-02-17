class Graphs:
    def __init__(self , v_no):
        self.verdex_count = v_no
        self.list = [[0]*v_no for i in range(v_no)]

    def add(self, u, v, weithg =1):
        if 0<=u<self.verdex_count and 0<=v<self.verdex_count:
            self.list[u][v] =weithg
            self.list[v][u] =weithg
        else:
            raise IndexError("Not Founde")

    def remove(self, u, v):
        if 0<=u<self.verdex_count and 0<=v<self.verdex_count:
            list[u][v]=0
            list[v][u]=0

    def Find_ele(self , u,v):
        if 0<=u<self.verdex_count and 0<=v<self.verdex_count:
            if list[u][v]  != 0:
                return 1 

    def print_all(self):
        for i in range(self.verdex_count):
            for j in range(self.verdex_count):
                print(self.list[i][j],end=" ")

            print("\n")

g1 =Graphs(5)
g1.add(0,1)
g1.add(1,2)
g1.add(2,4)
g1.add(3,4)
g1.print_all()