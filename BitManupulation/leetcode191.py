class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1 if (n & 1) else 0
            n >>= 1
        return res


x = Solution()
print(x.hammingWeight(int("100000000000000000000000000001011")))
