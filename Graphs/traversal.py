graph = {
    'A':['B','D'],
    'B':['A','C'],
    'C':['B','D','E'],
    'D':['A','C','E'],
    'E':['C','D']
}


def depth_first_search(graph, start):
    results = []
    seen = set()
    stack = []
    
    stack.append(start)
    
    while len(stack) > 0:
        
        current  =  stack.pop()
        
        if current not in seen:
            results.append(current)
            seen.add(current)
        
        for element in graph[current]:
            if element not in seen:
                stack.append(element)
    return results

print(depth_first_search(graph, 'A'))
#output ['A', 'D', 'E', 'C', 'B']

def breadth_first_search(grapth, start):
    results = []
    seen = set()
    queue = []
    
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