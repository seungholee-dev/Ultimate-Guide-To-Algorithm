from Graph import *
import heapq

class AdjacencyMatrixGraph(Graph):
    def __init__(self, nodes, edges=[], is_directed=False):
        self.n = nodes
        self.matrix = [[0 for j in range(self.n)] for i in range(self.n)]
        self.is_directed = is_directed

        for ((u, v), w) in edges:
            self.matrix[u][v] = w
            if not self.is_directed:
                self.matrix[v][u] = w
    
    def add_edge(self, edge):
        ((u, v), w) = edge
        self.matrix[u][v] = w
        if not self.is_directed:
            self.matrix[v][u] = w
    
    def remove_edge(self, edge):
        ((u, v), _ ) = edge
        self.matrix[u][v] = 0
        if not self.is_directed:
            self.matrix[v][u] = w

    def dijkstra(self, start):
        dist = [float('inf') for i in range(self.n)]
        dist[start] = 0
        prev = [None for i in range(self.n)]
        visited = [False for i in range(self.n)]

        heap = []
        heapq.heappush(heap, (0, start))

        while(heap):
            (path_len, u) = heapq.heappop(heap)
            visited[u] = True
            for i in range(self.n):
                if(self.matrix[u][i] != 0 and not(visited[i])):
                    new_path_len = dist[u] + self.matrix[u][i]
                    if(new_path_len < dist[i]):
                        dist[i] = new_path_len
                        prev[i] = u
                        heapq.heappush(heap, (dist[i], i))
            
        return (dist, prev)
    
    def bellman_ford(self, start):
        dist = [float('inf') for i in range(self.n)]
        dist[start] = 0
        prev = [None for i in range(self.n)]

        edges = []
        for i in range(self.n):
            for j in range(self.n):
                if(self.matrix[i][j] != 0):
                    edges.append(((i,j), self.matrix[i][j]))

        for i in range(self.n-1):
            for ((u,v), w) in edges:
                if(w + dist[u] < dist[v]):
                    dist[v] = w + dist[u]
                    prev[v] = u
        
        if(prev[start] is not None):
            return None
        
        return (dist, prev)

    def floyd_warshall(self):
        dist = [[float('inf') for i in range(self.n)] for j in range(self.n)]

        for i in range(self.n):
            dist[i][i] = 0
            for j in range(self.n):
                if(self.matrix[i][j] != 0):
                    dist[i][j] = self.matrix[i][j]
            
        for k in range(self.n):
            for u in range(self.n):
                for v in range(self.n):
                    if(dist[u][v] > dist[u][k] + dist[k][v]):
                        dist[u][v] = dist[u][k] + dist[k][v]
        
        for i in range(self.n):
            if(dist[i][i] < 0):
                return None
            
        return dist

nodes = 6
edges = [((0,1), 3), ((0,2), 8), ((1,2), 5), ((1,3), 6), ((2,3), 3), ((2,4), 2), ((3,4), 1), ((3,5), 9), ((4,5), 3)]

graph = AdjacencyMatrixGraph(nodes, edges)
print(graph.dijkstra(0))


graph3 = AdjacencyMatrixGraph(5, [((0, 1), 4), ((0, 2), 2), ((1, 3), -1), ((2, 3), 3), ((2, 4), 5), ((3, 4), 2)], True)
graph4 = AdjacencyMatrixGraph(4, [((0, 1), 3), ((0, 2), 2), ((1, 2), -2), ((1, 3), 4), ((2, 3), 1)], True)
graph5 = AdjacencyMatrixGraph(3, [((0, 1), 1), ((1, 2), -1), ((2, 0), -2)], True)

print(graph3.bellman_ford(0))
print(graph3.floyd_warshall()[0])
print(graph4.bellman_ford(0))
print(graph4.floyd_warshall()[0])
print(graph5.bellman_ford(0))
print(graph5.floyd_warshall())



    



