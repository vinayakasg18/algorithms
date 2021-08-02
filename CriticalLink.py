from collections import defaultdict
from itertools import count


class CriticalLink:
    def __init__(self):
        self.current = 0

    def criticalLink(self, n: int, links: [[int]]) -> int:
        gr = defaultdict(list)
        for vert in links:
            gr[vert[0]].append(vert[1])
            gr[vert[1]].append(vert[0])

        dfn = [None for i in range(n)]
        low = [None for i in range(n)]
        cur = 0
        start = 0
        result = []

        def dfs(node, parent):
            if dfn[node] is None:
                dfn[node] = self.current
                low[node] = self.current
                self.current += 1
                for n in gr[node]:
                    if dfn[n] is None:
                        dfs(n, node)

                if parent is not None:
                    lw = min([low[i] for i in gr[node] if i != parent] + [low[node]])
                else:
                    lw = min(low[i] for i in gr[node] + [low[node]])
                low[node] = lw

        dfs(0, None)

        for vert in links:
            if low[vert[0]] > dfn[vert[1]] or low[vert[1]] > dfn[vert[0]]:
                result.append(vert)
        result = len(result)
        return result
