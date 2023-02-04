class solution:
    def findPivot(self,nums:list[int]):
        lSum = 0
        tot = sum(nums)
        for i in range(len(nums)):
            rSum = tot - lSum - nums[i]
            if lSum == rSum:
                return i
            lSum += nums[i]
        return -1
x = solution()
print(x.findPivot([1,7,3,6,5,6]))