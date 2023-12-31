class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        startIdx, endIdx = {}, {}
        res = -1
        for i in range(len(s)):
            startIdx[s[i]] = i
        for j in range(len(s) - 1, -1, -1):
            endIdx[s[j]] = j

        for e in startIdx:
            if e in endIdx:
                res = max(res, startIdx[e] - endIdx[e] - 1)
        return res


x = Solution()
print(x.maxLengthBetweenEqualCharacters("abca"))
