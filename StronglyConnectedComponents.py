""" Class to find the strongly connected components """


class StronglyConnectedComponents:
    def scc(self, students: int, knows: [[int]]) -> [[int]]:
        """ Strongly connected component function """

        self.graph = {x: [] for x in range(students)}
        for n1, n2 in knows:
            self.add_edge(n1, n2, True)
        stack = []
        visited = [False] * students
        for i in range(students):
            if not visited[i]:
                self.fill_order(i, visited, stack)
        self.tmp_list = []
        self.get_transpose(students)
        visited = [False] * students
        result = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                self.dfs_util(i, visited)
                result.append(self.tmp_list)
                self.tmp_list = []
        return result

    def add_edge(self, node1, node2, flag):
        """ Adding edge to node function """

        if flag:
            self.graph[node1].append(node2)
        else:
            self.transpose[node1].append(node2)

    def dfs_util(self, node, visited):
        """ Util Function """

        visited[node] = True
        self.tmp_list.append(node)
        for elem in self.transpose[node]:
            if not visited[elem]:
                self.dfs_util(elem, visited)

    def fill_order(self, node, visited, stack):
        """ Fill order function """

        visited[node] = True
        for elem in self.graph[node]:
            if not visited[elem]:
                self.fill_order(elem, visited, stack)
        stack = stack.append(node)

    def get_transpose(self, students):
        """ Transpose Function """

        self.transpose = {x: [] for x in range(students)}
        for i in self.graph:
            for j in self.graph[i]:
                self.add_edge(j, i, False)
