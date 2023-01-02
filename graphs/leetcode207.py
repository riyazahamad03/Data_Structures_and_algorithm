class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap  = { i:[] for i in range(numCourses)}
        for c,r in prerequisites:
            preMap[c].append(r)
            
        visitSet = set()
        def dfs(c):
            if c in visitSet:
                return False
            if preMap[c] == []:
                return True
            visitSet.add(c)
            
            for pre in preMap[c]:
                if not dfs(pre):
                    return False
            visitSet.remove(c)
            preMap[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
x = Solution()
print(x.canFinish(2,[[1,0],[0,1]]))