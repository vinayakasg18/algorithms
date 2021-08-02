""" Class to find the MST """

class MinimumSpanningTree:
    def mst(self, edges: [[int]], vertices: int) -> int:
        
        self.graph = {x : [] for x in range(vertices)}
        self.complete_graph(edges, vertices)
        self.vert = {x: -1 for x in range(vertices)}
        self.rank = {x: 0 for x in range(vertices)}
        
        print(self.graph)
        print(self.vert)
        print(self.rank)
        

    # Make adjacency list
    def complete_graph(self, edges, vertices):
        for node1, node2, dist in edges:
            self.graph[node1] += [(node2, dist)]
            
print(MinimumSpanningTree().mst([[0, 1, 3], [1, 2, 1], [2, 0, 2]], 3))
        