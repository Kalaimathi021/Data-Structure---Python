class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.matrix=[[0]*vertex for i in range(vertex)]

    def insert(self,src,dest):
        if 0 <= src <= vertex and 0 <= dest <= vertex:
            self.matrix[src][dest]=1
            self.matrix[dest][src]=1
        else:
            print("Invalid vertex number!")

    def delete(self,src,dest):
        if 0 <= src <= vertex and 0 <= dest <= vertex:
            self.matrix[src][dest]=0
            self.matrix[dest][src]=0
        else:
            print("Invalid vertex number!")

    def display(self):
        for i in range (self.vertex):
            for j in range(self.vertex):
                print(self.matrix[i][j],end=" ")
            print()

vertex=int(input("Enter the number of vertices: "))
obj=Graph(vertex)
edges=int(input("enter number of edges: "))
for i  in range(edges):
    src=int(input("Enter source: "))
    dest=int(input("enter the destination: "))
    obj.insert(src,dest)
    

obj.display()
obj.delete()
