""" Breadth First serach  """

class BreadthFirstSearch:
    """ Breadth First serach  class """
    
    def breadthFirstSearch(self, edges, vertices):
        """ BFS Function """
        
        print(type(vertices))
        
        self.graph = { x: [] for x in range(vertices)}
        
        for n1, n2 in edges:
            self.add_edge(n1, n2)
        
        return self.bfs(vertices)
    
    
    def add_edge(self, n1, n2):
        self.graph[n1].append(n2)
        
    def prev(self, node):
        return self.graph[node]
    
    def bfs(self, vertices):
        
        if vertices == 0:
            return []
        
        visited = [False] * vertices
        sd = [-1] * vertices
        parent = [x for x in range(vertices)]
        oe = []
        oe.append(0)
        visited[0] = True
        sd[0] = 0
        while oe:
            curr_node = oe.pop(0)
            for node in self.prev(curr_node):
                if not visited[node]:
                    visited[node] = True
                    parent[node] = curr_node
                    sd[node] = sd[parent[node]] + 1
                    oe.append(node)
                    
        return sd


print(BreadthFirstSearch().breadthFirstSearch([[0, 1], [0, 4], [1, 3], [1, 2], [3, 4], [2, 4], [3, 6], [3, 5], [2, 3], [2, 6], [2, 5]], 7))