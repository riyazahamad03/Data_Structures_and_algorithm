class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for n1, n2 in roads:
            adj[n1].append(n2)
            adj[n2].append(n1)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = len(adj[i]) + len(adj[j])

                if i in adj[i] or j in adj[i]:
                    rank -= 1
                res = max(res, rank)
        return res


x = Solution()
print(x.maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]))
