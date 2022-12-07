import collections

# n,node = 4,2
# lst = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1]]
# n,node = 5,1
# lst = [[1, 0, 1, 0, 1], [0, 1, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 1, 1], [1, 0, 1, 1, 1]]

class solution:
    def GraphBfs(self,n,lst,node):
        q = collections.deque()
        visitSet = set()
        q.append(node)
        visitSet.add((node-1,node-1))
        while q:
            node = q.popleft()
            if node not in res:
                res.append(node)
            currNode = node-1
            for neighbour in range(n):
                if  (currNode != neighbour) and (lst[currNode][neighbour] == 1) and ((currNode,neighbour) not in visitSet):
                    q.append(neighbour+1)
                    visitSet.add((currNode,neighbour))

        return res

    def GraphDfs(self,n,lst):
        visitSet = set()
        res = []
        def dfs(node,i,j):
            if (i,j) in visitSet:
                return
            res.append(node)
            visitSet.add((i,j))
            for nei in range(n):
                if node-1!=nei and lst[node-1][nei] == 1:
                    visitSet.add((node-1,nei))
                    dfs(nei+1,nei,0)       
        dfs(node,node-1,0)
        return res
        
# n,node = map(int,input().split())
# lst,res = [],[]
# for i in range(n):
#     lst.append(list(map(int,input().split())))
res = []
n,node = 5,1
lst = [[1, 0, 1, 0, 1], [0, 1, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 1, 1], [1, 0, 1, 1, 1]]
x = solution()
print("Bfs Traversal : ",x.GraphBfs(n,lst,node))
print("Dfs Traversal : ",x.GraphDfs(n,lst))
            

