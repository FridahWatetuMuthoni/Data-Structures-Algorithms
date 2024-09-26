"""
Breadth First Search (BFS):
seen: Keeps track of visited nodes.
queue: Implements BFS using a queue (FIFO order).
results: Stores the order of visited nodes.

BFS Algorithm:
Start by adding the start node to the queue.
While the queue is not empty:
Dequeue the first node (FIFO order), and if it hasn’t been visited, process it by adding it to results.
Enqueue all its adjacent nodes if they haven’t been visited yet.

BFS vs DFS:
DFS explores as far as possible along each branch before backtracking.
BFS explores all neighbors of the current node before moving to the next level.
"""


# Adjacency List

graph = {
    'A':['B','D'],
    'B':['A','C'],
    'C':['B','D','E'],
    'D':['A','C','E'],
    'E':['C','D']
}


def depth_first_search(graph, start):
    seen = set()
    results = []
    stack = []
    
    stack.append(start)
    
    while(len(stack) > 0):
        current = stack.pop()
        
        #process the node
        if current not in seen:
            results.append(current)
            seen.add(current)
            
        
        #add all the adjacent nodes
        for element in graph[current]:
            if element not in seen:
                stack.append(element)
    return results

print(depth_first_search(graph, 'A'))
#output ['A', 'D', 'E', 'C', 'B']


def breadth_first_search(grapth, start):
    seen = set()
    queue = []
    results = []
    
    queue.append(start)
    
    while len(queue) > 0:
        current = queue.pop(0)
        
        if current not in seen:
            results.append(current)
            seen.add(current)
        
        for element in graph[current]:
            if element not in seen:
                queue.append(element)
    return results

print(breadth_first_search(graph, 'A'))
#output: ['A', 'B', 'D', 'C', 'E']


def dfs(graph, start, seen=None, results=None):
    if seen is None:
        seen = set()
    
    if results is None:
        results = []
    
    seen.add(start)
    
    results.append(start)
    
    for element in reversed(graph[start]):
        if element not in seen:
            dfs(graph, element, seen, results)
    return results

print(dfs(graph, 'A'))
#output ['A', 'D', 'E', 'C', 'B']
