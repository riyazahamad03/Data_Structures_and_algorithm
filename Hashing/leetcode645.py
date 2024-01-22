class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        Set = set()
        for i in nums:
            if i in Set:
                rep = i
                break
            Set.add(i)
        miss = (n * (n + 1) // 2) - (sum(nums) - rep)
        return [rep, miss]


x = Solution()
print(x.findErrorNums([1, 2, 2, 4]))
