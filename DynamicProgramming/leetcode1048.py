class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPossible(s, t):
            idx = 0  # s
            jdx = 0  # t
            while idx < len(s):
                if jdx < len(t) and s[idx] == t[jdx]:
                    jdx += 1
                idx += 1
            return jdx == len(t)

        words.sort(key=lambda x: len(x))
        dp = [1] * (len(words))
        for i in range(len(words) - 1, -1, -1):
            for j in range(i + 1, len(words)):
                if len(words[i]) + 1 == len(words[j]):
                    if isPossible(words[j], words[i]):
                        dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


x = Solution()
print(x.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]))
