class solution:
    def rotateArray(self,nums:list[int],k:int):
        k = k % len(nums)
        
        # reverse the entire array once
        l,r = 0,len(nums)-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        
        # reverse till the kth element
        l,r = 0, k-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        
        # reverse after kth element
        l,r= k, len(nums)-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        
        return nums
x = solution()
print(x.rotateArray([1,2,3,4,5,6,7],3))


