class solution:
    def minReOrder(self , n : int , connections : list[list[int]]):
        reOrder = 0
        visit = set()
        pathEdges = {(a , b) for a,b in connections}
        neighBors = {city : [] for city in range(n)}
        for a,b in connections:
            neighBors[a].append(b)
            neighBors[b].append(a)
        def dfs(city):
            nonlocal reOrder
            for nei in neighBors[city]:
                if nei in visit:
                    continue
                if (nei , city) not in pathEdges:
                    reOrder += 1
                visit.add(nei)
                dfs(nei)
        visit.add(0)
        dfs(0)
        return reOrder
x = solution()
print(x.minReOrder(5 , [[1,0],[1,2],[3,2],[3,4]]))
