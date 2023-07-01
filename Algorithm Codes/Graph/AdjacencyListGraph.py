from Graph import *
import heapq

class ListNode:
    def __init__(self, node=0, weight=0):
        self.node = node
        self.weight = weight
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, node, weight):
        if(self.head == None):
            self.head = ListNode(node, weight)
        else:
            new_head = ListNode(node, weight)
            new_head.next = self.head
            self.head = new_head
    
    def remove(self, node):
        dummy = ListNode()
        dummy.next = self.head

        prev = dummy
        curr = self.head

        while(curr != None):
            if(curr.node == node):
                prev.next = curr.next
                break
            prev = prev.next
            curr = curr.next
        
        self.head = dummy.next
    
    def to_list(self):
        res = []
        curr = self.head
        while(curr != None):
            res.append((curr.node, curr.weight))
            curr = curr.next
        return res
'''
a = LinkedList()
print(a.to_list())
a.add(1,4)
print(a.to_list())
a.add(2,4)
print(a.to_list())
a.remove(2)
print(a.to_list())
a.add(2, 5)
print(a.to_list())
a.remove(1)
print(a.to_list())
a.add(3,5)
a.add(4,5)
print(a.to_list())
a.remove(3)
print(a.to_list())
'''

class AdjacencyListGraph(Graph):
    def __init__(self, nodes, edges=[], is_directed=False):
        self.n = nodes
        self.adj = [LinkedList() for i in range(self.n)]
        self.is_directed = is_directed

        for ((u, v), w) in edges:
            self.adj[u].add(v, w)
            if not self.is_directed:
                self.adj[v].add(u, w)
    
    def add_edge(self, edge):
        ((u, v), w) = edge
        self.adj[u].add(v, w)
        if not self.is_directed:
            self.adj[v].add(u, w)

    def remove_edge(self, edge):
        ((u, v), _ ) = edge
        self.adj[u].remove(v)
        if not self.is_directed:
            self.adj[v].remove(u)
    
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

            curr = self.adj[u].head
            while(curr != None):
                new_path_len = dist[u] + curr.weight
                if(new_path_len < dist[curr.node]):
                    dist[curr.node] = new_path_len
                    prev[curr.node] = u
                    heapq.heappush(heap, (dist[curr.node], curr.node))
                curr = curr.next

        return (dist, prev)

nodes = 6
edges = [((0,1), 3), ((0,2), 8), ((1,2), 5), ((1,3), 6), ((2,3), 3), ((2,4), 2), ((3,4), 1), ((3,5), 9), ((4,5), 3)]

graph = AdjacencyListGraph(nodes, edges)
print(graph.dijkstra(0))
        