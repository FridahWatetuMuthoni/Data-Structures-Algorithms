"""
find all paths:
mumbai -> paris -> newyork
mumbai -> paris -> dubai -> newyork
mumabi -> dubai -> newyork

find shortest path:
mumbai -> paris -> newyork
mubai -> Dubai -> newyork
"""

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph = {}
        
        for start, end in self.edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
        
            # (Optional) If you want a bidirectional (undirected) graph, also add the reverse
            if end in self.graph:
                self.graph[end].append(start)
            else:
                self.graph[end] = [start]
    
    def get_paths(self, start, end, path=[]):
        path += [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph:
            return []
        
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    path.append(p)
                    
        return path

if __name__ == "__main__":
    routes = [
        ('mumbai', 'paris'),
        ('mumbai', 'dubai'),
        ('paris','dubai'),
        ('paris', 'newyork'),
        ('dubai', 'newyork'),
        ('newyork', 'toronto')
    ]
    
    route_graph = Graph(routes)
    print(route_graph.graph)
    start = 'mumbai'
    end = "dubai"
    print(f"paths between {start} and {end} is {route_graph.get_paths(start, end)}")