class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        adj = {i: 0 for i in range(1, len(edges) + 2)}
        for u, v in edges:
            adj[u] += 1
            adj[v] += 1
        for v in adj:
            if adj[v] == len(edges):
                return v


x = Solution()
print(x.findCenter(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]))
