class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        
        for idex in prerequisites:
            preMap[idex[0]].append(idex[1]) 
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)

            for c in preMap[crs]:
                if not dfs(c):
                    return False
            
            visitSet.remove(crs)
            preMap[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
x = Solution()
print(x.canFinish(2,[[1,0],[0,1]]))