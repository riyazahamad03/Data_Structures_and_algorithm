# 91. Decode Ways
class solution:
    def decodeWays(self,s:str):
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i  + 1)
            if (i + 1 < len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0) 


x = solution()
print(x.decodeWays("12134"))