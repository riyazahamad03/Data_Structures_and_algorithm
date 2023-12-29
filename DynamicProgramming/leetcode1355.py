class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        cache = {}

        def dfs(i, d, curr_max):
            if i == len(jobDifficulty):
                return 0 if d == 0 else float("inf")

            if d == 0:
                return float("inf")

            if (i, d, curr_max) in cache:
                return cache[(i, d, curr_max)]

            cMax = max(curr_max, jobDifficulty[i])
            res = min(dfs(i + 1, d, cMax), cMax + dfs(i + 1, d - 1, -1))

            cache[(i, d, curr_max)] = res
            return res

        return dfs(0, d, -1) if dfs(0, d, -1) != float("inf") else -1


x = Solution()
print(x.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
