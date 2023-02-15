# 27. Remove Element
class solution:
    def removeElem(self,nums: list[int], val: int):
        i,k = 0,0
        while i < len(nums):
            if nums[i] != val:
                nums[k]=nums[i]
                k += 1
            i += 1
        return k,nums
x=solution()
print(x.removeElem([3,2,2,3],3))