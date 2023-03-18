class solution:
    def checkPossibility(self , nums:list[int]):
        ch = False
        for idex in range(len(nums) - 1):
            if nums[idex] <= nums[idex + 1]:
                continue
            if ch:
                return False
            if idex == 0 or nums[idex + 1] >= nums[idex - 1]:
                nums[idex] = nums[idex + 1]
            else:
                nums[idex + 1] = nums[idex]
            ch = True
        return True
x = solution()
print(x.checkPossibility([4,2,1]))  