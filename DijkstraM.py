""" Class to find the minimum distance to each edge node in the graph """
class Dijkstra:
        def shortestDistance(self, edges, vertices):
            
            # Create a adjacency matrix
            d = {}
            
            for i in range(vertices):
                d[i] = []

            # maintain distance of edges
            large_num = 999999
            dist = [large_num] * vertices
            dist[0] = 0
            
            for edge in edges:
                d[0].append(edge)
            print(d)
            print(dist)

print(Dijkstra().shortestDistance([[0, 1, 4], [0, 2, 2], [1, 3, 2], [1, 4, 3], [2, 1, 1], [2, 3, 2], [2, 4, 5], [4, 3, 1], [5, 2, 2]], 6))