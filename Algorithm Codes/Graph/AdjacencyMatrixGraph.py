from Graph import *
import heapq

class AdjacencyMatrixGraph(Graph):
    def __init__(self, nodes):
        self.n = nodes
        self.matrix = [[0 for j in range(self.n)] for i in range(self.n)]
    
    def __init(self, nodes, edges):
        self.__init__(nodes)
        for ((u, v), w) in edges:
            self.matrix[u][v] = w
            self.matrix[v][u] = w
    
    def add_edge(self, edge):
        ((u, v), w) = edge
        self.matrix[u][v] = w
        self.matrix[v][u] = w
    
    def remove_edge(self, edge):
        (u, v) = edge
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def dijkstra(self, start, end):
        visited = [False for i in range(n)]
        in_heap = [False for i in range(n)]

        heap = []
        heapq.heappush(heap, (0, start))
        in_heap[start] = True

        while(heap):
            (path_len, u) = heapq.heappop(heap)
            in_heap[u] = False
            visited[u] = True
            if(u == end):
                return path_len
            for i in range(self.n):
                if(self.matrix[u][i] > 0 and not(visited[i]) and not(in_heap[i])):
                    heapq.heappush(heap, (path_len + self.matrix[u][i], i))
                    in_heap[i] = True
        
        return None

    



