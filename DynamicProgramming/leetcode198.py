class solution:
    def houseRobber1(self,nums:int):
        r1,r2 = 0, 0
        for i in range(len(nums)):
            t = max(r2, r1 + nums[i])
            r1 = r2 
            r2 = t
        return r2
x = solution()
print(x.houseRobber1([1,2,3,1]))