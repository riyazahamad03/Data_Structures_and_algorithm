# Lettcode : 323. Number of Connected Components in an Undirected Graph


# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to find the number of connected components in an undirected graph.


# Input : n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2

class solution:
    def countComponents(self,n:int,edges:list[list[int]]):
        hashMap = {i : [] for i in range(n)}
        for i,e in edges:
            hashMap[i].append(e)
        visit = set()
        
        def dfs(i):
            if i in visit:
                return True
            visit.add(i)
            for idex in hashMap[i]:
                dfs(idex)
            return True
        res = 0
        for i in range(n):
            if i not in visit and dfs(i):
                res += 1
        return res

class UnionFind:
    def __init__(self):
        self.hashTable = {}
    def parent(self,x):
        y = self.hashTable.get(x,x)
        if x!=y:
            y = self.hashTable[x] = self.parent(y)
        return y
    def union(self,x,y):
        self.hashTable[self.parent(x)] = self.parent(y)
class Sol:
    def countComponents(self,n:int,edges:list[list[int]]) -> int:
        d = UnionFind()
        for a,b in edges:
            d.union(a,b)
        return len(set(d.parent(x) for x in range(n)))
X = Sol()
print("Approach 1 : " ,X.countComponents(5,[[0, 1], [1, 2], [3, 4]]))


# Approach 2
class UnionFindApproach2:
    def UnionOperation(self,x,y,lst):
        parentX = self.findParent(x,lst)
        parentY = self.findParent(y,lst)

        if parentX == parentY:
            return False
        lst[parentX] = parentY
        return True

    def findParent(self,x,lst):
        if x!=lst[x]:
            lst[x] = self.findParent(x,lst)
        return lst[x]

    def countComponents(self,n:int,edges:list[list[int]]):
        d = UnionFindApproach2()
        lst = [i for i in range(n)]
        res = n
        for a,b in edges:
            res -= d.UnionOperation(a,b,lst)
        return res

class sol3:
    def countComponents(self,n:int,edges:list[list[int]]):
        parents = [i for i in range(n)]
        rank = [[1] for _ in range(n)]

        def findPar(n1):
            res = n1
            while res != parents[res]:
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res
        def union(n1 , n2):
            p1 , p2 = findPar(n1) , findPar(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] < rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1 , n2 in edges:
            res -= union(n1 , n2)
        return res
            



Y = UnionFindApproach2()
print("Approach 2 : ",Y.countComponents(5,[[0, 1], [1, 2], [3, 4]]))

x = solution()
print(x.countComponents(7,[[0, 1], [1, 2], [3, 4], [5, 6]]))

x = sol3()
print(x.countComponents(7,[[0, 1], [1, 2], [3, 4], [5, 6]]))