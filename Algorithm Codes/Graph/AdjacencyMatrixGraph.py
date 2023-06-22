from Graph import *
import heapq

class AdjacencyMatrixGraph(Graph):
    def __init__(self, nodes, edges=None, is_directed=False):
        self.n = nodes
        self.matrix = [[0 for j in range(self.n)] for i in range(self.n)]
        self.is_directed = is_directed

        if(edges != None):
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
        (u, v) = edge
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
        
        if(prev[start] != None):
            return None
        
        return (dist, prev)


nodes = 6
edges = [((0,1), 3), ((0,2), 8), ((1,2), 5), ((1,3), 6), ((2,3), 3), ((2,4), 2), ((3,4), 1), ((3,5), 9), ((4,5), 3)]

graph = AdjacencyMatrixGraph(nodes, edges)
print(graph.dijkstra(0))


graph3 = AdjacencyMatrixGraph(5, [((0, 1), 4), ((0, 2), 2), ((1, 3), -1), ((2, 3), 3), ((2, 4), 5), ((3, 4), 2)], True)
graph4 = AdjacencyMatrixGraph(4, [((0, 1), 3), ((0, 2), 2), ((1, 2), -2), ((1, 3), 4), ((2, 3), 1)], True)
graph5 = AdjacencyMatrixGraph(3, [((0, 1), 1), ((1, 2), -1), ((2, 0), -2)], True)

print(graph3.bellman_ford(0))
print(graph4.bellman_ford(0))
print(graph5.bellman_ford(0))


    



