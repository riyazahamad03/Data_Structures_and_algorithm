class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        adj = {i: [] for i in range(n)}
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def dfs(node):
            if node == destination:
                return True
            if node in visit:
                return False
            visit.add(node)
            for nodes in adj[node]:
                if dfs(nodes):
                    return True
            return False

        visit = set()
        return dfs(source)


x = Solution()
print(x.validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))
