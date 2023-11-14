class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        def getLdx(val):
            for i in range(len(s)):
                if s[i] == val:
                    return i

        def getRdx(val):
            for i in range(len(s) - 1, -1, -1):
                if s[i] == val:
                    return i

        letters = set(s)

        res = 0
        for l in letters:
            l, r = getLdx(l), getRdx(l)
            bet = set()

            for idx in range(l + 1, r):
                bet.add(s[idx])
            res += len(bet)

        return res


x = Solution()
print(x.countPalindromicSubsequence("aabca"))
