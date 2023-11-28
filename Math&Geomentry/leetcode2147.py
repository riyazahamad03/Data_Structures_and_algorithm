class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        dp = [[-1] * 3 for _ in range(len(corridor))]

        def dfs(idx, seats):
            if idx == len(corridor):
                return 1 if seats == 2 else 0
            if dp[idx][seats] != -1:
                return dp[idx][seats]
            res = 0
            if seats == 2:
                if corridor[idx] == "S":
                    res = dfs(idx + 1, 1)
                else:
                    res = (dfs(idx + 1, 0) + dfs(idx + 1, 2)) % mod
            else:
                if corridor[idx] == "S":
                    res = dfs(idx + 1, seats + 1)
                else:
                    res = dfs(idx + 1, seats)
            dp[idx][seats] = res % mod
            return res

        return dfs(0, 0)

    def numberOfWaysII(self, corridor: str):
        seats = []
        mod = 10**9 + 7
        for i in range(len(corridor)):
            if corridor[i] == "S":
                seats.append(i)

        if len(seats) % 2:
            return 0

        res, idx = 1, 1

        while idx < len(seats) - 1:
            res = (res * (seats[idx + 1] - seats[idx])) % mod
            idx += 2
        return res


x = Solution()
print(x.numberOfWays("SSPPSPS"))
print(x.numberOfWaysII("SSPPSPS"))
