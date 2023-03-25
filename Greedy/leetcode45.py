class solution:
    def jump(self,nums:list[int]):
        l , r , res = 0 ,0 ,0
        while r < len(nums) - 1:
            far = 0
            for i in range(l , r+1):
                far = max(far , i + nums[i])
            l = r + 1
            r = far
            res += 1
        return res
x = solution()
print(x.jump([2,3,1,1,4]))