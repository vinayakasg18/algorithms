from collections import defaultdict
class TopologicalSort:
        def topoSort(self, pre_requisites: [[int]], total_courses: int) -> [int]:
            pre_req = defaultdict(list)
            in_d = defaultdict(int)

            for key, val in pre_requisites:
                pre_req[key].append(val)

            for key, values in pre_req.items():
                for val in values:
                    in_d[0] = 0
                    for i in range(total_courses):
                        if i not in in_d and val == i:
                            in_d[i] = in_d.get(val, 0) + 1
                        
                
            # for key, values in pre_req.items():
            #     for val in values:
            #         for i in range(total_courses):
            #             if i == val:
            #                 in_d[i] = +1
            #             elif i in pre_req.keys() and i not in in_d.keys():
            #                 in_d[i] = 0
            #             if i in in_d.keys() and in_d[i] != 0 and val == i:
            #                 in_d[i] = in_d[i] + 1
            #             # elif i in in_d.keys() and in_d[i] != 0 and i == val:
            #             #     in_d[i] = in_d[i] + 1
                
            print(pre_req)
            print(in_d)

print(TopologicalSort().topoSort([[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4], [4, 0]], 5))