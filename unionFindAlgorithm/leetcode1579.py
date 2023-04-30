class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def findPar(self, x):
        res = x
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res

    def union(self, n1, n2):
        p1, p2 = self.findPar(n1), self.findPar(n2)
        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.n -= 1
        return 1

    def isConnected(self):
        return self.n == 1


class solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]):
        alice, bob = UnionFind(n), UnionFind(n)
        resCount = 0
        for type, src, dest in edges:
            if type == 3:
                resCount += alice.union(src, dest) | bob.union(src, dest)
        for type, src, dest in edges:
            if type == 1:
                resCount += alice.union(src, dest)
            elif type == 2:
                resCount += bob.union(src, dest)
        if alice.isConnected() and bob.isConnected():
            return len(edges) - resCount
        return -1


x = solution()
print(x.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [
      1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))
print(x.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))
