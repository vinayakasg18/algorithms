""" Class to identify if the graph is bipartite """

class Bipartiteness:
    def bipartite(self, edges, vertices):
        if vertices == 0 or vertices == 1:
            return 1
        self.graph = {x : [] for x in range(vertices)}
        self.add_edge(edges)
        return self.breadth_first_search(vertices)

    def add_edge(self, edges):
        for node1, node2 in edges:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
    
    def successor(self, node):
        return self.graph[node]

    def breadth_first_search(self, vertices):
        clr = [-1 for x in range(vertices)]
        frg = []
        for i in range(vertices):
            if clr[i] == -1:
                frg.append((i, 0))
                clr[i] = 0

                while frg:
                    node, col = frg.pop(0)
                    for succ in self.graph[node]:
                        if clr[succ] == col:
                            return -1
                        if clr[succ] == -1:
                            clr[succ] = 1 - col
                            frg.append((succ, clr[succ]))
        return 1

# print(Bipartiteness().bipartite([[0, 6], [1, 6], [1, 2], [5, 6], [3, 2], [3, 4]], 7))
# print(Bipartiteness().bipartite([[0, 6], [1, 6], [1, 2], [5, 6], [3, 2], [3, 4], [6, 2]], 7))
# print(Bipartiteness().bipartite([[4, 3], [0, 6], [2, 3], [2, 6], [1, 6]], 7))
