class Solution:
    def pivotInteger(self, n: int) -> int:

        if n == 1:
            return 1

        sumn = n * ((n + 1) / 2)
        for i in range(n):
            left = i * ((i + 1) / 2)
            right = sumn - left + i

            if left == right:
                return i
        return -1


x = Solution()
print(x.pivotInteger(8))
