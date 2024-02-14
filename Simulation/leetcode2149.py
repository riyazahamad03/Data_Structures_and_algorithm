class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        even, odd = [], []
        for n in nums:
            if n > 0:
                even.append(n)
            else:
                odd.append(n)
        l = 0
        res = []
        while l < len(even):
            res.append(even[l])
            res.append(odd[l])
            l += 1
        return res


x = Solution()
print(x.rearrangeArray([3, 1, -2, -5, 2, -4]))
