---
title: Graph Representations
description: Learning Sliding Window
---

When we were asked to explain Graphs, we usually on a paper with pen, with Vertices, Edges. 
However, Computers can't do the same.
Instead, we have to keep track of the graph status using following methods:

1. Edge lists

    ```
    [ [0,1], [0,6], [0,8], [1,4], [1,6], [1,9], [2,4], [2,6], [3,4], [3,5],
    [3,8], [4,5], [4,9], [7,8], [7,9] ]
    ```

    - To represent an edge, we just have an array of two vertex numbers, or an array of objects containing the vertex numbers of the vertices that the edges are incident on

    - For weights, add either a third element to the array or more information to the object.

    - Simple but needs linear search for checking whether the graph contains a particular edge

2. Adjacency matrices

    ```
    [ [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0] ]
    ```

    - For a graph with |V|∣V∣vertical bar, V, vertical bar vertices, an adjacency matrix is a |V| \times |V|∣V∣×∣V∣vertical bar, V, vertical bar, times, vertical bar, V, vertical bar matrix of 0s and 1s, where the entry in row iii and column jjj is 1 if and only if the edge (i,j)(i,j)left parenthesis, i, comma, j, right parenthesis is in the graph

    - Upside

        1. we can find out whether an edge is present in constant time, by just looking up the corresponding entry in the matrix

    - Downside

        1. Takes V^2 Space even if the graph is sparse

        2. if you want to find out which vertices are adjacent to a given vertex i, you have to look at all ∣V∣ enties in row i even if only a small number of vertices are adjacent to vertex i

    - For an undirected graph, the adjacency matrix is symmetric.

3. Adjacency lists

    ```
    [ [1, 6, 8],
    [0, 4, 6, 9],
    [4, 6],
    [4, 5, 8],
    [1, 2, 3, 5, 9],
    [3, 4],
    [0, 1, 2],
    [8, 9],
    [0, 3, 7],
    [1, 4, 7] ]
    ```

    - Representing a graph with adjacency lists combines adjacency matrices with edge lists

    - Vertex numbers in an adjacency list are not required to appear in any particular order, though it is often convenient to list them in increasing order

Reference
https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
