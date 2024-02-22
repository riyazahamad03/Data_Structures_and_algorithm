class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        indeg = [0] * (n + 1)
        outdeg = [0] * (n + 1)
        for one, two in trust:
            indeg[two] += 1
            outdeg[one] += 1
        for i in range(1, n + 1):
            if indeg[i] == n - 1 and outdeg[i] == 0:
                return i
        return -1 if n > 1 else 1


x = Solution()
print(x.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
