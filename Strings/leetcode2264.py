class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = float("-inf")
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                res = max(res, int(num[i]))
        return str(res) * 3 if res != float("-inf") else ""


x = Solution()
print(x.largestGoodInteger("6777133339"))
