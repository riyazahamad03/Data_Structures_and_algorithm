class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        for i in s:
            res += str(ord(i) - 96)
        transFormed = int(res)
        while k:
            new = 0
            while transFormed:
                new += transFormed % 10
                transFormed //= 10
            transFormed = new

            k -= 1
        return transFormed


x = Solution()
print(x.getLucky(s="iiii", k=1))
