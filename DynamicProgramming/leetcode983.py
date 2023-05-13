class solution:
    def minCostTicket(self, days: list[int], costs: list[int]):
        dp = {}

        def backTrack(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float('inf')
            for t, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + t:
                    j += 1
                dp[i] = min(dp[i], c + backTrack(j))
            return dp[i]
        return backTrack(0)


x = solution()
print(x.minCostTicket([1, 4, 6, 7, 8, 20],  [2, 7, 15]))
