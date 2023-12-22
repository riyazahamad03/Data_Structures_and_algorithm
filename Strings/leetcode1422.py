class Solution:
    def maxScore(self, s: str) -> int:
        zero = [0] * len(s)
        one = [0] * len(s)
        zeroCnt = oneCnt = 0
        for i in range(len(s)):
            if s[i] == "0":
                zeroCnt += 1
            zero[i] = zeroCnt
        for j in range(len(s)):
            if s[j] == "1":
                oneCnt += 1
            one[j] = oneCnt
        res = 0

        for i in range(len(s) - 1):
            left = zero[i]
            right = one[-1] - one[i]
            res = max(res, right + left)
        return res


x = Solution()
print(x.maxScore("011101"))
