class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1 for _ in range(n)]
        self.weights = [131071] * n

    def find(self, n1):
        res = n1
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res

    def union(self, n1, n2, w):
        g1, g2 = self.find(n1), self.find(n2)

        self.weights[g1] = self.weights[g2] = self.weights[g1] & self.weights[g2] & w
        if self.rank[g1] > self.rank[g2]:
            self.par[g1] = g2
            self.rank[g1] += self.rank[g2]
        else:
            self.par[g2] = g1
            self.rank[g2] += self.rank[g1]

    def minCost(self, g1, g2):
        if g1 == g2:
            return 0
        if self.find(g1) != self.find(g2):
            return -1
        return self.weights[self.find(g1)]


class Solution:
    def minimumCost(
        self, n: int, edges: list[list[int]], query: list[list[int]]
    ) -> list[int]:
        uf = UnionFind(n)
        for s, d, w in edges:
            uf.union(s, d, w)
        res = []

        for s, d in query:
            res.append(uf.minCost(s, d))
        return res


x = Solution()
print(
    x.minimumCost(n=5, edges=[[0, 1, 7], [1, 3, 7], [1, 2, 1]], query=[[0, 3], [3, 4]])
)
