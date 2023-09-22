class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for i in range(len(t)):
            if idx < len(s) and s[idx] == t[i]:
                idx += 1
        return True if idx == len(s) else False


x = Solution()
print(x.isSubsequence(s="abc", t="ahbgdc"))
