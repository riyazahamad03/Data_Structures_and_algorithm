class Solution1:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        i = 0
        while i < len(nums):
            rangeA = nums[i]
            cnt, fl = 0, False
            for j in range(i + 1, len(nums)):
                if nums[j]-nums[j-1] > 1:
                    break
                fl = True
                rangeB = nums[j]
                cnt += 1
            if fl:
                res.append(str(rangeA) + "->" + str(rangeB))
                i += cnt+1
            else:
                res.append(str(rangeA))
                i += 1
        return res


class Solution2:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res, idx = [], 0
        while idx < len(nums):
            rangeA = nums[idx]
            while idx + 1 < len(nums) and nums[idx] + 1 == nums[idx + 1]:
                idx += 1
            rangeB = nums[idx]

            if rangeA != rangeB:
                res.append(str(rangeA) + "->" + str(rangeB))
            else:
                res.append(str(rangeB))

            idx += 1
        return res


x = Solution1()
print(x.summaryRanges([0, 2, 3, 4, 6, 8, 9]))

x = Solution2()
print(x.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
