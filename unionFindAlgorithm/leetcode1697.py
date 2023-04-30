class solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]):
        par = [i for i in range(n)]
        rank = [1]*(n)

        def findPar(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                par[res] = n1
            return res

        def union(n1, n2):
            p1, p2 = findPar(n1), findPar(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p1] = p2
                rank[p1] += rank[p2]
            else:
                par[p2] = p1
                rank[p2] += rank[p1]
            return True
        for q1 , q2 , weight in queries:
            for n1 , n2 , aWeight in edgeList:
                print(n1 , n2 , aWeight)
x = solution()
print(x.distanceLimitedPathsExist(3 , [[0,1,2],[1,2,4],[2,0,8],[1,0,16]] , [[0,1,2],[0,2,5]]))