# Lettcode : 323. Number of Connected Components in an Undirected Graph


# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to find the number of connected components in an undirected graph.


# Input : n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2
class UnionFind:
    def __init__(self):
        self.hashTable = {}
    def parent(self,x):
        y = self.hashTable.get(x,x)
        if x!=y:
            y = self.hashTable[x] = self.parent(y)
        # print(y)
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

Y = UnionFindApproach2()
print("Approach 2 : ",Y.countComponents(5,[[0, 1], [1, 2], [3, 4]]))