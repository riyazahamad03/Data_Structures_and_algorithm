class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        def slide(x):
            if x < 0:
                return 0
            res = 0
            l, curr = 0, 0
            for r in range(len(nums)):
                curr += nums[r]
                while curr > x:
                    curr -= nums[l]
                    l += 1
                res += r - l + 1
            return res

        return slide(goal) - slide(goal - 1)


x = Solution()
print(x.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
