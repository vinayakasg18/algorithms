import itertools


# class StronglyConnectedComponents:
#     def scc(self, students: int, knows: [[int]]) -> [[int]]:


def strong_connect(vertex):
    global edges, indices, lowlinks, connected_components, index, stack
    indices[vertex] = index
    lowlinks[vertex] = index
    index += 1
    stack.append(vertex)

    for v, w in (e for e in edges if e[0] == vertex):
        if indices[w] < 0:
            strong_connect(w)
            lowlinks[v] = min(lowlinks[v], lowlinks[w])
        elif w in stack:
            lowlinks[v] = min(lowlinks[v], indices[w])

    if indices[vertex] == lowlinks[vertex]:
        connected_components.append([])
        while stack[-1] != vertex:
            connected_components[-1].append(stack.pop())
        connected_components[-1].append(stack.pop())


edges = [[0, 1], [1, 2], [2, 0], [2, 3], [4, 3], [3, 4]]
vertices = set(v for v in itertools.chain(*edges))
indices = dict((v, -1) for v in vertices)
lowlinks = indices.copy()
connected_components = []

index = 0
stack = []
for v in vertices:
    if indices[v] < 0:
        strong_connect(v)

print(connected_components)
