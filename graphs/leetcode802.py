class solution:
    def eventualSafeNodes(self , graph : list[list[int]]):
        safeState = {}
        def dfs(i):
            if i in safeState:
                return safeState[i]
            safeState[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safeState[i] = True
            return True
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
x = solution()
print(x.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))