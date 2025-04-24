import sys
IN = float('inf')
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0]*num_vertices for _ in range(num_vertices)]
    def insert(self, v1, v2, value):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = value
            self.adj_matrix[v2][v1] = value
    def mindistance(self, dist, visited):
        min_val = IN
        min_index = -1
        for i in range(self.num_vertices):
            if dist[i] < min_val and not visited[i]:
                min_val = dist[i]
                min_index = i
        return min_index

    def Dijkstra(self, source):
        cost = self.adj_matrix
        dist = [IN] * self.num_vertices
        visited = [False] * self.num_vertices
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adj_matrix[i][j] == 0 and i != j:
                    cost[i][j] = IN
        dist[source] = 0  
        for i in range(self.num_vertices):
            u = self.mindistance(dist, visited)
            visited[u] = True
            for v in range(self.num_vertices):
                if cost[u][v] > 0 and  visited[v]==False and dist[u] +cost[u][v] <dist[v]:
                    dist[v] = dist[u] + cost[u][v]
        
        print(dist)
num_vertices = int(input("Enter the number of vertices (or nodes): "))  
g = Graph(num_vertices)
edge = int(input("Enter the number of edges: "))
for i in range(edge):
    src = int(input("Enter the source vertex: "))
    dest = int(input("Enter the destination vertex: "))
    weight = int(input("Enter the weight of the edge: "))
    g.insert(src, dest, weight)
source = int(input("Enter the source vertex: "))
g.Dijkstra(source)