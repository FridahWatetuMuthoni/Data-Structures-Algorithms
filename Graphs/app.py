"""
A graph is a data structure made up of nodes/vertices and edges or the connections between nodes.
How to represents graphs with code:
i. Use an adjacency list for most real-world problems, especially with sparse graphs,
where space efficiency and traversal speed are critical.
2. Use an adjacency matrix if you have a dense graph or need fast edge existence checks. However, 
it's rarely used for large graphs due to its high space complexity.

Key Takeaway:
Adjacency List is generally better for most practical applications due to its space efficiency 
and performance for traversal operations, especially for sparse graphs.

"""

nodes = ['A','B','C','D','E']
edges = [
    ['A','B'],
    ['A','D'],
    ['B','C'],
    ['C','D'],
    ['C','E'],
    ['D','E']
]

#given a node find the adjency nodes
#time complexity O(n) => O(e + v)
def adjacency_nodes(node):
    results = []
    
    for arr in edges:
        if arr[0] == node:
            results.append(arr[1])
        if arr[1] == node:
            results.append(arr[0])
    return results

print(adjacency_nodes('A'))
print(adjacency_nodes('B'))
print(adjacency_nodes('C'))
print(adjacency_nodes('D'))
print(adjacency_nodes('E'))

def is_connected(node1, node2):
    for arr in edges:
        if (arr[0] == node1 or arr[1] == node1) and (arr[0] == node2 or arr[1] == node2):
            return True
    return False

print(is_connected('A','C')) #False
print(is_connected('A', 'C'))  #False
print(is_connected('A', 'B'))  #True


#adjacenct Matrix

vertices = ['A','B','C','D','E']

adjacenctMatrix = [
    [0,1,0,1,0],
    [1,0,1,0,0],
    [0,1,0,1,1],
    [1,0,1,0,1],
    [0,0,1,1,0],
]


#Time complexity => O(v)
#Space complexity => O(V^2)
def adjecent(node):
    node_index = -1
    for index, value in enumerate(vertices):
        if value == node:
            node_index = index
            break
    results = []
    
    if node_index == -1:
        return []
    
    for index, value in enumerate(adjacenctMatrix[node_index]):
        if value == 1:
            results.append(vertices[index])
    return results



print(adjecent('A')) #[B, D]
print(adjecent('B')) #[A, C]
print(adjecent('C')) #[B, D, E]
print(adjecent('D')) ##[A, C, E]
print(adjecent('E')) #[C, D]




# Adjacency List

graph = {
    'A':['B','D'],
    'B':['A','C'],
    'C':['B','D','E'],
    'D':['A','C','E'],
    'E':['C','D']
}

#O(1)
def adjecent_nodes(node):
    results = graph[node]
    return results

print(adjacency_nodes('A'))

#O(v)
def connected(node1, node2):
    arr1 = graph[node1]
    
    for element in arr1:
        if element == node2:
            return True
    return False


print(connected('A','C')) #False
print(connected('A', 'C'))  #False
print(connected('A', 'B'))  #True
print(connected('A', 'E'))  #False
print(connected('B', 'D'))  #True
