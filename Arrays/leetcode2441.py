class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        neg, pos = [-1] * 1001, [-1] * 1001

        for n in nums:
            if n < 0:
                neg[abs(n)] = 1
            else:
                pos[n] = 1
        for i in range(1000, -1, -1):
            if neg[i] == 1 and pos[i] == 1:
                return i
        return -1


x = Solution()
print(x.findMaxK(nums=[-1, 10, 6, 7, -7, 1]))
