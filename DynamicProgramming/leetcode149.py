class solution:
    def wordBreak(self,s:str,wordDict:list[str]):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for words in wordDict:
                if i + len(words) <= len(s) and s[i : i + len(words)] == words:
                    dp[i] = dp[i + len(words)]
                if dp[i]:
                    break
        return dp[0]
x = solution()
print(x.wordBreak("leetcode",["leet","code"]))