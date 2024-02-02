class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []
        for i in range(1, 10):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    res.append(num)
        return sorted(res)
x = Solution()
print(x.sequentialDigits(10 , 100))