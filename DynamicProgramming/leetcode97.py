class solution:
    def isInterLeave(self, s1: str, s2: str, s3: str):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s2), - 1, - 1):
            for j in range(len(s1), - 1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
class solution2:
    def isInterLeave(self, s1: str, s2: str, s3: str):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def dfs(i , j):
            if (i , j) in dp:
                return dp[i , j]
            if i == len(s1) and j == len(s2):
                return True
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1 , j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i , j + 1):
                return True
            dp[(i , j)] = False
            return dp[(i , j)]
        return dfs(0 , 0)

x = solution()
print(x.isInterLeave("aabcc",  "dbbca", "aadbbcbcac"))
