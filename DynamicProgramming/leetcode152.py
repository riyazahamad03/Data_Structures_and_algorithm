class solution:
    def maxProduct(self,nums:list[int]):
        i,Max,Min = 0,1,1
        res = nums[0]
        while i < len(nums):
            temp = Max * nums[i]
            Max = max(nums[i],nums[i]*Max,nums[i]*Min)
            Min = min(temp,nums[i],nums[i]*Min)
            res = max(Max,res)            
            i+=1
        return res
x=solution()
print(x.maxProduct([2,3,-2,4]))
