class Solution:
    def rob(self, nums: list[int]) -> int:
        
        return max(nums[0],self.maxRobber(nums[1:]),self.maxRobber(nums[:-1]))

    def maxRobber(self,lst):
        r1,r2 =0,0
        for l in lst:
            maxRob = max(l + r1, r2)
            r1 = r2
            r2 = maxRob
        return r2
x = Solution()
print(x.maxRobber([1,2,3,1]))