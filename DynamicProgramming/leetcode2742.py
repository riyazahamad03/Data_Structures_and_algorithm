class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        dp = {}

        def dfs(i, rem):
            if rem <= 0:
                return 0
            if i == len(cost):
                return float("inf")
            if (i, rem) in dp:
                return dp[(i, rem)]
            painting = cost[i] + dfs(i + 1, rem - 1 - time[i])
            notPainting = dfs(i + 1, rem)
            dp[(i, rem)] = min(painting, notPainting)
            return dp[(i, rem)]
        return dfs(0, len(time))


x = Solution()
print(x.paintWalls(cost=[1, 2, 3, 2], time=[1, 2, 3, 2]))
