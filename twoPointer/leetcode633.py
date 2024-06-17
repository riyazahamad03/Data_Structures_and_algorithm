class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c**0.5)
        while l <= r:
            sos = l * l + r * r
            if sos > c:
                r -= 1
            elif sos < c:
                l += 1
            else:
                return True
        return False


x = Solution()
print(x.judgeSquareSum(c=10000))
