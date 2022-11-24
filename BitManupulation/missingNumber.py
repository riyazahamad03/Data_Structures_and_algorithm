'''
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

'''

class Solution:
    def MissingNumber(self, nums: list[int]):
        res = len(nums)

        for i in range(len(nums)):
            res+= i - nums[i]

        return res

x = Solution()
print(x.MissingNumber([1,2,3,4]))
