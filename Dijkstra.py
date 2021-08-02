""" Class to find shortest distance using Dijkstra """

class Dijkstra:
    def shortestDistance(self, edges, vertices):
        self.graph = {x : [] for x in range(vertices)}
        self.complete_graph(edges, vertices)
        print(self.graph)
        if vertices == 1:
            return [0]
        if vertices == 0:
            return []
        min_distance = self.dijstra(vertices)
        for index in range(len(min_distance)):
            if min_distance[index] == 9999999:
                min_distance[index] = -1
        return min_distance

    def complete_graph(self, edges, vertices):
        for node1, node2, dist in edges:
            self.graph[node1] += [(node2, dist)]

    def min_dist(self, min_distance, sep_vertices, vertices):
        min_val = 9999999
        min_node = -1
        for node in range(vertices):
            if min_distance[node] < min_val and not sep_vertices[node]:
                min_val = min_distance[node]
                min_node = node
        return min_node
    
    def sucs(self, node):
        return self.graph[node]

    def dijstra(self, vertices):
        start_node = 0
        min_distance = [9999999] * vertices
        min_distance[start_node] = 0
        sep_vertices = [False] * vertices

        for node in range(vertices):
            min_index = self.min_dist(min_distance, sep_vertices, vertices)
            if min_index == -1:
                continue
            sep_vertices[min_index] = True
            for v, dist in self.sucs(min_index):
                if dist > 0 and not sep_vertices[v] and min_distance[v] > min_distance[min_index] + dist:
                    min_distance[v] = min_distance[min_index] + dist

        return min_distance

# print(Dijkstra().shortestDistance([[0, 1, 4], [0, 2, 2], [1, 3, 2], [1, 4, 3], [2, 1, 1], [2, 3, 2], [2, 4, 5], [4, 3, 1], [5, 2, 2]], 6))
