class Graph:
    def __init__(self):
        self.adjlist={}

    def insert(self,v1,v2):
        if v1 in self.adjlist:
            self.adjlist[v1].append(v2)
        else:
            self.adjlist[v1]=[v2]
        if v2 in self.adjlist:
            self.adjlist[v2].append(v1)
        else:
            self.adjlist[v2]=[v1]
        print()
        print(self.adjlist)
    def delete(self,v1,v2):
        if v1 in self.adjlist:
            if v2 in self.adjlist[v1]:
                self.adjlist[v1].delete(v2)

    
    def Display(self):
        for v1,v2  in self.adjlist.items():
            print(v1, "->",v2)



obj=Graph()
obj.insert(0,1)
obj.insert(0,2)
obj.insert(1,3)
obj.insert(3,2)
obj.insert(2,0)
print("After the deletion: ")
obj.delete()
obj.Display
