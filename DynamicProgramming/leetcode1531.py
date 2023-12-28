class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = {}

        def dfs(i, k, prev, prevCnt):
            if k < 0:
                return float("inf")
            if i == len(s):
                return 0
            if (i, k, prev, prevCnt) in dp:
                return dp[(i, k, prev, prevCnt)]
            if s[i] == prev:
                inc = 1 if prevCnt in [1, 9, 99] else 0
                res = inc + dfs(i + 1, k, prev, prevCnt + 1)
            else:
                res = min(dfs(i + 1, k - 1, prev, prevCnt), 1 + dfs(i + 1, k, s[i], 1))
            dp[(i, k, prev, prevCnt)] = res
            return res

        return dfs(0, k, "", 0)


x = Solution()
print(x.getLengthOfOptimalCompression(s="aaabcccd", k=2))
