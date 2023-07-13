class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if not preMap[crs]:
                return True

            visit.add(crs)

            for course in preMap[crs]:
                if not dfs(course):
                    return False

            visit.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


x = Solution()
print(x.canFinish(2, [[1, 0], [0, 1]]))
