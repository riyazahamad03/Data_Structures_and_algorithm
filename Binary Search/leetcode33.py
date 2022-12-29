# timeComplexity = O(logn)
class solution:
    def searchInRotatedArr(self,nums:list[int],target:int):
        low,high = 0, len(nums)-1

        while low<=high:
            mid  = (low+high)//2

            if nums[mid] == target:
                return mid
            # left sorted array
            if nums[low] <= nums[mid]:
                # left to right transition
                if target > nums[mid] or target < nums[low] :
                    low = mid+1
                else:
                    # stay in left side 
                    high = mid-1
            # right sorted array
            else:
                if target < nums[mid] or target > nums[high]:
                    # right to left transition
                    high = mid - 1
                else:
                    # stay in right side 
                    low = mid+1
        return -1

x = solution()
print(x.searchInRotatedArr([4,5,6,7,0,1,2],0))

