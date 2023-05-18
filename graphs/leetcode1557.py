class solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]):
        visit = set()
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)

        def dfs(node):
            for dest in adj[node]:
                if dest not in visit:
                    if dest not in visit:
                        visit.add(dest)
                        dfs(dest)

        for src in range(n):
            if src not in visit:
                dfs(src)
        res = []
        for src in range(n):
            if src not in visit:
                res.append(src)
        return res


x = solution()
print(x.findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
