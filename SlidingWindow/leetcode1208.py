class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        l = 0
        cost = 0

        for r in range(len(s)):
            cost += abs(ord(s[r]) - ord(t[r]))
            while l < len(s) and cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r - l + 1)
        return res


x = Solution()
print(x.equalSubstring(s="abcd", t="bcdf", maxCost=3))
