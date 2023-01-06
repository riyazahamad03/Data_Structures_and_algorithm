# 15. 3Sum
class solution:
    def threeSum(self,nums:list[int])-> list[list[int]]:
        res = []
        nums.sort()
        for i,e in enumerate(nums):
            if i>0 and nums[i-1] == e:
                continue
            left,right = i+1,len(nums)-1
            
            while left < right:
                threeSum = e + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([e,nums[left],nums[right]])
                    left += 1
                    while nums[left-1]==nums[left] and left < right:
                        left+=1  

        return res
x = solution()

print(x.threeSum([-1,0,1,2,-1,-4]))
