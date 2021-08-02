class BreadthFirstSearch:
    """ Breadth First serach  class """
    
    def breadthFirstSearch(self, edges, vertices):
        d = {}
         
        for i in range(vertices):
            d[i] = []
        for arr in edges:
            d[arr[0]].append(arr[1])
            
        queue = [0]
        visited = set()
        final  = [-1] * vertices
        final[0] = 0
        visited.add(0)
        
        while queue:
            ele = queue.pop(0)
            
            for elements in d[ele]:
                visited.add(elements)
                queue.append(elements)
                
                if final[elements] == -1:
                    final[elements] = final[ele] + 1
                else:
                    temp = final[elements] + final[ele] +1
                    if temp < final[elements]:
                        final[elements] = temp
                
        return final
  
print(BreadthFirstSearch().breadthFirstSearch([[0, 1], [0, 4], [1, 3], [1, 2], [3, 4], [2, 4], [3, 6], [3, 5], [2, 3], [2, 6], [2, 5]], 7))