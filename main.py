
### 2. `main.py`

#python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph): 
    topo_order = topological_sort(graph)
    return  calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    visited = [False] * len(graph)
    topo_order = []
    
    def dfs(graph, v, visited, topo_order):
        visited[v] = True
        for neighbor_node, _ in graph[v]:
            if not visited[neighbor_node]:
                dfs(graph, neighbor_node, visited, topo_order)
        topo_order.append(v)
    
    for v in range(len(graph)):
        if not visited[v]:
            dfs(graph, v, visited, topo_order)

    topo_order.reverse()
    return topo_order

def calculate_longest_path(graph, topo_order):
    dist = [-float('Inf')] * len(graph)

    for node in topo_order:
        if dist[node] == -float('Inf'):
            dist[node] = 0
        for neighbor_node, weight in graph[node]:
            if dist[neighbor_node] < dist[node] + weight:
                dist[neighbor_node] = dist[node] + weight

    return max(dist)