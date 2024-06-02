class Solution:
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        return s


x = Solution()
print(x.reverseString(s=["h", "e", "l", "l", "o"]))
