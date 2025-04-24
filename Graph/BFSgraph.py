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

    def BFS(self,src):
        visited = set()
        queue =deque([src])
        visited.add(src)
        while queue:
            temp=queue.popleft()
            print(temp,end=" ")

            if temp in self.adjlist:
                for i in self.adjlist[temp]:
                    if i not in visited:
                        queue.add(i)
                        visited.add(i)





obj=Graph()
obj.insert(0,1)
obj.insert(0,2)
obj.insert(1,4)
obj.insert(2,4)
obj.insert(1,3)
obj.insert(4,3)
obj.Display
 