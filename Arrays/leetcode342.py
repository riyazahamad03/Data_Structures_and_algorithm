import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n, 4) % 1 == 0

        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            return n % 4 == 0 and self.isPowerOfFour(n//4)

x = Solution()
print(x.isPowerOfFour(16))