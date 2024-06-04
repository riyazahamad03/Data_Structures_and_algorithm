from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        res = 0
        for c in cnt:
            res += (cnt[c] // 2) * 2
        for c in cnt:
            if cnt[c] % 2:
                return res + 1
        return res


x = Solution()
print(x.longestPalindrome(s="abccccdd"))
