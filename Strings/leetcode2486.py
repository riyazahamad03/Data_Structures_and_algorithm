class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx = 0
        i = 0
        while i < len(s) and idx < len(t):
            if s[i] == t[idx]:
                idx += 1
            i += 1

        if idx >= len(t):
            return 0
        return len(t) - idx


x = Solution()
print(x.appendCharacters(s="coaching", t="coding"))
