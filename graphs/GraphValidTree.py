# LeetCode : 261 Graph Valid Tree

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
#  write a function to check whether these edges make up a valid tree.

class ValidGraphTree:
    def __init__(self):
        self.visit = set()
    
    
    def ValidTree(self,n,edges):
        if not n:
            return False
        adj = { i : [] for i in range(n)}
        
        for ad1,ad2 in edges:
            adj[ad1].append(ad2)
            adj[ad2].append(ad1)
        
        def Dfs(self,i,prev):
            if i in self.visit:
                return False
            self.visit.add(i)

            for adjacent in adj[i]:
                if adjacent == prev:
                    continue
                if not Dfs(self,adjacent,i):
                    return False
            return True
        return Dfs(self,0,-1) and len(self.visit) == n
X = ValidGraphTree()
print(X.ValidTree(5,[[0, 1], [0, 2], [0, 3], [1, 4]]))

print(X.ValidTree(5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

        
            
