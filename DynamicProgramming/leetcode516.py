class solution:
    def longestPalindromicSubsequences(self , s : str):
        revS = s[::-1]
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        for r in range(len(s)-1 , -1 , -1):
            for c in range(len(s)-1 , -1 , -1):
                if s[r] == revS[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c] , dp[r][c + 1])
        return dp[0][0]
x = solution()
print(x.longestPalindromicSubsequences("bbbab"))