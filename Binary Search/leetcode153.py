# timeComplexity = O(logn)
# spaceComplexity = O(1)

class solution:
    def findMin(self,nums : list[int]):
        res = nums[0]
        low,high = 0,len(nums)-1
        
        while low <= high:
            if nums[low] < nums[high]:
                res = min(res,nums[low])
                break
            
            mid = (low + high) // 2
            res = min(res,nums[mid])

            if nums[mid] >= nums[low]:
                # move to right side
                low = mid + 1
            else:
                # move to left side
                high = mid - 1
        return res
x = solution()
print(x.findMin([3,4,5,1,2]))