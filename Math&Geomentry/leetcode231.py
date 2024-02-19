class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # if n%2 or n <= 0:
        #     return False
        # return self.isPowerOfTwo(n//2)

        if n == 0:
            return False
        return n & (n - 1) == 0


x = Solution()
print(x.isPowerOfTwo(16))
