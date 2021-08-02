""" Class to sort based on Topological order """
from collections import defaultdict , deque
class TopologicalSort:
    def topoSort(self, pre_requisites: [[int]], total_courses: int) -> [int]:

        pre_req = defaultdict(list)
        in_d = {}
        for key, val in pre_requisites:
            pre_req[val].append(key)
            in_d[key] = in_d.get(key, 0) + 1
            
        indegree_queue = deque([k for k in range(total_courses) if k not in in_d])

        top_sorted_order = []

        while indegree_queue:
            vert = indegree_queue.popleft()
            top_sorted_order.append(vert)
            
            if vert in pre_req:
                for neighbor in pre_req[vert]:
                    in_d[neighbor] -= 1

                    if in_d[neighbor] == 0:
                        indegree_queue.append(neighbor)

        return top_sorted_order[::-1] if len(top_sorted_order) == total_courses else []

print(TopologicalSort().topoSort([[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4]], 5))