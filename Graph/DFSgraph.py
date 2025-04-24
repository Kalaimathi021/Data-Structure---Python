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
            if len(v2)==0:
                continue
            print(v1, "->",v2)

    def DFS(self,src):
        visited = set()
        stack = [src]
        while stack:
            temp=stack.pop()
            if temp not in visited:
                print(temp)
                visited.add(temp)
                if temp in self.adjlist:
                    for i in self.adjlist[temp]:
                        if i not in visited:
                            stack.append(i)
                        





obj=Graph()
obj.insert(0,1)
obj.insert(0,2)
obj.insert(1,4)
obj.insert(2,4)
obj.insert(1,3)
obj.insert(4,3)
obj.Display
 