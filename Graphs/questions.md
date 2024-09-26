# Graphs Interview Questions

1. Graph Representation:

Graph Representations:

Adjacency Matrix: A 2D array where matrix[i][j] = 1 if there is an edge between nodes i and j.
Adjacency List: A dictionary where each key is a node, and the value is a list of adjacent nodes.
python

```python
# Adjacency List Representation
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['C', 'D']
}
```

2. Depth-First Search (DFS):

Problem: Implement DFS for a graph.
Solution:

```python

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['C', 'D']
}

dfs(graph, 'A')  # Output: A B C D E
```

3. Breadth-First Search (BFS):

Problem: Implement BFS for a graph.
Solution:

```python

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
bfs(graph, 'A')  # Output: A B D C E
```

4. Detect a Cycle in a Directed Graph:

Problem: Given a directed graph, detect if there is a cycle.
Solution:

```python

def is_cyclic(graph):
    visited = set()
    rec_stack = set()

    def dfs(v):
        visited.add(v)
        rec_stack.add(v)

        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(v)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

# Example usage
graph_with_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
}

print(is_cyclic(graph_with_cycle))  # Output: True
```

5. Find the Shortest Path in an Unweighted Graph:

Problem: Given an unweighted graph, find the shortest path between two nodes using BFS.
Solution:

```python

def shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            visited.add(node)
    return None

# Example usage
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['C', 'D']
}

print(shortest_path(graph, 'A', 'E'))  # Output: ['A', 'D', 'E']
```

6. Check if a Graph is Bipartite:

Problem: Determine if a given graph is bipartite.
Solution: A graph is bipartite if you can color the graph using two colors such that no two adjacent nodes have the same color. You can check this using BFS.

```python

def is_bipartite(graph):
    color = {}

    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0  # Assign the first color

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True

# Example usage
bipartite_graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

print(is_bipartite(bipartite_graph))  # Output: True
```

7. Dijkstra's Algorithm:

Problem: Find the shortest path in a weighted graph.
Solution:

```python

import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Example usage (weighted graph)
graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('D', 1), ('E', 5)],
    'D': [('A', 4), ('C', 1), ('E', 3)],
    'E': [('C', 5), ('D', 3)]
}

print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4, 'E': 7}
```

8. Topological Sort:

Problem: Given a directed acyclic graph (DAG), perform topological sorting.
Solution:

```python

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse stack to get topological ordering

# Example usage (DAG)
dag = {
    'A': ['B', 'D'],
    'B': ['C'],
    'C': [],
    'D': ['C', 'E'],
    'E': []
}

print(topological_sort(dag))  # Output: ['A', 'D', 'E', 'B', 'C']
```
