class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, res = len(s) - 1, 0
        while ord(s[i]) == 32:
            i -= 1
        while i >= 0 and ord(s[i]) != 32:
            i -= 1
            res += 1
        return res


x = Solution()
print(x.lengthOfLastWord("   fly me   to   the moon  "))
