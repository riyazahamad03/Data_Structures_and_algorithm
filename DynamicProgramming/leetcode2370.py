class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * (26)

        for char in s:
            curr = ord(char) - ord("a")
            longest = 1
            for a in range(26):
                if abs(a - curr) <= k:
                    longest = max(longest, 1 + dp[a])
            dp[curr] = max(dp[curr], longest)
        return max(dp)


x = Solution()
print(x.longestIdealString(s="acfgbd", k=2))
