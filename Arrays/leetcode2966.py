class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        if len(nums) < 3:
            return []
        nums.sort()

        for i in range(0, len(nums), 3):
            l = i
            r = i + 2
            if nums[r] - nums[l] > k:
                return []
        ans = []
        for i in range(0, len(nums), 3):
            res = []
            for j in range(i, i + 3):
                res.append(nums[j])
            ans.append(res)
        return ans


x = Solution()
print(x.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2))
